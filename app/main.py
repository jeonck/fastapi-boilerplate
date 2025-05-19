"""
Main application entry point for the FastAPI boilerplate.
"""
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

# Create FastAPI app
app = FastAPI(
    title="FastAPI Boilerplate",
    description="A minimal FastAPI boilerplate with essential features",
    version="0.1.0",
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# Simple API endpoint
@app.get("/api/hello")
async def hello():
    """Simple API endpoint that returns a greeting."""
    return {"message": "Hello World!"}

# Home page route
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Render the home page."""
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "FastAPI Boilerplate"},
    )

# About page route
@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """Render the about page."""
    return templates.TemplateResponse(
        "about.html",
        {"request": request, "title": "About | FastAPI Boilerplate"},
    )

# Favicon route
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    """Serve favicon."""
    favicon_path = Path("app/static/img/favicon.ico")
    return FileResponse(favicon_path)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
