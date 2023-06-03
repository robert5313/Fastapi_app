from fastapi import FastAPI
app = FastAPI()

@app.get("/users")
async def read_users():
    return ["John", "Doe"], ["Bean", "Sean"], ["Dane", "Doe"], ["Bean", "Sean"], ["Dan", "Joel"]

@app.get("/users")
async def read_users2():
    return ["Bean", "Sean"]

#The first one will always be used since the path matches first.