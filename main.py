from fastapi import FastAPI

app = FastAPI()

@app.get("/calculate")
async def calculate(operation: str, num1: float, num2: float):
    if operation == "+":
        return {"result": num1 + num2}
    elif operation == "-":
        return {"result": num1 - num2}
    elif operation == "*":
        return {"result": num1 * num2}
    elif operation == "/":
        return {"result": num1 / num2 if num2 != 0 else "Cannot divide by zero"}
    else:
        return {"error": "Invalid operation"}