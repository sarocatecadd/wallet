from fastapi import FastAPI 
from bitcoin import *


app = FastAPI()

class addbitcoin():
    
    public_key="030b25276b83bc5a125cd060c9487db4bab7491534f5146a529afd715385a84829"
    address=pubtoaddr(public_key)
    
    
    

@app.get("/")
def index():
    return "Saroca Tec S.A.S - Generator address bitcoin"

@app.get("/api/address")
def generar_address():
    return {
        "address":addbitcoin.address,
        "public_key":addbitcoin.public_key           
    }

@app.post("/api/address")
def addpublic_key():
    return {"message": f"public_key {addbitcoin.public_key} insert to"}    


@app.put("/api/address")
def updatepublic_key():
    return {"message": f"public_key {addbitcoin.public_key} insert to"}       

