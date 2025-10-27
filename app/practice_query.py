
from sqlalchemy import event, select, func
from sqlalchemy.engine import Engine
from app.database import SessionLocal
from app.models import Category, SubCategory


query_count = 0
     
@event.listens_for(Engine, "before_cursor_execute")
def count_queries(conn, cursor, statement, parameters, context, executemany):
    global query_count
    query_count += 1
    print(f"SQL Hit {query_count}: {statement}")  
 
    
db = SessionLocal()
print(" Connected to DB")


print("\n All Categories:")
print(db.query(Category).all())

print("\n Joined Data:")
stmt = select(SubCategory.name, Category.name.label("category_name")).join(Category)
print(db.execute(stmt).all())

print("\n Count per Category:")
stmt2 = (
    select(Category.name, func.count(SubCategory.id).label("sub_count"))
    .join(SubCategory, isouter=True)
    .group_by(Category.id)
)
print(db.execute(stmt2).all())

print(f"\n Total DB hits: {query_count}")

db.close()
