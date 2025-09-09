# Deploying MeTube to Render

This guide will help you deploy MeTube to Render's free hosting platform.

## Prerequisites

1. A GitHub account
2. A Render account (free at render.com)
3. Git installed on your local machine

## Step 1: Prepare Your Repository

### 1.1 Initialize Git Repository (if not already done)
```bash
cd /home/rishvaish/Downloads/metube-2025.07.31
git init
```

### 1.2 Create .gitignore file
```bash
cat > .gitignore << 'EOF'
# Node modules
node_modules/
npm-debug.log*

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Downloads (don't commit downloaded files)
downloads/
*.mp4
*.mp3
*.mkv
*.avi

# Logs
*.log

# Build outputs
ui/dist/
EOF
```

### 1.3 Commit your files
```bash
git add .
git commit -m "Initial commit: MeTube for Render deployment"
```

## Step 2: Create GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click "New repository"
3. Name it `metube-render` (or any name you prefer)
4. Make it public (required for Render free tier)
5. Don't initialize with README (you already have files)
6. Click "Create repository"

### 2.1 Push to GitHub
```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/metube-render.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## Step 3: Deploy to Render

### 3.1 Connect to Render
1. Go to [Render Dashboard](https://render.com/dashboard)
2. Click "New +" and select "Web Service"
3. Connect your GitHub account if not already connected
4. Select your `metube-render` repository

### 3.2 Configure Service
- **Name**: `metube` (or your preferred name)
- **Region**: Choose closest to you (Oregon for US West)
- **Branch**: `main`
- **Runtime**: `Python 3`
- **Build Command**: `./build.sh`
- **Start Command**: `python3 app/main.py`

### 3.3 Environment Variables (Optional)
You can add these environment variables in Render's dashboard:

- `DOWNLOAD_MODE`: `limited` (default)
- `MAX_CONCURRENT_DOWNLOADS`: `2` (reduce for free tier)
- `DEFAULT_THEME`: `dark` or `light` or `auto`
- `LOGLEVEL`: `INFO`

### 3.4 Advanced Settings
- **Instance Type**: Free (for testing)
- **Auto Deploy**: Yes (recommended)

## Step 4: Deploy!

1. Click "Create Web Service"
2. Render will start building your app
3. This process takes 5-15 minutes for the first deployment
4. Monitor the build logs for any issues

## Step 5: Access Your App

Once deployed successfully:
1. Render will provide a URL like `https://metube-xxxx.onrender.com`
2. Visit this URL to access your MeTube instance
3. The UI should load and you can start downloading videos!

## Important Notes for Render Free Tier

⚠️ **Limitations on Free Tier:**
- Service spins down after 15 minutes of inactivity
- 512MB RAM limit
- 750 hours/month (enough for hobby use)
- Downloaded files are stored in `/tmp` and will be deleted when service restarts

⚠️ **File Storage:**
- Downloaded videos are temporary on Render free tier
- Files will be lost when the service restarts
- For permanent storage, you'd need to integrate with cloud storage (S3, Google Drive, etc.)

## Troubleshooting

### Build Fails
- Check build logs in Render dashboard
- Ensure all files are properly committed to GitHub
- Verify `build.sh` has execute permissions

### Service Won't Start
- Check service logs in Render dashboard
- Ensure Python dependencies are properly installed
- Verify Angular build completed successfully

### Can't Access UI
- Wait for build to complete (check logs)
- Ensure service is running (not sleeping)
- Check if PORT environment variable is properly handled

## Updating Your Deployment

To update your MeTube instance:
1. Make changes to your local code
2. Commit and push to GitHub:
```bash
git add .
git commit -m "Update MeTube"
git push origin main
```
3. Render will automatically redeploy (if auto-deploy is enabled)

## Custom Domain (Paid Plans)

If you upgrade to a paid Render plan, you can:
1. Add a custom domain in Render dashboard
2. Render provides free SSL certificates
3. Configure DNS to point to Render

---

**Enjoy your cloud-hosted MeTube instance! 🎉**
