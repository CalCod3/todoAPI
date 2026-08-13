from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

tasks = [
    {"id": 1, "title": "Task 1", "done": False},
    {"id": 2, "title": "Task 2", "done": True},
    {"id": 3, "title": "Task 3", "done": False},
]

@app.get("/")
async def read_root():
    return JSONResponse(content={ "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] })

@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "healthy"})

@app.get("/tasks")
async def get_tasks():
    return JSONResponse(content=tasks)

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return JSONResponse(status_code=404, content={"error": "Task not found"})
    return JSONResponse(content=task)

@app.post("/tasks")
async def create_task(task: dict):
    if "title" not in task:
        return JSONResponse(status_code=400, content={"error": "Task title is required"})
    
    new_task = {
        "id": len(tasks) + 1,
        "title": task.get("title", ""),
        "done": task.get("done", False),
    }
    tasks.append(new_task)
    return JSONResponse(status_code=201, content=new_task)

