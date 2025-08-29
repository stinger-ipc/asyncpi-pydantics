"""Tag Object.

This module contains the Tag Object for categorization.
"""

from typing import Optional
from pydantic import BaseModel, Field

from .external_docs import ExternalDocumentation


class Tag(BaseModel):
    """Tag Object.

    Allows adding meta data to a single tag.
    """

    name: str = Field(..., description="The name of the tag.")

    description: Optional[str] = Field(
        None, description="A short description for the tag."
    )

    external_docs: Optional[ExternalDocumentation] = Field(
        None,
        alias="externalDocs",
        description="Additional external documentation for this tag.",
    )

    class Config:
        """Pydantic configuration."""

        populate_by_name = True
        extra = "allow"
