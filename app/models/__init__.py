"""
SQLAlchemy models initialization module.
"""
from app.core.database import Base

# Import models to register them with SQLAlchemy
from app.models.user import User  # noqa
from app.models.item import Item  # noqa
