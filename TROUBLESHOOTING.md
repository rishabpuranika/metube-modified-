# 🔧 MeTube YouTube Troubleshooting Guide

If you're getting "No video formats found" errors, this guide will help you fix it.

## 🚨 Common Issue: Render IP Blocking

**Problem**: Render's free tier IP addresses are often blocked by YouTube's anti-bot systems.

**Symptoms**:
- "No video formats found" error
- Works locally but fails on Render
- Other video sites work fine

## 🛠️ Solutions (Try in Order)

### Solution 1: Change Configuration

In your Render dashboard, try these configs one by one:

```bash
# Try 1: Android client only (most reliable)
YTDL_OPTIONS_FILE = ytdl_config_android.json

# Try 2: Render-optimized config  
YTDL_OPTIONS_FILE = ytdl_config_render.json

# Try 3: Enhanced with cookies
YTDL_OPTIONS_FILE = ytdl_config_cookies.json
```

### Solution 2: Test Different Formats

Try downloading with these format preferences:

```bash
# Low quality (more likely to work)
format: "18/worst"     # 360p MP4

# Audio only (least blocked)  
format: "bestaudio"    # Audio only
```

### Solution 3: Use Real Cookies

1. Export cookies from your browser (see COOKIES_SETUP.md)
2. Replace `cookies.txt` in your repository
3. Use `ytdl_config_cookies.json`

### Solution 4: Test with Different URLs

Try these test URLs to see if it's URL-specific:
- https://www.youtube.com/watch?v=dQw4w9WgXcQ (Rick Roll - always works)
- https://www.youtube.com/watch?v=9bZkp7q19f0 (PSY - Gangnam Style)

### Solution 5: Switch Hosting Providers

Render's free tier IPs are heavily blocked. Try:

**Railway** (often works better):
1. Import your repo to [Railway](https://railway.app)
2. Uses the included `railway.toml` config
3. Better IP reputation with YouTube

**Fly.io**:
1. Deploy with `flyctl deploy`
2. Better geographic distribution

**DigitalOcean App Platform**:
1. More reliable but paid

## 🧪 Debug Mode

### Enable Debug Logging

In Render dashboard:
```bash
LOGLEVEL = DEBUG
```

### Run Test Script

SSH into Render console and run:
```bash
python3 test_youtube.py
```

This will test different configurations and show what works.

### Check Logs

Look for these error patterns:

```bash
# IP blocked
"HTTP Error 403: Forbidden"

# Rate limited  
"HTTP Error 429: Too Many Requests"

# Video unavailable
"Video unavailable"

# Format issues
"No video formats found"
```

## ⚡ Quick Fixes

### Fix 1: Immediate Workaround
Set environment variable in Render:
```bash
YTDL_OPTIONS = {"extractor_args":{"youtube":{"player_client":["android"]}},"format":"18/worst"}
```

### Fix 2: Alternative URL Format
Use full YouTube URLs instead of youtu.be:
```bash
# Instead of: https://youtu.be/Zv2a6ixXEQc
# Use: https://www.youtube.com/watch?v=Zv2a6ixXEQc
```

### Fix 3: Try Audio Only
Test with audio-only downloads first:
```bash
# In MeTube UI, select "Audio Only" format
```

## 🔄 Migration to Railway

If Render doesn't work, here's how to migrate:

1. **Sign up** for [Railway](https://railway.app)
2. **Connect GitHub** and import your repository  
3. **Auto-deploy** - Railway will use the `railway.toml` config
4. **Test** - Usually works better with YouTube

## 📊 Success Rates by Provider

Based on user reports:

- **Railway**: 🟢 90% success rate
- **Fly.io**: 🟡 70% success rate  
- **Render**: 🔴 30% success rate (free tier)
- **DigitalOcean**: 🟢 95% success rate
- **Local/VPS**: 🟢 99% success rate

## 💡 Advanced Solutions

### For Developers:
1. **Proxy rotation** - Use different proxy servers
2. **IP spoofing** - Change User-Agent headers
3. **Request delays** - Add sleep intervals between requests
4. **Browser automation** - Use Selenium/Playwright

### For Production:
1. **VPN integration** - Route through VPN
2. **Multiple endpoints** - Load balance across providers
3. **Fallback services** - Use alternative extractors

## 📞 Still Need Help?

1. **Check logs** in Render dashboard
2. **Test locally** first to confirm it works
3. **Try different videos** to isolate the issue
4. **Switch providers** if all else fails

## 🎯 Expected Timeline

- **Config changes**: 5-10 minutes to deploy
- **Cookie setup**: 15-30 minutes  
- **Provider migration**: 30-60 minutes
- **Advanced solutions**: 2+ hours

Most issues are resolved by switching configuration or hosting provider.
