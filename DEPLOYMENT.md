# Deployment Guide - Blog Website

## Deploy to Railway (Recommended - Free Tier)

Railway is perfect for this blog because it:
- Supports SQLite databases with persistent storage
- Has a free tier ($5 credit/month)
- Easy deployment from GitHub
- Automatic HTTPS

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in (or create account)
2. Click "New repository"
3. Name it (e.g., "my-blog-site")
4. Keep it Public (required for free Railway deployment)
5. Click "Create repository"

### Step 2: Push Your Code to GitHub

Open terminal in your project directory and run:

```bash
git add .
git commit -m "Initial commit - Blog website"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual values.

### Step 3: Deploy to Railway

1. Go to [Railway](https://railway.app)
2. Click "Login" and sign in with GitHub
3. Click "New Project"
4. Click "Deploy from GitHub repo"
5. Select your blog repository
6. Railway will automatically:
   - Detect it's a Python app
   - Install dependencies from requirements.txt
   - Use the Procfile to start the app
7. Wait 2-3 minutes for deployment

### Step 4: Get Your Public URL

1. In Railway dashboard, click on your project
2. Click on the "Settings" tab
3. Scroll to "Domains" section
4. Click "Generate Domain"
5. Copy the URL (e.g., `your-blog.up.railway.app`)

### Step 5: Share with Your Friend

Send your friend:
- The website URL: `https://your-blog.up.railway.app`
- Tell them to:
  - Click "New Post" to create a blog
  - Write in Markdown
  - Add categories and tags
  - Click "Create Post"
  - Share the specific blog post URL with you

Example blog post URL: `https://your-blog.up.railway.app/blog/1`

---

## Alternative: Deploy to Render (Another Free Option)

**Note**: Render's free tier doesn't persist SQLite databases between deployments. Use Railway instead for this project.

If you still want to use Render:

1. Go to [Render](https://render.com)
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - Name: your-blog-site
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Click "Create Web Service"
7. Wait for deployment

**Important**: With Render free tier, your database will reset on each deployment. Consider upgrading to use PostgreSQL or use Railway instead.

---

## How Your Friend Can Use the Blog

1. **Create a Blog Post**:
   - Go to your blog URL
   - Click "New Post"
   - Write the blog title
   - Write content in Markdown
   - Add categories (e.g., "Personal, Travel")
   - Add tags (e.g., "adventure, photos")
   - Click "Create Post"

2. **Share a Blog Post**:
   - After creating, they'll see the blog post
   - Copy the URL from browser (e.g., `https://your-blog.up.railway.app/blog/3`)
   - Send you that link

3. **View All Blogs**:
   - Go to the home page
   - All published blogs are listed
   - Click on any blog to read it

---

## Troubleshooting

### Build Failed
- Check that all files are committed to GitHub
- Verify requirements.txt is present
- Check Railway/Render logs for error messages

### Database Not Saving
- On Railway: Should work automatically with persistent storage
- On Render: Free tier doesn't persist SQLite - need to upgrade or use Railway

### Can't Access Website
- Wait 2-3 minutes after deployment
- Check Railway/Render dashboard for deployment status
- Make sure you generated a domain in Railway settings

---

## Cost

- **Railway Free Tier**: $5 credit/month (renews automatically)
- For a simple blog, this should be enough for moderate usage
- If you run out, Railway will pause the service until next month

---

## Need Help?

Common issues:
1. Website loads but looks broken → Check static files are being served
2. Can't create posts → Check database write permissions
3. Markdown not rendering → Verify markdown package is in requirements.txt
