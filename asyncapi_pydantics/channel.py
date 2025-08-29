"""Channel Object and related models."""

from typing import Optional, Dict, List, Any, Union
from pydantic import BaseModel, Field

from .tag import Tag
from .external_docs import ExternalDocumentation


class CorrelationId(BaseModel):
    """Correlation ID Object."""

    description: Optional[str] = Field(None, description="Description")
    location: str = Field(..., description="Location")

    class Config:
        extra = "allow"


class MessageExample(BaseModel):
    """Message Example Object."""

    headers: Optional[Dict[str, Any]] = Field(None, description="Headers")
    payload: Optional[Any] = Field(None, description="Payload")
    name: Optional[str] = Field(None, description="Name")
    summary: Optional[str] = Field(None, description="Summary")

    class Config:
        extra = "allow"


class Message(BaseModel):
    """Message Object."""

    headers: Optional[Union[Dict[str, Any], Any]] = Field(None, description="Headers")
    payload: Optional[Union[Dict[str, Any], Any]] = Field(None, description="Payload")
    correlation_id: Optional[CorrelationId] = Field(None, alias="correlationId")
    content_type: Optional[str] = Field(None, alias="contentType")
    name: Optional[str] = Field(None, description="Name")
    title: Optional[str] = Field(None, description="Title")
    summary: Optional[str] = Field(None, description="Summary")
    description: Optional[str] = Field(None, description="Description")
    tags: Optional[List[Tag]] = Field(None, description="Tags")
    external_docs: Optional[ExternalDocumentation] = Field(None, alias="externalDocs")
    bindings: Optional[Dict[str, Any]] = Field(None, description="Bindings")
    examples: Optional[List[MessageExample]] = Field(None, description="Examples")
    traits: Optional[List[Union[Dict[str, Any], Any]]] = Field(
        None, description="Traits"
    )

    class Config:
        populate_by_name = True
        extra = "allow"


class Parameter(BaseModel):
    """Parameter Object."""

    enum: Optional[List[str]] = Field(None, description="Enum")
    default: Optional[str] = Field(None, description="Default")
    description: Optional[str] = Field(None, description="Description")
    examples: Optional[List[str]] = Field(None, description="Examples")
    location: Optional[str] = Field(None, description="Location")

    class Config:
        extra = "allow"


class Channel(BaseModel):
    """Channel Object."""

    address: Optional[str] = Field(None, description="Address")
    messages: Optional[Dict[str, Union[Message, Any]]] = Field(
        None, description="Messages"
    )
    title: Optional[str] = Field(None, description="Title")
    summary: Optional[str] = Field(None, description="Summary")
    description: Optional[str] = Field(None, description="Description")
    servers: Optional[List[Union[Dict[str, str], Any]]] = Field(
        None, description="Servers"
    )
    parameters: Optional[Dict[str, Parameter]] = Field(None, description="Parameters")
    tags: Optional[List[Tag]] = Field(None, description="Tags")
    external_docs: Optional[ExternalDocumentation] = Field(None, alias="externalDocs")
    bindings: Optional[Dict[str, Any]] = Field(None, description="Bindings")

    class Config:
        populate_by_name = True
        extra = "allow"
