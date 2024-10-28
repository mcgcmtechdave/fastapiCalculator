
from judoscale.asgi.middleware import FastAPIRequestQueueTimeMiddleware # Test AutoScale by using JudoScale
from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

app.add_middleware(FastAPIRequestQueueTimeMiddleware)#judo

@app.get("/")
def read_root():
    return {"Hello": "Pew"}

@app.get("/eval")
def calculate(
    Operator: str = Query(..., description="Choose to Calculate type: add |minus | times | devide"),
    firstDigit: float = Query(..., description="First Digit"),
    secondDigit: float = Query(..., description="Second Digit")
):
    if Operator == "add":
        result = firstDigit + secondDigit
    elif Operator == "minus":
        result = firstDigit - secondDigit
    elif Operator == "times":
        result = firstDigit * secondDigit
    elif Operator == "divide":
        if secondDigit == 0:
            return {"error": "! divide secondDigity zero"}
        result = firstDigit / secondDigit
    else:
        return {"error": "Invalid!!! Just type add, minus, times, division"}
    
    return {"Operator": Operator, "a": firstDigit, "secondDigit": secondDigit, "result": result}
    app.add_middleware(FastAPIRequestQueueTimeMiddleware)
#if __name__ == "__main__":
#   uvicorn.run("app:app", host="0.0.0.0", port=10000 , reload=True)
