from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List, Optional

from app import crud, models, schemas
from app.database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Blog Site")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Home page - List all blogs
@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    blogs = crud.get_blogs(db)
    categories = crud.get_categories(db)
    tags = crud.get_tags(db)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "blogs": blogs,
        "categories": categories,
        "tags": tags
    })

# Create blog form page (must come before /blog/{blog_id})
@app.get("/blog/create", response_class=HTMLResponse)
async def create_blog_form(request: Request):
    return templates.TemplateResponse("create_blog.html", {
        "request": request,
        "blog": None,
        "mode": "create"
    })

# Edit blog form page (must come before /blog/{blog_id})
@app.get("/blog/edit/{blog_id}", response_class=HTMLResponse)
async def edit_blog_form(request: Request, blog_id: int, db: Session = Depends(get_db)):
    blog = crud.get_blog(db, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return templates.TemplateResponse("create_blog.html", {
        "request": request,
        "blog": blog,
        "mode": "edit"
    })

# View single blog (generic route, must come after specific routes)
@app.get("/blog/{blog_id}", response_class=HTMLResponse)
async def view_blog(request: Request, blog_id: int, db: Session = Depends(get_db)):
    blog = crud.get_blog(db, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return templates.TemplateResponse("blog_detail.html", {
        "request": request,
        "blog": blog
    })

# API: Create blog
@app.post("/api/blog")
async def create_blog(
    title: str = Form(...),
    content: str = Form(...),
    published: bool = Form(True),
    categories: str = Form(""),
    tags: str = Form(""),
    db: Session = Depends(get_db)
):
    # Parse comma-separated categories and tags
    category_list = [c.strip() for c in categories.split(",") if c.strip()]
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]

    blog_data = schemas.BlogCreate(
        title=title,
        content=content,
        published=published,
        category_names=category_list,
        tag_names=tag_list
    )

    blog = crud.create_blog(db, blog_data)
    return RedirectResponse(url=f"/blog/{blog.id}", status_code=303)

# API: Update blog
@app.post("/api/blog/{blog_id}")
async def update_blog(
    blog_id: int,
    title: str = Form(...),
    content: str = Form(...),
    published: bool = Form(True),
    categories: str = Form(""),
    tags: str = Form(""),
    db: Session = Depends(get_db)
):
    # Parse comma-separated categories and tags
    category_list = [c.strip() for c in categories.split(",") if c.strip()]
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]

    blog_data = schemas.BlogUpdate(
        title=title,
        content=content,
        published=published,
        category_names=category_list,
        tag_names=tag_list
    )

    blog = crud.update_blog(db, blog_id, blog_data)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return RedirectResponse(url=f"/blog/{blog.id}", status_code=303)

# API: Delete blog
@app.post("/api/blog/{blog_id}/delete")
async def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    success = crud.delete_blog(db, blog_id)
    if not success:
        raise HTTPException(status_code=404, detail="Blog not found")
    return RedirectResponse(url="/", status_code=303)

# Filter by category
@app.get("/category/{category_name}", response_class=HTMLResponse)
async def filter_by_category(request: Request, category_name: str, db: Session = Depends(get_db)):
    blogs = crud.get_blogs_by_category(db, category_name)
    categories = crud.get_categories(db)
    tags = crud.get_tags(db)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "blogs": blogs,
        "categories": categories,
        "tags": tags,
        "filter_type": "category",
        "filter_name": category_name
    })

# Filter by tag
@app.get("/tag/{tag_name}", response_class=HTMLResponse)
async def filter_by_tag(request: Request, tag_name: str, db: Session = Depends(get_db)):
    blogs = crud.get_blogs_by_tag(db, tag_name)
    categories = crud.get_categories(db)
    tags = crud.get_tags(db)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "blogs": blogs,
        "categories": categories,
        "tags": tags,
        "filter_type": "tag",
        "filter_name": tag_name
    })

# API: Get all categories
@app.get("/api/categories", response_model=List[schemas.Category])
async def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

# API: Get all tags
@app.get("/api/tags", response_model=List[schemas.Tag])
async def get_tags(db: Session = Depends(get_db)):
    return crud.get_tags(db)
