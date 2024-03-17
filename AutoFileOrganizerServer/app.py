from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def index():
    return {"hello":"World"}

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)