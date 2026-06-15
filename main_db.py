from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, Depends

# اتصال به دیتابیس (فایل local.db ساخته می‌شود)
SQLALCHEMY_DATABASE_URL = "sqlite:///./catalog.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# تعریف مدل دیتابیس (همان ساختار جدول)
class CatalogDB(Base):
    __tablename__ = "catalog"
    
    name = Column(String, primary_key=True, index=True)
    price = Column(Float)
    number_in_box = Column(Integer)
    total_inventory = Column(Integer)

# ساخت جدول در دیتابیس
Base.metadata.create_all(bind=engine)

# مدل Pydantic برای ورودی API
class ProductCreate(BaseModel):
    number_in_box: int
    price: float
    total_inventory: int

# مدل Pydantic برای خروجی (با name)
class ProductOut(ProductCreate):
    name: str

app = FastAPI(title="Catalog API with Database")

# وابستگی برای گرفتن session دیتابیس
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------- API ها -------------------

@app.get("/item", response_model=list[ProductOut])
async def get_all_items(db: SessionLocal = Depends(get_db)):
    items = db.query(CatalogDB).all()
    return items

@app.get("/item/{nameItem}", response_model=ProductOut)
async def get_one_item(nameItem: str, db: SessionLocal = Depends(get_db)):
    item = db.query(CatalogDB).filter(CatalogDB.name == nameItem).first()
    if not item:
        return {"error": "This product is not in our catalog"}
    return item

@app.post("/item/{nameItem}")
async def create_item(nameItem: str, item: ProductCreate, db: SessionLocal = Depends(get_db)):
    existing = db.query(CatalogDB).filter(CatalogDB.name == nameItem).first()
    if existing:
        return {"error": "Already exist"}
    
    new_item = CatalogDB(
        name=nameItem,
        price=item.price,
        number_in_box=item.number_in_box,
        total_inventory=item.total_inventory
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"message": f"{nameItem} added", "item": new_item}

@app.put("/item/{nameItem}")
async def update_item(nameItem: str, item: ProductCreate, db: SessionLocal = Depends(get_db)):
    existing = db.query(CatalogDB).filter(CatalogDB.name == nameItem).first()
    if not existing:
        return {"error": "This product is not in our catalog"}
    
    existing.price = item.price
    existing.number_in_box = item.number_in_box
    existing.total_inventory = item.total_inventory
    db.commit()
    db.refresh(existing)
    return {"message": f"{nameItem} updated", "item": existing}

@app.delete("/item/{nameItem}")
async def delete_item(nameItem: str, db: SessionLocal = Depends(get_db)):
    existing = db.query(CatalogDB).filter(CatalogDB.name == nameItem).first()
    if not existing:
        return {"error": "This product is not in our catalog"}
    
    db.delete(existing)
    db.commit()
    return {"message": f"{nameItem} deleted"}