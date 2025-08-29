"""Schema Object and related models.

This module contains the Schema Object for data validation.
"""

from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field

from .external_docs import ExternalDocumentation


class MultiFormatSchema(BaseModel):
    """Multi Format Schema Object.

    The Multi Format Schema Object represents a schema definition.
    """

    schema_format: Optional[str] = Field(
        None,
        alias="schemaFormat",
        description="A string containing the name of the schema format that is used to define the information.",
    )

    schema: Any = Field(..., description="Definition of the message payload.")

    class Config:
        """Pydantic configuration."""

        populate_by_name = True
        extra = "allow"


class Schema(BaseModel):
    """Schema Object.

    The Schema Object allows the definition of input and output data types.
    This object is a superset of the JSON Schema Specification Draft 07.
    """

    # JSON Schema Core properties
    title: Optional[str] = Field(None, description="The title of the schema")
    type: Optional[Union[str, List[str]]] = Field(
        None, description="The type of the schema"
    )
    required: Optional[List[str]] = Field(None, description="Required properties")
    multiple_of: Optional[float] = Field(
        None, alias="multipleOf", description="Value must be a multiple of this"
    )
    maximum: Optional[float] = Field(None, description="Maximum value")
    exclusive_maximum: Optional[float] = Field(
        None, alias="exclusiveMaximum", description="Exclusive maximum value"
    )
    minimum: Optional[float] = Field(None, description="Minimum value")
    exclusive_minimum: Optional[float] = Field(
        None, alias="exclusiveMinimum", description="Exclusive minimum value"
    )
    max_length: Optional[int] = Field(
        None, alias="maxLength", description="Maximum string length", ge=0
    )
    min_length: Optional[int] = Field(
        None, alias="minLength", description="Minimum string length", ge=0
    )
    pattern: Optional[str] = Field(None, description="Regular expression pattern")
    max_items: Optional[int] = Field(
        None, alias="maxItems", description="Maximum array length", ge=0
    )
    min_items: Optional[int] = Field(
        None, alias="minItems", description="Minimum array length", ge=0
    )
    unique_items: Optional[bool] = Field(
        None, alias="uniqueItems", description="Array items must be unique"
    )
    max_properties: Optional[int] = Field(
        None, alias="maxProperties", description="Maximum object properties", ge=0
    )
    min_properties: Optional[int] = Field(
        None, alias="minProperties", description="Minimum object properties", ge=0
    )
    enum: Optional[List[Any]] = Field(None, description="Enumeration of valid values")
    const: Optional[Any] = Field(None, description="Constant value")

    # AsyncAPI specific properties
    description: Optional[str] = Field(None, description="Description of the schema")
    format: Optional[str] = Field(None, description="Format of the schema")
    default: Optional[Any] = Field(None, description="Default value")
    examples: Optional[List[Any]] = Field(None, description="Example values")

    # Object properties
    properties: Optional[Dict[str, Union["Schema", Dict[str, Any]]]] = Field(
        None, description="Object properties"
    )
    pattern_properties: Optional[Dict[str, Union["Schema", Dict[str, Any]]]] = Field(
        None, alias="patternProperties", description="Pattern properties"
    )
    additional_properties: Optional[Union[bool, "Schema", Dict[str, Any]]] = Field(
        None, alias="additionalProperties", description="Additional properties"
    )
    property_names: Optional[Union["Schema", Dict[str, Any]]] = Field(
        None, alias="propertyNames", description="Property name schema"
    )

    # Array properties
    items: Optional[Union["Schema", List["Schema"], Dict[str, Any]]] = Field(
        None, description="Array item schema"
    )
    additional_items: Optional[Union[bool, "Schema", Dict[str, Any]]] = Field(
        None, alias="additionalItems", description="Additional array items"
    )
    contains: Optional[Union["Schema", Dict[str, Any]]] = Field(
        None, description="Array contains schema"
    )

    # Composition
    all_of: Optional[List[Union["Schema", Dict[str, Any]]]] = Field(
        None, alias="allOf", description="All of schemas"
    )
    any_of: Optional[List[Union["Schema", Dict[str, Any]]]] = Field(
        None, alias="anyOf", description="Any of schemas"
    )
    one_of: Optional[List[Union["Schema", Dict[str, Any]]]] = Field(
        None, alias="oneOf", description="One of schemas"
    )
    not_schema: Optional[Union["Schema", Dict[str, Any]]] = Field(
        None, alias="not", description="Not schema"
    )

    # Conditional
    if_schema: Optional[Union["Schema", Dict[str, Any]]] = Field(
        None, alias="if", description="If schema"
    )
    then_schema: Optional[Union["Schema", Dict[str, Any]]] = Field(
        None, alias="then", description="Then schema"
    )
    else_schema: Optional[Union["Schema", Dict[str, Any]]] = Field(
        None, alias="else", description="Else schema"
    )

    # AsyncAPI extensions
    discriminator: Optional[str] = Field(
        None, description="Discriminator property name"
    )
    external_docs: Optional[ExternalDocumentation] = Field(
        None, alias="externalDocs", description="External documentation"
    )
    deprecated: Optional[bool] = Field(
        None, description="Whether the schema is deprecated"
    )

    # Meta properties
    read_only: Optional[bool] = Field(
        None, alias="readOnly", description="Read only property"
    )
    write_only: Optional[bool] = Field(
        None, alias="writeOnly", description="Write only property"
    )

    class Config:
        """Pydantic configuration."""

        populate_by_name = True
        extra = "allow"


# Update forward references
Schema.model_rebuild()
