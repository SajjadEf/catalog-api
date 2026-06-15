
from fastapi import FastAPI
from pydantic import BaseModel


catalog = {
    "kalaghi": {
        "price": 18000,
        "number_in_box": 350,
        "total_inventory": 35,
    },
    "docheshme": {
        "price": 60000,
        "number_in_box": 43,
        "total_inventory": 100,
    },
    "takcheshme": {
        "price": 40000,
        "number_in_box": 70,
        "total_inventory": 90,
    },
    "sabadi": {
        "price": 25000,
        "number_in_box": 110,
        "total_inventory": 35,
    },
    "topol": {
        "price": 27000,
        "number_in_box": 100,
        "total_inventory": 14,
    }
}

app = FastAPI(title="get catalog")

class ProductCreate(BaseModel) :
    number_in_box : int
    price : float
    total_inventory : int





@app.get("/item")
async def get_catalog(): 
    return catalog

@app.get("/item/{nameItem}")
async def get_one_item(nameItem: str):
    if nameItem not in catalog:
        return {"error" : "This product is not in our catalog" } 
    return  catalog[nameItem]

@app.delete("/item/{nameItem}")
async def delete_product(nameItem: str):
    if nameItem not in catalog:
        return {"error" : "This product is not in our catalog" } 
    del catalog[nameItem]
    return {"message": f"{nameItem} deleted"}
    
@app.post("/item/{nameItem}")
async def post_item(nameItem:str , item: ProductCreate):

    if nameItem in catalog:
        return {"error" : "Already exist"}

    catalog[nameItem] = {
        "price": item.price,
        "number_in_box": item.number_in_box,
        "total_inventory": item.total_inventory,
    }
    return {"message": f"{nameItem} added", "item": catalog[nameItem]}


@app.put("/item/{nameItem}")
async def update_product(nameItem:str , item: ProductCreate):
    if nameItem not in catalog:
        return {"error" : "This product is not in our catalog" } 
    catalog[nameItem] = {
        "price": item.price,
        "number_in_box": item.number_in_box,
        "total_inventory": item.total_inventory,
    }
    return {"message": f"{nameItem} updated ", "item": catalog[nameItem]}