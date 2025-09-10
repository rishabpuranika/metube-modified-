#!/usr/bin/env python3
"""
Quick test script to verify MeTube setup
Tests config files, dependencies, and basic functionality
"""

import os
import sys
import json
import importlib.util

def check_file(filepath):
    """Check if file exists and is readable"""
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                content = f.read()
                if filepath.endswith('.json'):
                    json.loads(content)  # Validate JSON
                print(f"✅ {filepath} - OK ({len(content)} bytes)")
                return True
        except Exception as e:
            print(f"❌ {filepath} - Error: {e}")
            return False
    else:
        print(f"⚠️  {filepath} - Not found")
        return False

def check_import(module_name):
    """Check if module can be imported"""
    try:
        __import__(module_name)
        print(f"✅ {module_name} - OK")
        return True
    except ImportError as e:
        print(f"❌ {module_name} - Error: {e}")
        return False

def check_environment():
    """Check environment variables"""
    required_vars = ['PORT', 'HOST', 'DOWNLOAD_DIR', 'STATE_DIR', 'TEMP_DIR']
    optional_vars = ['YTDL_OPTIONS_FILE', 'BASE_DIR']
    
    print("\n📋 Environment Variables:")
    for var in required_vars:
        value = os.environ.get(var)
        if value:
            print(f"✅ {var} = {value}")
        else:
            print(f"⚠️  {var} - Not set")
    
    for var in optional_vars:
        value = os.environ.get(var)
        if value:
            print(f"ℹ️  {var} = {value}")

def test_ytdl_config():
    """Test yt-dlp configuration loading"""
    config_file = os.environ.get('YTDL_OPTIONS_FILE', 'ytdl_config_android.json')
    
    print(f"\n🔧 Testing ytdl config: {config_file}")
    
    if check_file(config_file):
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                print(f"  📝 Config keys: {list(config.keys())}")
                
                # Check specific important configs
                if 'extractor_args' in config:
                    print(f"  🎯 Extractor args: {config['extractor_args']}")
                if 'format' in config:
                    print(f"  📹 Format: {config['format']}")
                    
        except Exception as e:
            print(f"  ❌ Config parse error: {e}")

def main():
    print("🧪 MeTube Configuration Test")
    print("=" * 50)
    
    print("\n📁 File System Check:")
    files_to_check = [
        'app/main.py',
        'requirements.railway.txt',
        'railway_start.py',
        'ytdl_config_android.json',
        'ytdl_config.json',
        'ytdl_config_render.json',
        'cookies.txt'
    ]
    
    for file_path in files_to_check:
        check_file(file_path)
    
    print("\n📦 Python Dependencies:")
    deps_to_check = [
        'aiohttp',
        'yt_dlp',
        'aiofiles',
        'json'
    ]
    
    for dep in deps_to_check:
        check_import(dep)
    
    check_environment()
    test_ytdl_config()
    
    print("\n🎯 Working Directory:")
    print(f"  📂 Current: {os.getcwd()}")
    print(f"  📋 Contents: {os.listdir('.')}")
    
    # Test if we can create directories
    print("\n📁 Directory Creation Test:")
    test_dirs = ['/tmp/downloads', '/tmp/test_metube']
    for test_dir in test_dirs:
        try:
            os.makedirs(test_dir, exist_ok=True)
            print(f"✅ {test_dir} - OK")
        except Exception as e:
            print(f"❌ {test_dir} - Error: {e}")
    
    print("\n🏁 Test completed!")

if __name__ == "__main__":
    main()
