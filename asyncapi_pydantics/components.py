"""Components Object and related models.

This module contains the Components Object for reusable definitions.
"""

from typing import Optional, Dict, Any, Union
from pydantic import BaseModel, Field


class Components(BaseModel):
    """Components Object.

    Holds a set of reusable objects for different aspects of the AsyncAPI specification.
    """

    schemas: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None, description="An object to hold reusable Schema Objects."
    )

    servers: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None, description="An object to hold reusable Server Objects."
    )

    channels: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None, description="An object to hold reusable Channel Objects."
    )

    operations: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None, description="An object to hold reusable Operation Objects."
    )

    messages: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None, description="An object to hold reusable Message Objects."
    )

    security_schemes: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None,
        alias="securitySchemes",
        description="An object to hold reusable Security Scheme Objects.",
    )

    server_variables: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None,
        alias="serverVariables",
        description="An object to hold reusable Server Variable Objects.",
    )

    parameters: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None, description="An object to hold reusable Parameter Objects."
    )

    correlation_ids: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None,
        alias="correlationIds",
        description="An object to hold reusable Correlation ID Objects.",
    )

    replies: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None, description="An object to hold reusable Operation Reply Objects."
    )

    reply_addresses: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None,
        alias="replyAddresses",
        description="An object to hold reusable Operation Reply Address Objects.",
    )

    external_docs: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None,
        alias="externalDocs",
        description="An object to hold reusable External Documentation Objects.",
    )

    tags: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None, description="An object to hold reusable Tag Objects."
    )

    operation_traits: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None,
        alias="operationTraits",
        description="An object to hold reusable Operation Trait Objects.",
    )

    message_traits: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None,
        alias="messageTraits",
        description="An object to hold reusable Message Trait Objects.",
    )

    server_bindings: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None,
        alias="serverBindings",
        description="An object to hold reusable Server Bindings Objects.",
    )

    channel_bindings: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None,
        alias="channelBindings",
        description="An object to hold reusable Channel Bindings Objects.",
    )

    operation_bindings: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None,
        alias="operationBindings",
        description="An object to hold reusable Operation Bindings Objects.",
    )

    message_bindings: Optional[Dict[str, Union[Dict[str, Any], Any]]] = Field(
        None,
        alias="messageBindings",
        description="An object to hold reusable Message Bindings Objects.",
    )

    class Config:
        """Pydantic configuration."""

        populate_by_name = True
        extra = "allow"
