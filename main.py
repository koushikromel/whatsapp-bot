from fastapi import FastAPI, Request
import uvicorn


app = FastAPI()

@app.get("/")
def getData():
    return {"message": "Welcome to Onwords WhatsApp Bot"}






if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=7777, reload=True)