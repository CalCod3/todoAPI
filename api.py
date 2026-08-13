from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def read_root():
    return JSONResponse(content={ "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] })

@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "healthy"})

