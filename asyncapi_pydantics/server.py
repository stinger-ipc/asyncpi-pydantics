"""Server Object and related models.

This module contains the Server Object and ServerVariable models.
"""

from typing import Optional, Dict, List, Any
from pydantic import BaseModel, Field

from .tag import Tag
from .external_docs import ExternalDocumentation


class ServerVariable(BaseModel):
    """Server Variable Object.

    An object representing a Server Variable for server URL template substitution.
    """

    enum: Optional[List[str]] = Field(
        None,
        description="An enumeration of string values to be used if the substitution options are from a limited set.",
    )

    default: Optional[str] = Field(
        None, description="The default value to use for substitution."
    )

    description: Optional[str] = Field(
        None, description="An optional description for the server variable."
    )

    examples: Optional[List[str]] = Field(
        None, description="An array of examples of the server variable."
    )

    class Config:
        """Pydantic configuration."""

        extra = "allow"


class Server(BaseModel):
    """Server Object.

    An object representing a message broker, a server or any other kind of computer
    program capable of sending and/or receiving data.
    """

    host: str = Field(..., description="The server host name. It MAY include the port.")

    protocol: str = Field(
        ..., description="The protocol this server supports for connection."
    )

    protocol_version: Optional[str] = Field(
        None,
        alias="protocolVersion",
        description="The version of the protocol used for connection.",
    )

    pathname: Optional[str] = Field(
        None, description="The path to a resource in the host."
    )

    description: Optional[str] = Field(
        None, description="An optional string describing the server."
    )

    title: Optional[str] = Field(
        None, description="A human-friendly title for the server."
    )

    summary: Optional[str] = Field(None, description="A short summary of the server.")

    variables: Optional[Dict[str, ServerVariable]] = Field(
        None, description="A map between a variable name and its value."
    )

    security: Optional[List[Dict[str, Any]]] = Field(
        None,
        description="A declaration of which security schemes can be used with this server.",
    )

    tags: Optional[List[Tag]] = Field(
        None,
        description="A list of tags for logical grouping and categorization of servers.",
    )

    external_docs: Optional[ExternalDocumentation] = Field(
        None,
        alias="externalDocs",
        description="Additional external documentation for this server.",
    )

    bindings: Optional[Dict[str, Any]] = Field(
        None,
        description="A map where the keys describe the name of the protocol and the values describe protocol-specific definitions for the server.",
    )

    class Config:
        """Pydantic configuration."""

        populate_by_name = True
        extra = "allow"
