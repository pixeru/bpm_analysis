#!/usr/bin/env python3
"""
Test script to validate the Django setup and BPM analysis integration
"""

import os
import sys
import django
from django.conf import settings

# Add the current directory to the Python path
sys.path.insert(0, os.getcwd())

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bmp_analyzer.settings')
django.setup()

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    
    try:
        # Test Django imports
        from django.core.management import execute_from_command_line
        from django.urls import reverse
        print("✓ Django imports successful")
    except ImportError as e:
        print(f"✗ Django import error: {e}")
        return False
    
    try:
        # Test BPM analysis imports
        from bpm_analysis import analyze_wav_file, convert_to_wav
        from config import DEFAULT_PARAMS
        print("✓ BPM analysis imports successful")
    except ImportError as e:
        print(f"✗ BPM analysis import error: {e}")
        return False
    
    try:
        # Test analyzer app imports
        from analyzer.views import index, upload_file, view_result
        from analyzer.urls import urlpatterns
        print("✓ Analyzer app imports successful")
    except ImportError as e:
        print(f"✗ Analyzer app import error: {e}")
        return False
    
    return True

def test_directories():
    """Test that all required directories exist"""
    print("\nTesting directories...")
    
    required_dirs = [
        'media',
        'temp',
        'static',
        'templates',
        'templates/analyzer'
    ]
    
    all_good = True
    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"✓ {dir_path} exists")
        else:
            print(f"✗ {dir_path} missing")
            all_good = False
    
    return all_good

def test_templates():
    """Test that all required templates exist"""
    print("\nTesting templates...")
    
    required_templates = [
        'templates/base.html',
        'templates/analyzer/index.html',
        'templates/analyzer/result.html'
    ]
    
    all_good = True
    for template_path in required_templates:
        if os.path.exists(template_path):
            print(f"✓ {template_path} exists")
        else:
            print(f"✗ {template_path} missing")
            all_good = False
    
    return all_good

def test_configuration():
    """Test Django configuration"""
    print("\nTesting Django configuration...")
    
    try:
        from django.conf import settings
        print(f"✓ SECRET_KEY configured: {bool(settings.SECRET_KEY)}")
        print(f"✓ DEBUG mode: {settings.DEBUG}")
        print(f"✓ Apps installed: {len(settings.INSTALLED_APPS)}")
        print(f"✓ Database configured: {settings.DATABASES['default']['ENGINE']}")
        return True
    except Exception as e:
        print(f"✗ Configuration error: {e}")
        return False

def main():
    """Run all tests"""
    print("BPM Analysis Web App - Setup Validation")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_directories,
        test_templates,
        test_configuration
    ]
    
    all_passed = True
    for test in tests:
        if not test():
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("✓ All tests passed! The setup looks good.")
        print("\nTo start the web application:")
        print("1. cd bpm-analysis-web")
        print("2. python3 manage.py runserver 0.0.0.0:8000")
        print("3. Open http://localhost:8000 in your browser")
    else:
        print("✗ Some tests failed. Please check the errors above.")
    
    return all_passed

if __name__ == "__main__":
    main()