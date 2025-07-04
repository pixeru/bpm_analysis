import os
import uuid
import tempfile
import logging
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json

# Import the BPM analysis modules
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

try:
    from bpm_analysis import analyze_wav_file, convert_to_wav
    from config import DEFAULT_PARAMS
except ImportError as e:
    logging.error(f"Failed to import BPM analysis modules: {e}")
    # Fallback imports
    analyze_wav_file = None
    convert_to_wav = None
    DEFAULT_PARAMS = {}

def index(request):
    """Main page with file upload form"""
    return render(request, 'analyzer/index.html')

@csrf_exempt
def upload_file(request):
    """Handle file upload and BPM analysis"""
    if request.method == 'POST':
        if 'audio_file' not in request.FILES:
            return JsonResponse({'error': 'No file uploaded'}, status=400)
        
        audio_file = request.FILES['audio_file']
        
        # Validate file type
        allowed_extensions = ['.wav', '.mp3', '.m4a', '.flac', '.ogg']
        file_extension = os.path.splitext(audio_file.name)[1].lower()
        
        if file_extension not in allowed_extensions:
            return JsonResponse({
                'error': f'Unsupported file type. Allowed types: {", ".join(allowed_extensions)}'
            }, status=400)
        
        try:
            # Generate unique analysis ID
            analysis_id = str(uuid.uuid4())
            
            # Create analysis directory
            analysis_dir = os.path.join(settings.MEDIA_ROOT, 'analyses', analysis_id)
            os.makedirs(analysis_dir, exist_ok=True)
            
            # Save uploaded file
            original_filename = audio_file.name
            uploaded_file_path = os.path.join(analysis_dir, f"original_{original_filename}")
            
            with open(uploaded_file_path, 'wb+') as destination:
                for chunk in audio_file.chunks():
                    destination.write(chunk)
            
            # Convert to WAV if necessary
            wav_file_path = os.path.join(analysis_dir, 'analysis.wav')
            if file_extension.lower() == '.wav':
                # Copy WAV file directly
                import shutil
                shutil.copy2(uploaded_file_path, wav_file_path)
            else:
                # Convert to WAV
                if convert_to_wav:
                    success = convert_to_wav(uploaded_file_path, wav_file_path)
                    if not success:
                        return JsonResponse({'error': 'Failed to convert audio file'}, status=500)
                else:
                    return JsonResponse({'error': 'Audio conversion not available'}, status=500)
            
            # Run BPM analysis
            if analyze_wav_file:
                try:
                    # Use default parameters
                    params = DEFAULT_PARAMS.copy()
                    start_bpm_hint = None
                    
                    # Run the analysis
                    analyze_wav_file(
                        wav_file_path,
                        params,
                        start_bpm_hint,
                        original_file_path=uploaded_file_path,
                        output_directory=analysis_dir
                    )
                    
                    # Save analysis metadata
                    metadata = {
                        'analysis_id': analysis_id,
                        'original_filename': original_filename,
                        'file_extension': file_extension,
                        'analysis_completed': True,
                        'error': None
                    }
                    
                    metadata_path = os.path.join(analysis_dir, 'metadata.json')
                    with open(metadata_path, 'w') as f:
                        json.dump(metadata, f)
                    
                    return JsonResponse({
                        'success': True,
                        'analysis_id': analysis_id,
                        'message': 'Analysis completed successfully'
                    })
                    
                except Exception as e:
                    logging.error(f"BPM analysis failed: {e}")
                    return JsonResponse({'error': f'Analysis failed: {str(e)}'}, status=500)
            else:
                return JsonResponse({'error': 'BPM analysis not available'}, status=500)
                
        except Exception as e:
            logging.error(f"File processing error: {e}")
            return JsonResponse({'error': f'File processing failed: {str(e)}'}, status=500)
    
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)

def view_result(request, analysis_id):
    """Display analysis results"""
    try:
        analysis_dir = os.path.join(settings.MEDIA_ROOT, 'analyses', str(analysis_id))
        
        if not os.path.exists(analysis_dir):
            messages.error(request, 'Analysis not found')
            return redirect('analyzer:index')
        
        # Load metadata
        metadata_path = os.path.join(analysis_dir, 'metadata.json')
        if os.path.exists(metadata_path):
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
        else:
            metadata = {'original_filename': 'Unknown', 'analysis_completed': False}
        
        # Find the generated HTML plot
        plot_files = []
        for file in os.listdir(analysis_dir):
            if file.endswith('_bpm_plot.html'):
                plot_files.append(file)
        
        if plot_files:
            # Use the first plot file found
            plot_filename = plot_files[0]
            plot_path = os.path.join(analysis_dir, plot_filename)
            
            # Read the HTML content
            with open(plot_path, 'r', encoding='utf-8') as f:
                plot_html = f.read()
        else:
            plot_html = None
        
        # Find other analysis files
        analysis_files = []
        for file in os.listdir(analysis_dir):
            if file.endswith(('.json', '.md', '.html')) and file != 'metadata.json':
                analysis_files.append(file)
        
        context = {
            'analysis_id': analysis_id,
            'metadata': metadata,
            'plot_html': plot_html,
            'analysis_files': analysis_files,
            'has_results': bool(plot_html)
        }
        
        return render(request, 'analyzer/result.html', context)
        
    except Exception as e:
        logging.error(f"Error viewing result: {e}")
        messages.error(request, f'Error loading results: {str(e)}')
        return redirect('analyzer:index')