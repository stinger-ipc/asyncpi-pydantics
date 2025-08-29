"""Operation Object and related models.

This module contains the Operation Object and related models.
"""

from typing import Optional, List, Dict, Union, Any, Literal
from pydantic import BaseModel, Field

from .tag import Tag
from .external_docs import ExternalDocumentation


class OperationReplyAddress(BaseModel):
    """Operation Reply Address Object.

    An object that specifies where an operation has to send the reply.
    """

    description: Optional[str] = Field(
        None, description="An optional description of the address."
    )

    location: str = Field(
        ...,
        description="A runtime expression that specifies the location of the reply address.",
    )

    class Config:
        """Pydantic configuration."""

        extra = "allow"


class OperationReply(BaseModel):
    """Operation Reply Object.

    Describes the reply part that MAY be applied to an Operation Object.
    """

    address: Optional[OperationReplyAddress] = Field(
        None,
        description="Definition of the address that implementations MUST use for the reply.",
    )

    channel: Optional[Union[Dict[str, str], Any]] = Field(
        None,
        description="A $ref pointer to the definition of the channel in which this operation is performed.",
    )

    messages: Optional[List[Union[Dict[str, str], Any]]] = Field(
        None,
        description="A list of $ref pointers pointing to the supported Message Objects that can be processed by this operation as reply.",
    )

    class Config:
        """Pydantic configuration."""

        extra = "allow"


class OperationTrait(BaseModel):
    """Operation Trait Object.

    Describes a trait that MAY be applied to an Operation Object.
    """

    title: Optional[str] = Field(
        None, description="A human-friendly title for the operation."
    )

    summary: Optional[str] = Field(
        None, description="A short summary of what the operation is about."
    )

    description: Optional[str] = Field(
        None, description="A verbose explanation of the operation."
    )

    security: Optional[List[Dict[str, Any]]] = Field(
        None,
        description="A declaration of which security schemes are associated with this operation.",
    )

    tags: Optional[List[Tag]] = Field(
        None,
        description="A list of tags for logical grouping and categorization of operations.",
    )

    external_docs: Optional[ExternalDocumentation] = Field(
        None,
        alias="externalDocs",
        description="Additional external documentation for this operation.",
    )

    bindings: Optional[Dict[str, Any]] = Field(
        None,
        description="A map where the keys describe the name of the protocol and the values describe protocol-specific definitions for the operation.",
    )

    class Config:
        """Pydantic configuration."""

        populate_by_name = True
        extra = "allow"


class Operation(BaseModel):
    """Operation Object.

    Describes a specific operation.
    """

    action: Literal["send", "receive"] = Field(
        ...,
        description="Use send when it's expected that the application will send a message to the given channel, and receive when the application should expect receiving messages from the given channel.",
    )

    channel: Union[Dict[str, str], Any] = Field(
        ...,
        description="A $ref pointer to the definition of the channel in which this operation is performed.",
    )

    title: Optional[str] = Field(
        None, description="A human-friendly title for the operation."
    )

    summary: Optional[str] = Field(
        None, description="A short summary of what the operation is about."
    )

    description: Optional[str] = Field(
        None, description="A verbose explanation of the operation."
    )

    security: Optional[List[Dict[str, Any]]] = Field(
        None,
        description="A declaration of which security schemes are associated with this operation.",
    )

    tags: Optional[List[Tag]] = Field(
        None,
        description="A list of tags for logical grouping and categorization of operations.",
    )

    external_docs: Optional[ExternalDocumentation] = Field(
        None,
        alias="externalDocs",
        description="Additional external documentation for this operation.",
    )

    bindings: Optional[Dict[str, Any]] = Field(
        None,
        description="A map where the keys describe the name of the protocol and the values describe protocol-specific definitions for the operation.",
    )

    traits: Optional[List[Union[OperationTrait, Dict[str, str], Any]]] = Field(
        None, description="A list of traits to apply to the operation object."
    )

    messages: Optional[List[Union[Dict[str, str], Any]]] = Field(
        None,
        description="A list of $ref pointers pointing to the supported Message Objects that can be processed by this operation.",
    )

    reply: Optional[OperationReply] = Field(
        None, description="The definition of the reply in a request-reply operation."
    )

    class Config:
        """Pydantic configuration."""

        populate_by_name = True
        extra = "allow"
