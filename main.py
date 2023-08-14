from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Gametems, we are a fucking great team!!"}


@app.get("/test")
async def test():
    return {"message": "Hello Abrahan"}
