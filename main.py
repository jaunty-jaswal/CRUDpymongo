from fastapi import FastAPI
from routes import route
app = FastAPI()
app.include_router(route.router)
@app.get('/')
def homePage():
    return {"HOMEPAGE":"This is the HOMEPAGE"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(host="127.0.0.1", port=8000,app=app)