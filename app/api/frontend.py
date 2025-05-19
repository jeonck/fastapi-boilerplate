"""
Frontend routes for web interface using Jinja2 templates.
"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.core.config import settings

# Create router for frontend
frontend_router = APIRouter(include_in_schema=False)

# Initialize Jinja2 templates
templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)


@frontend_router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Render the home page."""
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": settings.PROJECT_NAME},
    )


@frontend_router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """Render the about page."""
    return templates.TemplateResponse(
        "about.html",
        {"request": request, "title": f"About | {settings.PROJECT_NAME}"},
    )
