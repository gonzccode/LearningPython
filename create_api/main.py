from fastapi import FastAPI

app = FastAPI()

# "/docs" => para consultar las peticiones http http://127.0.0.1:8000/docs
"""el uvicorn seria como el nodemon, para que la ejecucion se haga en tiempo real
FAST API ayuda a crear el servidor local asi como node y poder interactuar con este, 
en este caso es el de arriba 
uvircorn main:app --reload"""


@app.get("/transactions")
def get_transactions():
    return {"message": "get all my movements"}


@app.get("/transaction/{id}")
def get_one_transaction(id: int):
    #para estos casos es bueno hacer un try exception
    return {"message": f'get all my movements {id}'}


@app.post("/transaction")
def create_transaction(body: dict):
    print(type(body))
    return {"message": "create transaction successfully", "body": body}


@app.put("/transaction/{id}")
def update_transaction(id):
    return {"message": f'update transaction successfully {id}'}


@app.delete("/transaction/{id}")
def delete_transaction(id):
    return {"message": f'delete transaction successfully {id}'}


"""def read_root():
    return {"Hello": "World"}"""

