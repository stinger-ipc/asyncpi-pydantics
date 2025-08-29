"""Info Object and related models.

This module contains the Info Object and related models like Contact and License.
"""

from typing import Optional, List
from pydantic import BaseModel, Field, HttpUrl, EmailStr

from .tag import Tag
from .external_docs import ExternalDocumentation


class Contact(BaseModel):
    """Contact information for the exposed API."""

    name: Optional[str] = Field(
        None, description="The identifying name of the contact person/organization."
    )

    url: Optional[HttpUrl] = Field(
        None, description="The URL pointing to the contact information."
    )

    email: Optional[EmailStr] = Field(
        None, description="The email address of the contact person/organization."
    )

    class Config:
        """Pydantic configuration."""

        extra = "allow"


class License(BaseModel):
    """License information for the exposed API."""

    name: str = Field(..., description="The license name used for the API.")

    url: Optional[HttpUrl] = Field(
        None, description="A URL to the license used for the API."
    )

    class Config:
        """Pydantic configuration."""

        extra = "allow"


class Info(BaseModel):
    """The object provides metadata about the API."""

    title: str = Field(..., description="The title of the application.")

    version: str = Field(
        ..., description="Provides the version of the application API."
    )

    description: Optional[str] = Field(
        None, description="A short description of the application."
    )

    terms_of_service: Optional[HttpUrl] = Field(
        None,
        alias="termsOfService",
        description="A URL to the Terms of Service for the API.",
    )

    contact: Optional[Contact] = Field(
        None, description="The contact information for the exposed API."
    )

    license: Optional[License] = Field(
        None, description="The license information for the exposed API."
    )

    tags: Optional[List[Tag]] = Field(
        None, description="A list of tags for application API documentation control."
    )

    external_docs: Optional[ExternalDocumentation] = Field(
        None,
        alias="externalDocs",
        description="Additional external documentation of the exposed API.",
    )

    class Config:
        """Pydantic configuration."""

        populate_by_name = True
        extra = "allow"
