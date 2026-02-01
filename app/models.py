from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

# Association table for Blog-Category many-to-many relationship
blog_category = Table(
    'blog_category',
    Base.metadata,
    Column('blog_id', Integer, ForeignKey('blogs.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

# Association table for Blog-Tag many-to-many relationship
blog_tag = Table(
    'blog_tag',
    Base.metadata,
    Column('blog_id', Integer, ForeignKey('blogs.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)  # Markdown content
    html_content = Column(Text, nullable=False)  # Rendered HTML
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published = Column(Boolean, default=True)

    # Relationships
    categories = relationship("Category", secondary=blog_category, back_populates="blogs")
    tags = relationship("Tag", secondary=blog_tag, back_populates="blogs")

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    # Relationship
    blogs = relationship("Blog", secondary=blog_category, back_populates="categories")

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    # Relationship
    blogs = relationship("Blog", secondary=blog_tag, back_populates="tags")
