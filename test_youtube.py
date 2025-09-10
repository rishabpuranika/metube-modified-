#!/usr/bin/env python3
"""
Test script to verify YouTube extraction works on Render
Run this script in Render console to test different configurations
"""

import json
import sys
import os
from yt_dlp import YoutubeDL

def test_config(config_name, config):
    """Test a specific yt-dlp configuration"""
    print(f"\n🧪 Testing {config_name}...")
    print("-" * 40)
    
    test_url = "https://www.youtube.com/watch?v=Zv2a6ixXEQc"
    
    try:
        with YoutubeDL(config) as ydl:
            # First, try to extract info only
            info = ydl.extract_info(test_url, download=False)
            
            if info:
                print(f"✅ SUCCESS: {info.get('title', 'Unknown')}")
                print(f"   Duration: {info.get('duration', 'Unknown')} seconds")
                print(f"   Uploader: {info.get('uploader', 'Unknown')}")
                
                # Check available formats
                formats = info.get('formats', [])
                print(f"   Available formats: {len(formats)}")
                
                if formats:
                    for fmt in formats[:3]:  # Show first 3 formats
                        print(f"   - {fmt.get('format_id')}: {fmt.get('format_note', 'Unknown')} ({fmt.get('ext')})")
                
                return True
            else:
                print("❌ FAILED: No info extracted")
                return False
                
    except Exception as e:
        print(f"❌ FAILED: {str(e)}")
        return False

def main():
    print("🎬 YouTube Extraction Test for Render")
    print("=" * 50)
    
    # Test different configurations
    configs = {
        "Basic Android": {
            "extractor_args": {
                "youtube": {
                    "player_client": ["android"]
                }
            },
            "format": "worst",
            "quiet": True
        },
        
        "Android + iOS": {
            "extractor_args": {
                "youtube": {
                    "player_client": ["android", "ios"]
                }
            },
            "format": "18/worst",
            "quiet": True
        },
        
        "Mobile Web": {
            "extractor_args": {
                "youtube": {
                    "player_client": ["mweb"]
                }
            },
            "format": "worst",
            "quiet": True
        },
        
        "Default (No Config)": {},
    }
    
    results = {}
    
    for name, config in configs.items():
        results[name] = test_config(name, config)
    
    # Summary
    print("\n📊 SUMMARY")
    print("=" * 30)
    working_configs = []
    for name, success in results.items():
        status = "✅ WORKS" if success else "❌ FAILED"
        print(f"{name}: {status}")
        if success:
            working_configs.append(name)
    
    if working_configs:
        print(f"\n🎉 Working configurations: {', '.join(working_configs)}")
        print("\nRecommended action:")
        print("1. Use the first working config in your ytdl_config.json")
        print("2. Update YTDL_OPTIONS_FILE in Render dashboard")
        print("3. Redeploy your service")
    else:
        print("\n😞 No configurations worked.")
        print("This suggests Render's IP is heavily blocked by YouTube.")
        print("\nTry:")
        print("1. Different hosting provider (Railway, Fly.io)")
        print("2. Using real browser cookies")
        print("3. Proxy/VPN solution")

if __name__ == "__main__":
    main()
