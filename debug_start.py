#!/usr/bin/env python3
"""
Debug script to help identify Railway startup issues
"""
import os
import sys
import traceback

def debug_environment():
    print("🔍 Environment Debug Information")
    print("=" * 50)
    
    # Check Python version
    print(f"Python version: {sys.version}")
    
    # Check environment variables
    env_vars = [
        'PORT', 'HOST', 'DOWNLOAD_DIR', 'YTDL_OPTIONS_FILE',
        'RAILWAY_PROJECT_ID', 'RAILWAY_SERVICE_NAME'
    ]
    
    print("\n📋 Environment Variables:")
    for var in env_vars:
        value = os.environ.get(var, 'NOT SET')
        print(f"  {var}: {value}")
    
    # Check file system
    print("\n📁 File System Check:")
    
    required_files = [
        'app/main.py',
        'ytdl_config_android.json',
        'ui/dist/metube/browser/index.html'
    ]
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} - MISSING!")
    
    # Check directory creation
    print("\n📂 Directory Creation Test:")
    try:
        os.makedirs('/tmp/downloads', exist_ok=True)
        print("  ✅ /tmp/downloads created successfully")
    except Exception as e:
        print(f"  ❌ Failed to create /tmp/downloads: {e}")
    
    # Test imports
    print("\n📦 Package Import Test:")
    packages = ['aiohttp', 'socketio', 'yt_dlp', 'mutagen', 'watchfiles']
    
    for package in packages:
        try:
            __import__(package)
            print(f"  ✅ {package}")
        except ImportError as e:
            print(f"  ❌ {package} - {e}")
    
    # Test yt-dlp
    print("\n🎬 yt-dlp Test:")
    try:
        from yt_dlp import YoutubeDL
        with YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(
                'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                download=False
            )
            if info:
                print(f"  ✅ yt-dlp works: {info.get('title', 'Unknown')}")
            else:
                print("  ❌ yt-dlp failed to extract info")
    except Exception as e:
        print(f"  ❌ yt-dlp error: {e}")

def test_server_start():
    print("\n🚀 Server Start Test:")
    try:
        # Change to app directory for imports
        sys.path.insert(0, '/app/app')
        os.chdir('/app')
        
        from app.main import app, config
        print(f"  ✅ App imported successfully")
        print(f"  ✅ Config loaded: {config.HOST}:{config.PORT}")
        print(f"  ✅ Download dir: {config.DOWNLOAD_DIR}")
        return True
        
    except Exception as e:
        print(f"  ❌ Server start failed: {e}")
        print(f"  Traceback: {traceback.format_exc()}")
        return False

if __name__ == "__main__":
    print("🐛 MeTube Railway Debug")
    print("=" * 60)
    
    debug_environment()
    
    if test_server_start():
        print("\n✅ All checks passed! Starting main application...")
        try:
            exec(open('/app/app/main.py').read())
        except Exception as e:
            print(f"❌ Main app failed: {e}")
            sys.exit(1)
    else:
        print("\n❌ Pre-flight checks failed!")
        sys.exit(1)
