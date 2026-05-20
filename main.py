from fastapi import FastAPI
from api.routes import employees, departments, leave_types, leave_allocations
import uvicorn

app = FastAPI()
app.include_router(employees.router)
app.include_router(departments.router)
app.include_router(leave_types.router)
app.include_router(leave_allocations.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
