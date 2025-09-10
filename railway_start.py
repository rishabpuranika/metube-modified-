#!/usr/bin/env python3
"""
Robust startup script for Railway deployment
Handles missing config files gracefully
"""

import os
import sys
import json

def setup_environment():
    """Set up environment with fallbacks for missing config"""
    
    # Ensure we're in the right directory
    os.chdir('/app')
    
    # Set default environment variables if not set
    defaults = {
        'PORT': '8081',
        'HOST': '0.0.0.0',
        'DOWNLOAD_DIR': '/tmp/downloads',
        'STATE_DIR': '/tmp',
        'TEMP_DIR': '/tmp',
        'BASE_DIR': '/app'
    }
    
    for key, value in defaults.items():
        if key not in os.environ:
            os.environ[key] = value
    
    # Handle YTDL_OPTIONS_FILE
    config_file = os.environ.get('YTDL_OPTIONS_FILE', 'ytdl_config_android.json')
    
    # Check if the specified config file exists
    if not os.path.exists(config_file):
        print(f"⚠️  Config file '{config_file}' not found. Looking for alternatives...")
        
        # Try different config files in order of preference
        alternatives = [
            'ytdl_config_android.json',
            'ytdl_config.json', 
            'ytdl_config_cookies.json',
            'ytdl_config_enhanced.json'
        ]
        
        for alt_config in alternatives:
            if os.path.exists(alt_config):
                print(f"✅ Using alternative config: {alt_config}")
                os.environ['YTDL_OPTIONS_FILE'] = alt_config
                break
        else:
            # No config file found, create minimal one
            print("🔧 Creating minimal config file...")
            minimal_config = {
                "extractor_args": {
                    "youtube": {
                        "player_client": ["android"]
                    }
                },
                "format": "18/worst",
                "retries": 5
            }
            
            config_file = 'ytdl_config_minimal.json'
            with open(config_file, 'w') as f:
                json.dump(minimal_config, f, indent=2)
            
            os.environ['YTDL_OPTIONS_FILE'] = config_file
            print(f"✅ Created and using: {config_file}")
    
    # Ensure directories exist
    for dir_var in ['DOWNLOAD_DIR', 'STATE_DIR', 'TEMP_DIR']:
        dir_path = os.environ.get(dir_var)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
            print(f"📁 Ensured directory exists: {dir_path}")
    
    # Debug output
    print("\n🔧 Environment Summary:")
    print(f"  Port: {os.environ.get('PORT')}")
    print(f"  Host: {os.environ.get('HOST')}")
    print(f"  Config: {os.environ.get('YTDL_OPTIONS_FILE')}")
    print(f"  Download Dir: {os.environ.get('DOWNLOAD_DIR')}")
    print(f"  Working Dir: {os.getcwd()}")

def start_application():
    """Start the main application"""
    
    print("\n🚀 Starting MeTube application...")
    
    try:
        # Import and run the main application
        sys.path.insert(0, '/app/app')
        from main import *
        
    except Exception as e:
        print(f"❌ Failed to start application: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    print("🚂 MeTube Railway Startup")
    print("=" * 40)
    
    setup_environment()
    start_application()
