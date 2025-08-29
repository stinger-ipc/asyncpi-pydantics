"""Security Scheme Object and related models.

This module contains security-related models.
"""

from typing import Optional, Dict, List, Literal, Any
from pydantic import BaseModel, Field, HttpUrl


class OAuthFlow(BaseModel):
    """OAuth Flow Object.

    Configuration details for a supported OAuth Flow.
    """

    authorization_url: Optional[HttpUrl] = Field(
        None,
        alias="authorizationUrl",
        description="The authorization URL to be used for this flow.",
    )

    token_url: Optional[HttpUrl] = Field(
        None, alias="tokenUrl", description="The token URL to be used for this flow."
    )

    refresh_url: Optional[HttpUrl] = Field(
        None,
        alias="refreshUrl",
        description="The URL to be used for obtaining refresh tokens.",
    )

    available_scopes: Dict[str, str] = Field(
        ...,
        alias="availableScopes",
        description="The available scopes for the OAuth2 security scheme.",
    )

    class Config:
        """Pydantic configuration."""

        populate_by_name = True
        extra = "allow"


class OAuthFlows(BaseModel):
    """OAuth Flows Object.

    Allows configuration of the supported OAuth Flows.
    """

    implicit: Optional[OAuthFlow] = Field(
        None, description="Configuration for the OAuth Implicit flow."
    )

    password: Optional[OAuthFlow] = Field(
        None,
        description="Configuration for the OAuth Resource Owner Protected Credentials flow.",
    )

    client_credentials: Optional[OAuthFlow] = Field(
        None,
        alias="clientCredentials",
        description="Configuration for the OAuth Client Credentials flow.",
    )

    authorization_code: Optional[OAuthFlow] = Field(
        None,
        alias="authorizationCode",
        description="Configuration for the OAuth Authorization Code flow.",
    )

    class Config:
        """Pydantic configuration."""

        populate_by_name = True
        extra = "allow"


class SecurityScheme(BaseModel):
    """Security Scheme Object.

    Defines a security scheme that can be used by the operations.
    """

    type: Literal[
        "userPassword",
        "apiKey",
        "X509",
        "symmetricEncryption",
        "asymmetricEncryption",
        "httpApiKey",
        "http",
        "oauth2",
        "openIdConnect",
        "plain",
        "scramSha256",
        "scramSha512",
        "gssapi",
    ] = Field(..., description="The type of the security scheme.")

    description: Optional[str] = Field(
        None, description="A short description for security scheme."
    )

    name: Optional[str] = Field(
        None,
        description="The name of the header, query or cookie parameter to be used.",
    )

    in_: Optional[Literal["user", "password", "query", "header", "cookie"]] = Field(
        None, alias="in", description="The location of the API key."
    )

    scheme: Optional[str] = Field(
        None,
        description="The name of the HTTP Authorization scheme to be used in the Authorization header.",
    )

    bearer_format: Optional[str] = Field(
        None,
        alias="bearerFormat",
        description="A hint to the client to identify how the bearer token is formatted.",
    )

    flows: Optional[OAuthFlows] = Field(
        None,
        description="An object containing configuration information for the flow types supported.",
    )

    open_id_connect_url: Optional[HttpUrl] = Field(
        None,
        alias="openIdConnectUrl",
        description="OpenId Connect URL to discover OAuth2 configuration values.",
    )

    scopes: Optional[List[str]] = Field(
        None, description="List of the needed scope names."
    )

    class Config:
        """Pydantic configuration."""

        populate_by_name = True
        extra = "allow"
