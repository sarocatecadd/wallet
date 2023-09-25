from fastapi import FastAPI 
from bitcoin import *


app = FastAPI()

class addbitcoin():
    
    private_key = sha256('safvdsdat ghbbar ali amirkabir ghooli chaldhooz')
    public_key=privtopub(private_key)
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