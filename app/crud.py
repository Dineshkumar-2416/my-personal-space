from sqlalchemy.orm import Session
from app import models, schemas
import markdown

# Blog CRUD operations
def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()

def get_blogs(db: Session, skip: int = 0, limit: int = 100, published_only: bool = True):
    query = db.query(models.Blog)
    if published_only:
        query = query.filter(models.Blog.published == True)
    return query.order_by(models.Blog.created_at.desc()).offset(skip).limit(limit).all()

def create_blog(db: Session, blog: schemas.BlogCreate):
    # Convert markdown to HTML
    html_content = markdown.markdown(blog.content, extensions=['fenced_code', 'tables'])

    db_blog = models.Blog(
        title=blog.title,
        content=blog.content,
        html_content=html_content,
        published=blog.published
    )

    # Handle categories
    for category_name in blog.category_names:
        category = get_or_create_category(db, category_name)
        db_blog.categories.append(category)

    # Handle tags
    for tag_name in blog.tag_names:
        tag = get_or_create_tag(db, tag_name)
        db_blog.tags.append(tag)

    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def update_blog(db: Session, blog_id: int, blog: schemas.BlogUpdate):
    db_blog = get_blog(db, blog_id)
    if not db_blog:
        return None

    # Update blog fields
    db_blog.title = blog.title
    db_blog.content = blog.content
    db_blog.html_content = markdown.markdown(blog.content, extensions=['fenced_code', 'tables'])
    db_blog.published = blog.published

    # Update categories
    db_blog.categories.clear()
    for category_name in blog.category_names:
        category = get_or_create_category(db, category_name)
        db_blog.categories.append(category)

    # Update tags
    db_blog.tags.clear()
    for tag_name in blog.tag_names:
        tag = get_or_create_tag(db, tag_name)
        db_blog.tags.append(tag)

    db.commit()
    db.refresh(db_blog)
    return db_blog

def delete_blog(db: Session, blog_id: int):
    db_blog = get_blog(db, blog_id)
    if db_blog:
        db.delete(db_blog)
        db.commit()
        return True
    return False

# Category CRUD operations
def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_category_by_name(db: Session, name: str):
    return db.query(models.Category).filter(models.Category.name == name).first()

def get_categories(db: Session):
    return db.query(models.Category).all()

def get_or_create_category(db: Session, name: str):
    category = get_category_by_name(db, name)
    if not category:
        category = models.Category(name=name)
        db.add(category)
        db.commit()
        db.refresh(category)
    return category

def get_blogs_by_category(db: Session, category_name: str):
    category = get_category_by_name(db, category_name)
    if category:
        return category.blogs
    return []

# Tag CRUD operations
def get_tag(db: Session, tag_id: int):
    return db.query(models.Tag).filter(models.Tag.id == tag_id).first()

def get_tag_by_name(db: Session, name: str):
    return db.query(models.Tag).filter(models.Tag.name == name).first()

def get_tags(db: Session):
    return db.query(models.Tag).all()

def get_or_create_tag(db: Session, name: str):
    tag = get_tag_by_name(db, name)
    if not tag:
        tag = models.Tag(name=name)
        db.add(tag)
        db.commit()
        db.refresh(tag)
    return tag

def get_blogs_by_tag(db: Session, tag_name: str):
    tag = get_tag_by_name(db, tag_name)
    if tag:
        return tag.blogs
    return []
