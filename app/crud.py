from sqlalchemy.orm import Session
from . import models
from app.schemas import CategoryCreate
from app.schemas import SubCategoryCreate
from fastapi import HTTPException


def create_category(db: Session, category:CategoryCreate):
    db_category = models.Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session):
    return db.query(models.Category).all()

def get_category_by_id( db: Session ,category_id: int):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

def update_category(db: Session, category_id: int, category:CategoryCreate):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        for key, value in category.model_dump().items():
            setattr(db_category, key, value)
        db.commit()
        db.refresh(db_category)
    return db_category

"""
          SubCategory Crud             """



def create_subcategory(db: Session, subcategory:SubCategoryCreate):
    db_sub = models.SubCategory(**subcategory.model_dump())  
    db.add(db_sub)
    db.commit()
    db.refresh(db_sub)
    return db_sub

def update_subcategory(db: Session, subcategory_id: int, updated_subcategory:SubCategoryCreate):
    db_sub = db.query(models.SubCategory).filter(models.SubCategory.id == subcategory_id).first()
    if not db_sub:
        return None
    for key, value in updated_subcategory.model_dump().items():
        setattr(db_sub, key, value)
    db.commit()
    db.refresh(db_sub)
    return db_sub

def get_subcategories(db: Session):
    return db.query(models.SubCategory).all()

def get_subcategory_by_id(db: Session, subcategory_id: int):
    subcategory = db.query(models.SubCategory).filter(models.SubCategory.id == subcategory_id).first()
    if not subcategory:
        raise HTTPException(status_code=404, detail="SubCategory not found")
    return subcategory