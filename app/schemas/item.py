"""
Pydantic schemas for Item entities.
"""
from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    """Base Item schema with common attributes."""
    
    title: Optional[str] = None
    description: Optional[str] = None


class ItemCreate(ItemBase):
    """Item creation schema."""
    
    title: str


class ItemUpdate(ItemBase):
    """Item update schema."""
    pass


class ItemInDBBase(ItemBase):
    """Base Item schema for database instances."""
    
    id: int
    owner_id: int
    
    class Config:
        """Pydantic config."""
        from_attributes = True


class Item(ItemInDBBase):
    """Item schema for API responses."""
    pass


class ItemInDB(ItemInDBBase):
    """Item schema for database."""
    pass
