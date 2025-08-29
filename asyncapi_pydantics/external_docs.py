"""Tag Object.

This module contains the Tag Object for categorization.
"""

from typing import Optional
from pydantic import BaseModel, Field


class ExternalDocumentation(BaseModel):
    """External Documentation Object.

    Allows referencing an external resource for extended documentation.
    """

    description: Optional[str] = Field(
        None, description="A short description of the target documentation."
    )

    url: str = Field(..., description="The URL for the target documentation.")

    class Config:
        """Pydantic configuration."""

        extra = "allow"
