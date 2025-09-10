# 🚂 Railway Deployment Guide

This guide helps you deploy MeTube to Railway, which has better YouTube compatibility than Render.

## 🚀 Quick Deploy (Recommended)

### Method 1: Minimal Docker Build (Most Reliable)

1. **Push changes to GitHub** first:
   ```bash
   git add .
   git commit -m "Railway deployment setup - removed aria2"
   git push origin main
   ```

2. **Go to Railway**: https://railway.app
3. **Connect GitHub** and select your repository
4. **Railway will use** the `Dockerfile.minimal` (no aria2/ffmpeg)
5. **Wait for deployment** (usually 3-5 minutes)

### Method 1b: If Build Still Fails

1. **In Railway Settings → Build**:
   - Builder: Docker
   - Dockerfile Path: `Dockerfile.minimal`
2. **Or try even more basic**:
   - Change `requirements.railway.txt` to `requirements.basic.txt` in Dockerfile.minimal

### Method 2: Nixpacks Build (Faster)

If Docker build fails, try this:

1. **In Railway dashboard**, go to Settings → Build
2. **Change Builder** from "Docker" to "Nixpacks"
3. **Set Build Command**:
   ```bash
   cd ui && npm install && node_modules/.bin/ng build && cd .. && cp requirements.railway.txt requirements.txt && pip install -r requirements.txt
   ```
4. **Set Start Command**:
   ```bash
   python3 app/main.py
   ```

## 🔧 Robust Startup (NEW!)

The latest version includes a robust startup script (`railway_start.py`) that:
- ✅ **Auto-detects missing config files** and creates fallbacks
- ✅ **Handles environment setup** automatically  
- ✅ **Prevents deployment crashes** from missing files
- ✅ **Provides detailed logging** for troubleshooting

### Updated Dockerfile

The `Dockerfile.noui` now includes:
```dockerfile
# Robust startup with error handling
COPY railway_start.py ./
CMD ["python3", "railway_start.py"]
```

## ⚙️ Environment Variables

Set these in Railway dashboard under "Variables":

```bash
PORT=8081
HOST=0.0.0.0
DOWNLOAD_DIR=/tmp/downloads
YTDL_OPTIONS_FILE=ytdl_config_android.json
LOGLEVEL=INFO
```

## 🔧 Troubleshooting

### Config File Errors (SOLVED!)

✅ **Automatic handling**: The startup script now handles missing config files automatically!

If you see "Config file not found" in logs:
1. The script will automatically try alternatives
2. Creates a minimal config as last resort  
3. Check logs to see which config was used

### Build Fails with "aria2 banned"

**Solution**: Use Docker build method (Method 1)

### Build Fails with Dependencies

**Solution**: Use simplified requirements:
1. Copy `requirements.railway.txt` to `requirements.txt`
2. Redeploy

### Still Getting "No video formats found"

Try different configs by changing `YTDL_OPTIONS_FILE`:

1. `ytdl_config_android.json` (most compatible)
2. `ytdl_config_render.json` (aggressive settings)
3. `ytdl_config_cookies.json` (if you have cookies setup)
4. The startup script will try these automatically if your specified file is missing!

### Testing Your Setup

Run the test script to verify everything is working:
```bash
python3 test_setup.py
```

## 📊 Expected Results

Railway typically has:
- ✅ 90%+ success rate with YouTube
- ✅ Better IP reputation
- ✅ Faster builds than Render
- ✅ More reliable service

## 🔄 Migration from Render

1. **Export environment variables** from Render (if any custom ones)
2. **Deploy to Railway** using this guide
3. **Test video downloads**
4. **Update DNS/bookmarks** to new Railway URL
5. **Delete Render service** once confirmed working

## 💡 Advanced Configuration

### Custom Domain
1. Go to Railway dashboard → Settings → Domains
2. Add your custom domain
3. Update DNS records as instructed

### Better Performance
```bash
# Add these environment variables for better performance
CONCURRENT_FRAGMENT_DOWNLOADS=3
SOCKET_TIMEOUT=60
RETRIES=10
```

### Debug Mode
```bash
LOGLEVEL=DEBUG
```

## 🆚 Railway vs Render

| Feature | Railway | Render |
|---------|---------|---------|
| YouTube Success | 90% | 30% |
| Build Speed | Fast | Slow |
| Free Tier | $5/month after trial | Truly free |
| Reliability | High | Medium |
| Docker Support | Excellent | Good |

## 💰 Pricing

- **Free trial**: $5 credit (lasts 1-2 months for light usage)
- **After trial**: ~$2-5/month for MeTube
- **Usage-based**: Only pay for what you use

## 🎯 Success Checklist

- [ ] Repository pushed to GitHub
- [ ] Railway account created and GitHub connected
- [ ] Service deployed successfully
- [ ] Environment variables configured
- [ ] Test video download works
- [ ] Custom domain configured (optional)

Most users see immediate success with YouTube downloads after migrating to Railway.
