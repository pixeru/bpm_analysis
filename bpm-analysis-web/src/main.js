import { BPMAnalyzer } from './bpm-analysis.js';
import { PlotGenerator } from './plotting.js';
import { AudioProcessor } from './audio-processor.js';

// Global variables
let currentFile = null;
let analyzer = null;
let plotGenerator = null;

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    setupEventListeners();
    analyzer = new BPMAnalyzer();
    plotGenerator = new PlotGenerator();
});

function setupEventListeners() {
    const fileInput = document.getElementById('fileInput');
    const uploadArea = document.getElementById('uploadArea');
    const analyzeBtn = document.getElementById('analyzeBtn');

    // File input handling
    fileInput.addEventListener('change', handleFileSelect);

    // Drag and drop handling
    uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadArea.classList.add('dragover');
    });

    uploadArea.addEventListener('dragleave', () => {
        uploadArea.classList.remove('dragover');
    });

    uploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadArea.classList.remove('dragover');
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            handleFile(files[0]);
        }
    });

    uploadArea.addEventListener('click', () => {
        fileInput.click();
    });
}

function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
        handleFile(file);
    }
}

function handleFile(file) {
    const supportedTypes = ['audio/wav', 'audio/mpeg', 'audio/mp4', 'audio/flac', 'audio/ogg'];
    
    if (!supportedTypes.includes(file.type) && !file.name.match(/\.(wav|mp3|m4a|flac|ogg)$/i)) {
        showError('Unsupported file type. Please select a WAV, MP3, M4A, FLAC, or OGG file.');
        return;
    }

    currentFile = file;
    displayFileInfo(file);
    document.getElementById('analyzeBtn').disabled = false;
}

function displayFileInfo(file) {
    const fileInfo = document.getElementById('fileInfo');
    const fileDetails = document.getElementById('fileDetails');
    
    const sizeStr = (file.size / 1024 / 1024).toFixed(2) + ' MB';
    
    fileDetails.innerHTML = `
        <p><strong>File:</strong> ${file.name}</p>
        <p><strong>Type:</strong> ${file.type || 'Unknown'}</p>
        <p><strong>Size:</strong> ${sizeStr}</p>
        <p><strong>Last Modified:</strong> ${file.lastModified ? new Date(file.lastModified).toLocaleString() : 'Unknown'}</p>
    `;
    
    fileInfo.style.display = 'block';
}

async function startAnalysis() {
    if (!currentFile) {
        showError('Please select a file first.');
        return;
    }

    try {
        // Disable the analyze button and show progress
        document.getElementById('analyzeBtn').disabled = true;
        showProgress('Loading audio file...', 10);

        // Process the audio file
        const audioProcessor = new AudioProcessor();
        const audioData = await audioProcessor.loadAudioFile(currentFile);
        
        showProgress('Preprocessing audio...', 25);
        const processedData = await audioProcessor.preprocessAudio(audioData);

        showProgress('Analyzing heartbeat patterns...', 50);
        
        // Get analysis parameters
        const startBpmHint = parseFloat(document.getElementById('startBpm').value) || null;
        
        // Run the BPM analysis
        const analysisResults = await analyzer.analyzeHeartbeat(processedData, {
            startBpmHint: startBpmHint,
            sampleRate: audioData.sampleRate
        });

        showProgress('Generating visualization...', 80);
        
        // Generate the plot
        await plotGenerator.createAnalysisPlot(
            processedData,
            analysisResults,
            document.getElementById('plotContainer')
        );

        showProgress('Complete!', 100);
        
        // Display results
        displayResults(analysisResults);
        
        // Hide progress and show results
        setTimeout(() => {
            document.getElementById('progressSection').style.display = 'none';
            document.getElementById('resultsSection').style.display = 'block';
            document.getElementById('analyzeBtn').disabled = false;
        }, 500);

    } catch (error) {
        console.error('Analysis error:', error);
        showError(`Analysis failed: ${error.message}`);
        document.getElementById('progressSection').style.display = 'none';
        document.getElementById('analyzeBtn').disabled = false;
    }
}

function displayResults(results) {
    const statsGrid = document.getElementById('statsGrid');
    
    const stats = [
        { label: 'Average BPM', value: results.averageBpm ? results.averageBpm.toFixed(1) : 'N/A' },
        { label: 'Peak BPM', value: results.peakBpm ? results.peakBpm.toFixed(1) : 'N/A' },
        { label: 'Min BPM', value: results.minBpm ? results.minBpm.toFixed(1) : 'N/A' },
        { label: 'Heart Rate Variability', value: results.hrv ? results.hrv.toFixed(1) + ' ms' : 'N/A' },
        { label: 'Total S1 Beats', value: results.totalS1Beats || 'N/A' },
        { label: 'S1-S2 Pairs', value: results.s1s2Pairs || 'N/A' }
    ];

    statsGrid.innerHTML = stats.map(stat => `
        <div class="stat-card">
            <div class="stat-value">${stat.value}</div>
            <div class="stat-label">${stat.label}</div>
        </div>
    `).join('');
}

function showProgress(message, percentage) {
    const progressSection = document.getElementById('progressSection');
    const statusText = document.getElementById('statusText');
    const progressFill = document.getElementById('progressFill');
    
    progressSection.style.display = 'block';
    statusText.textContent = message;
    progressFill.style.width = percentage + '%';
}

function showError(message) {
    const errorElement = document.getElementById('errorMessage');
    errorElement.textContent = message;
    errorElement.style.display = 'block';
    
    setTimeout(() => {
        errorElement.style.display = 'none';
    }, 5000);
}

// Make startAnalysis globally available
window.startAnalysis = startAnalysis;