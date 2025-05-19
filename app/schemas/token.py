"""
Pydantic schemas for JWT tokens.
"""
from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    """JWT token schema for API responses."""
    
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    """JWT token payload schema."""
    
    sub: Optional[str] = None
