from fastapi import FastAPI 
from bitcoin import *


app = FastAPI()

class addbitcoin():
    
    public_key="030b25276b83bc5a125cd060c9487db4bab7491534f5146a529afd715385a84829"
    address=pubtoaddr(public_key)

    public_key1 = "030b25276b83bc5a125cd060c9487db4bab7491534f5146a529afd715385a84829"
    address1 = pubtoaddr(public_key1)

    multi_sig = mk_multisig_script(public_key, public_key1, 1, 2)
    multi_sig_addr = scriptaddr(multi_sig)

   


@app.get("/")
def index():
    return "Saroca Tec S.A.S - Generator address bitcoin"

@app.get("/api/address")
def generar_address():
    return {
        "public_key":addbitcoin.public_key,
        "address":addbitcoin.address,
        "address1" : addbitcoin.multi_sig_addr
        
        
    }

@app.post("/api/address")
def addpublic_key():
    return {"message": f"public_key {addbitcoin.public_key} insert to"}    


@app.put("/api/address")
def updatepublic_key():
    return {"message": f"public_key {addbitcoin.public_key} insert to"}       