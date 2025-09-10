# 🍪 YouTube Cookies Setup for MeTube

This guide helps you set up cookies to bypass YouTube's bot detection on Render and other hosting platforms.

## 🚨 Why Cookies Are Needed

YouTube blocks many cloud hosting providers' IP addresses to prevent automated downloads. Using browser cookies helps MeTube appear as a legitimate browser session.

## 📋 Method 1: Browser Extension (Recommended)

### Step 1: Install Extension
**Chrome:** [Export Cookies](https://chrome.google.com/webstore/detail/export-cookies/cclelndahbckbenkjhflpdbgdldlbecc)
**Firefox:** [cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)

### Step 2: Export Cookies
1. Visit `youtube.com` in your browser
2. (Optional) Log into your YouTube account
3. Click the extension icon
4. Export cookies for `youtube.com` domain
5. Save as `cookies.txt` in Netscape format

### Step 3: Upload to Repository
1. Replace the `cookies.txt` file in your repository
2. Commit and push changes:
   ```bash
   git add cookies.txt
   git commit -m "Update YouTube cookies"
   git push origin main
   ```

## 🔧 Method 2: Python Script (Local Machine)

Run the included `get_cookies.py` script on your local machine:

```bash
python3 get_cookies.py
```

This will extract cookies from Chrome automatically.

## 🛠️ Method 3: Manual Cookie Extraction

### Chrome DevTools Method:
1. Open YouTube in Chrome
2. Press `F12` to open DevTools
3. Go to Application → Cookies → https://youtube.com
4. Copy relevant cookies manually

### Key Cookies to Include:
- `CONSENT`
- `VISITOR_INFO1_LIVE` 
- `__Secure-YEC`
- `PREF`
- Any cookies starting with `__Secure-`

## 📝 Cookies.txt Format

```
# Netscape HTTP Cookie File
.youtube.com	TRUE	/	FALSE	1735689600	CONSENT	PENDING+123
.youtube.com	TRUE	/	TRUE	1735689600	__Secure-YEC	abc123def
.youtube.com	TRUE	/	FALSE	1735689600	VISITOR_INFO1_LIVE	xyz789
```

Format: `domain` `subdomain` `path` `secure` `expiration` `name` `value`

## ⚡ Alternative Configurations

If cookies don't work, try these fallback configs:

### Config 1: Basic (no cookies)
```bash
# In Render dashboard, set YTDL_OPTIONS_FILE to:
ytdl_config.json
```

### Config 2: Enhanced (conservative)
```bash
# In Render dashboard, set YTDL_OPTIONS_FILE to:
ytdl_config_enhanced.json
```

### Config 3: Cookies + Android client
```bash
# In Render dashboard, set YTDL_OPTIONS_FILE to:
ytdl_config_cookies.json
```

## 🔄 Updating Cookies

Cookies expire! Update them every few weeks:

1. Re-export cookies using the same method
2. Replace `cookies.txt` in your repository
3. Push changes to trigger Render redeploy

## 🔐 Security Notes

- **Never commit cookies from logged-in sessions** to public repositories
- Use cookies from incognito/private browsing when possible
- Regularly rotate cookies for security

## 🚫 Troubleshooting

### Still getting "No video formats found"?

1. **Check cookie freshness** - Export new cookies
2. **Try different config** - Switch between config files
3. **Use shorter URLs** - Remove tracking parameters
4. **Test with audio-only** - Less likely to be blocked
5. **Try different hosting** - Railway, Fly.io, etc.

### Common Issues:

- **Expired cookies**: Re-export fresh cookies
- **Wrong format**: Ensure Netscape format, not JSON
- **Missing key cookies**: Include CONSENT and VISITOR_INFO1_LIVE
- **IP still blocked**: Try VPN or different hosting provider

## 📞 Support

If you're still having issues:
1. Check Render deployment logs
2. Enable DEBUG logging in render.yaml
3. Test with different video URLs
4. Try deploying to a different region

## 🎯 Expected Results

After proper cookie setup:
- ✅ YouTube videos download successfully
- ✅ Various quality options available
- ✅ No "bot detection" errors
- ✅ Consistent download speeds
