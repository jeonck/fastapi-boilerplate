"""
Pydantic schemas for User entities.
"""
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Base User schema with common attributes."""
    
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


class UserCreate(UserBase):
    """User creation schema."""
    
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    """User update schema."""
    
    password: Optional[str] = None


class UserInDBBase(UserBase):
    """Base User schema for database instances."""
    
    id: Optional[int] = None
    
    class Config:
        """Pydantic config."""
        from_attributes = True


class User(UserInDBBase):
    """User schema for API responses."""
    pass


class UserInDB(UserInDBBase):
    """User schema for database with hashed password."""
    
    hashed_password: str
