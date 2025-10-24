from typing import List 
from pydantic import BaseModel
from .sub_category import SubCategoryResponse   

class CategoryBase(BaseModel):
    name: str
    code: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    subcategories: List[SubCategoryResponse] = []

    class Config:
        from_attributes = True