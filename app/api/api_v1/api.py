"""
API router initialization and version management.
"""
from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, items, users

# Create API router for version 1
api_router = APIRouter()

# Include specific endpoint routers with their prefixes
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(items.router, prefix="/items", tags=["Items"])
