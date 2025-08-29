"""AsyncAPI Document Object.

This module contains the root AsyncAPI document object and related models.
"""

from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

from .info import Info
from .server import Server
from .channel import Channel
from .operation import Operation
from .components import Components


class AsyncAPI(BaseModel):
    """AsyncAPI Document Object.

    This is the root document object for the API specification.
    It combines resource listing and API declaration together into one document.
    """

    asyncapi: str = Field(
        ...,
        description="Specifies the AsyncAPI Specification version being used.",
        pattern=r"^3\.0\.\d+$",
    )

    id: Optional[str] = Field(
        None,
        description="Identifier of the application the AsyncAPI document is defining.",
    )

    info: Info = Field(..., description="Provides metadata about the API.")

    servers: Optional[Dict[str, Server]] = Field(
        None, description="Provides connection details of servers."
    )

    default_content_type: Optional[str] = Field(
        None,
        alias="defaultContentType",
        description="Default content type to use when encoding/decoding a message's payload.",
    )

    channels: Optional[Dict[str, Channel]] = Field(
        None, description="The channels used by this application."
    )

    operations: Optional[Dict[str, Operation]] = Field(
        None, description="The operations this application MUST implement."
    )

    components: Optional[Components] = Field(
        None,
        description="An element to hold various reusable objects for the specification.",
    )

    class Config:
        """Pydantic configuration."""

        populate_by_name = True
        extra = "allow"  # Allow specification extensions
