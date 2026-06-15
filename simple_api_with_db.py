from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel, Field, validator

def get_db():
    connection = sqlite3.connect("catalog2.db")
    connection.row_factory = sqlite3.Row
    return connection


app = FastAPI(title="Simple API with SQLite")

class ProductCreate(BaseModel) :
    number_in_box : int = Field(...,gt=0, description="Quantity must be greater than zero.")
    price : float = Field(...,gt=0 , description="Price must be greater than 0")
    total_inventory : int = Field(...,gt=0 , description="Total inventory cannot be negative.")


@app.get("/items")

async def get_all_items():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM catalog")
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


@app.get("/items/{nameItem}")

async def get_one_item(nameItem: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM catalog
                   WHERE name = ?''',(nameItem,))
    row = cursor.fetchone()
    if row is None:
        conn.close()
        return {"message": f"product '{nameItem}' not exist"}
    return dict(row)
    


@app.post("/item/{nameItem}")
async def create_one_item(nameItem:str , item: ProductCreate):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM catalog
                   WHERE name = ?''',(nameItem,))
    existing= cursor.fetchone()
    if existing:
        conn.close()
        return {"message": f"product '{nameItem}' exist"}
    cursor.execute('''
    INSERT INTO catalog (name , price, number_in_box,total_inventory)
            VALUES (?,?,?,?)
    ''',(nameItem , item.price ,item.number_in_box, item.total_inventory) )
    conn.commit()
    conn.close()
    return {"message": f"{nameItem} created"}


@app.put("/items/{nameItem}")
async def update_item(nameItem: str , item: ProductCreate):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM catalog
                   WHERE name = ?''',(nameItem,))
    existing= cursor.fetchone()
    if not existing:
        conn.close()
        return {"message": f"product '{nameItem}' not exist"}
    cursor.execute('''
                   UPDATE catalog
                   SET price = ?,number_in_box = ?,total_inventory = ?
                   WHERE name = ?
                   ''',(item.price ,item.number_in_box , item.total_inventory ,nameItem ) )
    conn.commit()
    conn.close()

    return {"message" : f"{nameItem} updated"}


@app.delete("/item/{nameItem}")
async def delete_product(nameItem: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM catalog
                   WHERE name = ?''',(nameItem,))
    existing= cursor.fetchone()
    if not existing:
        conn.close()
        return {"message": f"product '{nameItem}' not exist"}
    cursor.execute('''
    DELETE FROM catalog 
       WHERE name = ?
    ''',(nameItem,))

    conn.commit()
    conn.close()



    return {"message": f"{nameItem} deleted"}

