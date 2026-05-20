from fastapi import FastAPI
from api.routes import employees, departments
import uvicorn

app = FastAPI()
app.include_router(employees.router)
app.include_router(departments.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
