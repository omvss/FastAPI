from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.database import get_db
from app.schemas import SubCategoryCreate, SubCategoryResponse

router = APIRouter(prefix="/subcategories", tags=["SubCategories"])

@router.post("/", response_model=SubCategoryResponse)
def create_subcategory(subcategory: SubCategoryCreate, db: Session = Depends(get_db)):
    return crud.create_subcategory(db, subcategory)

@router.get("/", response_model=list[SubCategoryResponse])
def list_subcategories(db: Session = Depends(get_db)):
    return crud.get_subcategories(db)

@router.get("/subcategories/{subcategory_id}", response_model=SubCategoryResponse)
def get_subcategory(subcategory_id: int, db: Session = Depends(get_db)):
    return crud.get_subcategory_by_id(db, subcategory_id)


@router.get("/with-category", response_model=list[SubCategoryResponse])
def get_subcategories_with_category_api(db: Session = Depends(get_db)):
    return crud.get_subcategories_with_category(db)


@router.put("/subcategories/{subcategory_id}", response_model=SubCategoryResponse)
def update_subcategory_api(subcategory_id: int, subcategory:SubCategoryCreate, db: Session = Depends(get_db)):
    updated = crud.update_subcategory(db, subcategory_id, subcategory)
    if not updated:
        raise HTTPException(status_code=404, detail="Subcategory not found")
    return updated

@router.get("/subcategories-with-category")
def get_joined(db: Session = Depends(get_db)):
    return crud.get_subcategories_with_category(db)