"""
Core utilities for the application.
"""
import logging
from typing import Any, Dict, List, Optional, Union

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def check_entity_exists(
    db: Session, model: Any, entity_id: int, message: str = "Entity not found"
) -> Any:
    """
    Check if an entity exists in the database.
    
    Args:
        db: Database session
        model: SQLAlchemy model
        entity_id: Entity ID
        message: Error message if entity not found
        
    Returns:
        Entity if found
        
    Raises:
        HTTPException: If entity not found
    """
    entity = db.query(model).filter(model.id == entity_id).first()
    if not entity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message,
        )
    return entity


def filter_none_values(obj: Dict[str, Any]) -> Dict[str, Any]:
    """
    Filter out None values from a dictionary.
    
    Args:
        obj: Dictionary to filter
        
    Returns:
        Filtered dictionary
    """
    return {k: v for k, v in obj.items() if v is not None}


def get_multi(
    db: Session,
    model: Any,
    *,
    skip: int = 0,
    limit: int = 100,
    filters: Optional[Dict[str, Any]] = None,
) -> List[Any]:
    """
    Get multiple entities from the database with pagination and filtering.
    
    Args:
        db: Database session
        model: SQLAlchemy model
        skip: Number of records to skip
        limit: Maximum number of records to return
        filters: Optional dictionary of filters
        
    Returns:
        List of entities
    """
    query = db.query(model)
    
    if filters:
        for field, value in filters.items():
            if value is not None:
                if isinstance(value, list):
                    query = query.filter(getattr(model, field).in_(value))
                else:
                    query = query.filter(getattr(model, field) == value)
    
    return query.offset(skip).limit(limit).all()


def create_entity(db: Session, model: Any, obj_in: Dict[str, Any]) -> Any:
    """
    Create a new entity in the database.
    
    Args:
        db: Database session
        model: SQLAlchemy model
        obj_in: Entity data
        
    Returns:
        Created entity
    """
    db_obj = model(**obj_in)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_entity(
    db: Session, model: Any, entity_id: int, obj_in: Union[Dict[str, Any], Any]
) -> Any:
    """
    Update an entity in the database.
    
    Args:
        db: Database session
        model: SQLAlchemy model
        entity_id: Entity ID
        obj_in: Updated entity data
        
    Returns:
        Updated entity
        
    Raises:
        HTTPException: If entity not found
    """
    db_obj = check_entity_exists(db, model, entity_id)
    
    # Convert Pydantic model to dict if necessary
    update_data = obj_in if isinstance(obj_in, dict) else obj_in.dict(exclude_unset=True)
    
    # Filter out None values
    update_data = filter_none_values(update_data)
    
    # Update attributes
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_entity(db: Session, model: Any, entity_id: int) -> Any:
    """
    Delete an entity from the database.
    
    Args:
        db: Database session
        model: SQLAlchemy model
        entity_id: Entity ID
        
    Returns:
        Deleted entity
        
    Raises:
        HTTPException: If entity not found
    """
    db_obj = check_entity_exists(db, model, entity_id)
    db.delete(db_obj)
    db.commit()
    return db_obj
