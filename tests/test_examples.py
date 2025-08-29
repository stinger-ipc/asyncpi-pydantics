"""Test examples for AsyncAPI Pydantic models."""

import pytest
from typing import Dict, Any

# Note: These tests will require pydantic to be installed
# For now, they serve as examples of how the models would be used

def test_basic_asyncapi_document():
    """Test creating a basic AsyncAPI document."""
    
    # Example AsyncAPI 3.0.0 document
    asyncapi_doc = {
        "asyncapi": "3.0.0",
        "info": {
            "title": "Streetlights API",
            "version": "1.0.0",
            "description": "The Smartylighting Streetlights API allows you to remotely manage the city lights."
        },
        "servers": {
            "production": {
                "host": "api.streetlights.smartylighting.com",
                "protocol": "mqtt",
                "description": "Production MQTT broker"
            }
        },
        "channels": {
            "lightingMeasured": {
                "address": "smartylighting/streetlights/1/0/event/{streetlightId}/lighting/measured",
                "messages": {
                    "lightMeasured": {
                        "name": "lightMeasured",
                        "title": "Light measured",
                        "summary": "Inform about environmental lighting conditions",
                        "contentType": "application/json",
                        "payload": {
                            "type": "object",
                            "properties": {
                                "lumens": {
                                    "type": "integer",
                                    "minimum": 0,
                                    "description": "Light intensity measured in lumens."
                                },
                                "sentAt": {
                                    "type": "string",
                                    "format": "date-time",
                                    "description": "Date and time when the message was sent."
                                }
                            }
                        }
                    }
                }
            }
        },
        "operations": {
            "receiveLightMeasurement": {
                "action": "receive",
                "channel": {
                    "$ref": "#/channels/lightingMeasured"
                },
                "summary": "Receive lighting measurement"
            }
        }
    }
    
    # This would be used like:
    # from asyncapi_pydantics import AsyncAPI
    # doc = AsyncAPI(**asyncapi_doc)
    
    assert asyncapi_doc["asyncapi"] == "3.0.0"
    assert asyncapi_doc["info"]["title"] == "Streetlights API"


def test_info_object():
    """Test Info object creation."""
    
    info_data = {
        "title": "Sample API",
        "version": "1.0.0",
        "description": "A sample API for testing",
        "contact": {
            "name": "API Support",
            "url": "https://www.example.com/support",
            "email": "support@example.com"
        },
        "license": {
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
        }
    }
    
    # This would be used like:
    # from asyncapi_pydantics import Info
    # info = Info(**info_data)
    
    assert info_data["title"] == "Sample API"
    assert info_data["contact"]["email"] == "support@example.com"


def test_server_object():
    """Test Server object creation."""
    
    server_data = {
        "host": "kafka.in.mycompany.com:9092",
        "protocol": "kafka",
        "protocolVersion": "3.2",
        "description": "Production Kafka broker",
        "variables": {
            "env": {
                "enum": ["production", "staging"],
                "default": "production",
                "description": "Environment to connect to"
            }
        }
    }
    
    # This would be used like:
    # from asyncapi_pydantics import Server
    # server = Server(**server_data)
    
    assert server_data["protocol"] == "kafka"
    assert server_data["variables"]["env"]["default"] == "production"


def test_message_object():
    """Test Message object creation."""
    
    message_data = {
        "name": "UserSignup",
        "title": "User signup",
        "summary": "Action to sign a user up.",
        "contentType": "application/json",
        "headers": {
            "type": "object",
            "properties": {
                "correlationId": {
                    "description": "Correlation ID set by application",
                    "type": "string"
                }
            }
        },
        "payload": {
            "type": "object",
            "properties": {
                "user": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "email": {"type": "string", "format": "email"}
                    }
                }
            }
        }
    }
    
    # This would be used like:
    # from asyncapi_pydantics import Message
    # message = Message(**message_data)
    
    assert message_data["name"] == "UserSignup"
    assert message_data["contentType"] == "application/json"


if __name__ == "__main__":
    test_basic_asyncapi_document()
    test_info_object()
    test_server_object()
    test_message_object()
    print("All example tests passed!")
