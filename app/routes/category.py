from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.database import get_db
from app.schemas import CategoryResponse, CategoryCreate

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@router.get("/", response_model=list[CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@router.get("/categories/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return crud.get_category_by_id(db, category_id)

@router.put("/categories/{category_id}", response_model=CategoryResponse)
def update_category_api(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    updated = crud.update_category(db, category_id, category) 
    if not updated:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated