# Getting Started - Step by Step Guide

## Part 1: Test Locally (On Your Computer)

### Step 1: Open Terminal
- Open Command Prompt or PowerShell
- Navigate to your project folder:
```bash
cd d:\Project_1
```

### Step 2: Activate Virtual Environment
```bash
website_v1\Scripts\activate
```
You should see `(website_v1)` appear before your prompt.

### Step 3: Start the Server
```bash
uvicorn app.main:app --reload
```

You'll see output like:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Step 4: Open Your Browser
Go to: **http://127.0.0.1:8000**

You should see your blog home page!

### Step 5: Test Creating a Blog
1. Click the **"New Post"** button
2. Fill in:
   - **Title**: `My First Blog Post`
   - **Content**:
     ```markdown
     # Welcome to My Blog

     This is my **first** blog post!

     ## What I'll Write About
     - Travel experiences
     - Photography
     - Daily life

     Stay tuned for more!
     ```
   - **Categories**: `Personal, Updates`
   - **Tags**: `first-post, welcome`
3. Click **"Create Post"**

You should see your blog post with:
- Beautiful formatting
- Categories and tags as clickable buttons
- Edit and Delete options

### Step 6: Test Other Features
- Click on a category → See filtered posts
- Click "Edit" → Modify the post
- Go to home page → See all posts listed

### Step 7: Stop the Server
Press `CTRL+C` in the terminal when you're done testing.

---

## Part 2: Deploy to Railway (Make It Public)

### Step 1: Install Git (If Not Already Installed)
Download from: https://git-scm.com/downloads

Verify installation:
```bash
git --version
```

### Step 2: Create GitHub Account
1. Go to https://github.com
2. Click "Sign up"
3. Follow the registration process
4. Verify your email

### Step 3: Create New Repository on GitHub
1. Click the **"+"** icon (top right)
2. Click **"New repository"**
3. Repository name: `my-blog-site` (or any name you like)
4. Description: `Personal blogging website`
5. Keep it **Public** ✓
6. **DO NOT** check "Initialize with README"
7. Click **"Create repository"**

### Step 4: Configure Git on Your Computer
Open terminal and run (replace with YOUR info):
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 5: Push Code to GitHub
In your project folder (`d:\Project_1`), run these commands:

```bash
# Add all files to git
git add .

# Create first commit
git commit -m "Initial commit - Blog website ready for deployment"

# Connect to your GitHub repository (REPLACE with your actual URL)
git remote add origin https://github.com/YOUR_USERNAME/my-blog-site.git

# Set main branch
git branch -M main

# Push to GitHub
git push -u origin main
```

**Important**: Replace `YOUR_USERNAME` with your actual GitHub username!

Example:
```bash
git remote add origin https://github.com/john123/my-blog-site.git
```

When prompted:
- Username: Your GitHub username
- Password: Use a **Personal Access Token** (not your password)

#### How to Get Personal Access Token:
1. GitHub → Click your profile picture → Settings
2. Scroll down → Developer settings → Personal access tokens → Tokens (classic)
3. Generate new token → Give it a name: "Blog Deployment"
4. Check "repo" scope
5. Generate token → **COPY IT** (you won't see it again!)
6. Use this token as password when pushing

### Step 6: Deploy to Railway

#### A. Create Railway Account
1. Go to: https://railway.app
2. Click **"Login"**
3. Select **"Login with GitHub"**
4. Authorize Railway to access GitHub

#### B. Create New Project
1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Railway will show your GitHub repositories
4. Find and click **"my-blog-site"** (or your repo name)
5. Click **"Deploy Now"**

#### C. Wait for Deployment
You'll see logs like:
```
Installing dependencies...
Building application...
Starting server...
Deployment successful ✓
```

This takes **2-3 minutes**.

#### D. Generate Public URL
1. Click on your project in Railway dashboard
2. Click the **"Settings"** tab
3. Scroll to **"Networking"** section
4. Click **"Generate Domain"**
5. Railway creates a URL like: `my-blog-site-production.up.railway.app`

#### E. Copy Your URL
Your blog is now live! Copy the URL.

### Step 7: Test Your Live Website
1. Open the Railway URL in your browser
2. Test creating a blog post
3. Everything should work exactly like local!

### Step 8: Share with Your Friend
Send your friend:
1. **The URL**: `https://your-blog-site.up.railway.app`
2. **Instructions**:
   ```
   Hey! I made a blog website. You can create blog posts here:

   1. Go to: https://your-blog-site.up.railway.app
   2. Click "New Post"
   3. Write your blog in the form
   4. Click "Create Post"
   5. Copy the URL of your post and send it to me!

   The blog post URL will look like:
   https://your-blog-site.up.railway.app/blog/1
   ```

---

## Troubleshooting Common Issues

### Issue 1: "uvicorn: command not found"
**Solution**: Make sure virtual environment is activated
```bash
website_v1\Scripts\activate
```

### Issue 2: "Port already in use"
**Solution**: Another app is using port 8000
```bash
# Use a different port
uvicorn app.main:app --reload --port 8001
```
Then visit: http://127.0.0.1:8001

### Issue 3: Git push asks for password
**Solution**: Use Personal Access Token (see Step 5 above)

### Issue 4: Railway build fails
**Solution**: Check that all files are pushed to GitHub
```bash
# Verify files are on GitHub
# Go to: https://github.com/YOUR_USERNAME/my-blog-site
# You should see all folders: app/, templates/, static/, etc.
```

### Issue 5: Railway site loads but looks broken
**Solution**: Check Railway logs for errors
- Railway Dashboard → Your Project → Click "View Logs"
- Look for any error messages

### Issue 6: Blog posts not saving on Railway
**Solution**: Railway should handle SQLite automatically, but check:
- Railway Dashboard → Settings → Check "Storage" is enabled
- If not, contact Railway support (they're very helpful!)

---

## Quick Reference Commands

### Local Development:
```bash
# Start server
cd d:\Project_1
website_v1\Scripts\activate
uvicorn app.main:app --reload

# Stop server
CTRL+C
```

### Making Changes After Deployment:
```bash
# After editing your code locally:
git add .
git commit -m "Description of changes"
git push

# Railway automatically redeploys!
```

---

## What's Next?

After your friend creates blogs, you can:
1. View all blogs at: `your-site.com`
2. Click on specific posts they share
3. Filter by categories/tags
4. Even edit or add your own posts!

---

## Cost & Limits

**Railway Free Tier:**
- $5 credit per month (auto-renews)
- Perfect for personal blogs with moderate traffic
- If you exceed, Railway pauses until next month
- Can upgrade if needed

**GitHub:**
- Free for public repositories
- Unlimited storage for code

---

## Need Help?

If something doesn't work:
1. Check the error message carefully
2. Make sure all steps were followed
3. Verify files are pushed to GitHub
4. Check Railway deployment logs
5. Try redeploying in Railway

Common fixes:
- Re-run the failed command
- Check for typos in URLs/commands
- Make sure virtual environment is activated
- Restart the terminal and try again
