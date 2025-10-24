
from pydantic import BaseModel
   

class SubCategoryBase(BaseModel):
    name: str
    code: str

class SubCategoryCreate(SubCategoryBase):
    category_id: int

class SubCategoryResponse(SubCategoryBase):
    id: int
    category_id: int

    class Config:
        from_attributes = True

