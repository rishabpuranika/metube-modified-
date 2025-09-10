#!/usr/bin/env python3
"""
Script to help extract YouTube cookies from browser
Run this on your local machine where you have a browser with YouTube access
"""

import os
import sys
import json
import sqlite3
import shutil
from pathlib import Path

def get_chrome_cookies():
    """Extract cookies from Chrome browser"""
    try:
        # Chrome cookies location varies by OS
        if sys.platform == "win32":
            cookies_path = Path.home() / "AppData/Local/Google/Chrome/User Data/Default/Cookies"
        elif sys.platform == "darwin":
            cookies_path = Path.home() / "Library/Application Support/Google/Chrome/Default/Cookies"
        else:
            cookies_path = Path.home() / ".config/google-chrome/Default/Cookies"
        
        if not cookies_path.exists():
            return None
            
        # Copy cookies file to avoid locking issues
        temp_cookies = "/tmp/cookies_temp.db"
        shutil.copy2(cookies_path, temp_cookies)
        
        conn = sqlite3.connect(temp_cookies)
        cursor = conn.cursor()
        
        # Query YouTube cookies
        cursor.execute("""
            SELECT host_key, name, value, path, expires_utc, is_secure, is_httponly
            FROM cookies 
            WHERE host_key LIKE '%youtube.com%' OR host_key LIKE '%googlevideo.com%'
        """)
        
        cookies = cursor.fetchall()
        conn.close()
        os.remove(temp_cookies)
        
        return cookies
    except Exception as e:
        print(f"Error extracting Chrome cookies: {e}")
        return None

def format_cookies_txt(cookies):
    """Format cookies in Netscape format"""
    lines = ["# Netscape HTTP Cookie File"]
    
    for cookie in cookies:
        host, name, value, path, expires, secure, httponly = cookie
        
        # Convert Chrome timestamp to Unix timestamp
        if expires:
            expires = int(expires / 1000000 - 11644473600)
        else:
            expires = 0
            
        secure_flag = "TRUE" if secure else "FALSE"
        
        lines.append(f"{host}\tTRUE\t{path}\t{secure_flag}\t{expires}\t{name}\t{value}")
    
    return "\n".join(lines)

def create_cookies_txt():
    """Create cookies.txt file from browser cookies"""
    print("Extracting YouTube cookies from Chrome...")
    
    cookies = get_chrome_cookies()
    if not cookies:
        print("\n❌ Could not extract cookies from Chrome.")
        print("Manual steps:")
        print("1. Install 'Export Cookies' extension in Chrome")
        print("2. Visit youtube.com")
        print("3. Export cookies for youtube.com")
        print("4. Save as cookies.txt")
        return False
    
    cookies_content = format_cookies_txt(cookies)
    
    with open("cookies.txt", "w") as f:
        f.write(cookies_content)
    
    print(f"✅ Created cookies.txt with {len(cookies)} cookies")
    print("Upload this file to your server and update the config to use it.")
    return True

if __name__ == "__main__":
    print("🍪 YouTube Cookies Extractor")
    print("=" * 30)
    
    if not create_cookies_txt():
        print("\n📖 Alternative methods:")
        print("• Use browser extension: https://chrome.google.com/webstore/search/export%20cookies")
        print("• Use online tools (be careful with privacy)")
        print("• Use yt-dlp with --cookies-from-browser chrome")
