from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Category Schemas
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True

# Tag Schemas
class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        from_attributes = True

# Blog Schemas
class BlogBase(BaseModel):
    title: str
    content: str
    published: bool = True

class BlogCreate(BlogBase):
    category_names: Optional[List[str]] = []
    tag_names: Optional[List[str]] = []

class BlogUpdate(BlogBase):
    category_names: Optional[List[str]] = []
    tag_names: Optional[List[str]] = []

class Blog(BlogBase):
    id: int
    html_content: str
    created_at: datetime
    updated_at: datetime
    categories: List[Category] = []
    tags: List[Tag] = []

    class Config:
        from_attributes = True
