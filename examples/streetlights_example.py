"""Example usage of AsyncAPI Pydantic models.

This example demonstrates how to use the AsyncAPI Pydantic models
to parse and validate AsyncAPI 3.0.0 documents.
"""

import json
from typing import Dict, Any


def create_streetlights_example() -> Dict[str, Any]:
    """Create a complete AsyncAPI 3.0.0 document example for a streetlights API."""

    return {
        "asyncapi": "3.0.0",
        "id": "urn:example:com:smartylighting:streetlights:server",
        "info": {
            "title": "Streetlights Kafka API",
            "version": "1.0.0",
            "description": "The Smartylighting Streetlights API allows you to remotely manage the city lights.",
            "license": {
                "name": "Apache 2.0",
                "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
            },
        },
        "servers": {
            "scram-connections": {
                "host": "test.mykafkacluster.org:18092",
                "protocol": "kafka-secure",
                "description": "Test broker secured with scramSha256",
                "security": [{"sasl-scram": []}],
                "tags": [
                    {
                        "name": "env:test-scram",
                        "description": "This environment is meant for running internal tests through scramSha256",
                    }
                ],
            },
            "mtls-connections": {
                "host": "test.mykafkacluster.org:28092",
                "protocol": "kafka-secure",
                "description": "Test broker secured with X509",
                "security": [{"certs": []}],
                "tags": [
                    {
                        "name": "env:test-mtls",
                        "description": "This environment is meant for running internal tests through mtls",
                    }
                ],
            },
        },
        "defaultContentType": "application/json",
        "channels": {
            "lightingMeasured": {
                "address": "smartylighting.streetlights.1.0.event.{streetlightId}.lighting.measured",
                "messages": {
                    "lightMeasured": {"$ref": "#/components/messages/lightMeasured"}
                },
                "description": "The topic on which measured values may be produced and consumed.",
                "parameters": {
                    "streetlightId": {"$ref": "#/components/parameters/streetlightId"}
                },
            },
            "lightingCommand": {
                "address": "smartylighting.streetlights.1.0.action.{streetlightId}.turn.{direction}",
                "messages": {"turnOnOff": {"$ref": "#/components/messages/turnOnOff"}},
                "description": "The topic on which turn on/off commands may be sent.",
                "parameters": {
                    "streetlightId": {"$ref": "#/components/parameters/streetlightId"},
                    "direction": {"$ref": "#/components/parameters/direction"},
                },
            },
        },
        "operations": {
            "receiveLightMeasurement": {
                "action": "receive",
                "channel": {"$ref": "#/channels/lightingMeasured"},
                "summary": "Inform about environmental lighting conditions of a particular streetlight.",
                "traits": [{"$ref": "#/components/operationTraits/kafka"}],
                "messages": [
                    {"$ref": "#/channels/lightingMeasured/messages/lightMeasured"}
                ],
            },
            "sendLightCommand": {
                "action": "send",
                "channel": {"$ref": "#/channels/lightingCommand"},
                "summary": "Command a particular streetlight to turn the lights on or off.",
                "traits": [{"$ref": "#/components/operationTraits/kafka"}],
                "messages": [{"$ref": "#/channels/lightingCommand/messages/turnOnOff"}],
            },
        },
        "components": {
            "messages": {
                "lightMeasured": {
                    "name": "lightMeasured",
                    "title": "Light measured",
                    "summary": "Inform about environmental lighting conditions of a particular streetlight.",
                    "contentType": "application/json",
                    "traits": [{"$ref": "#/components/messageTraits/commonHeaders"}],
                    "payload": {"$ref": "#/components/schemas/lightMeasuredPayload"},
                },
                "turnOnOff": {
                    "name": "turnOnOff",
                    "title": "Turn on/off",
                    "summary": "Command a particular streetlight to turn the lights on or off.",
                    "traits": [{"$ref": "#/components/messageTraits/commonHeaders"}],
                    "payload": {"$ref": "#/components/schemas/turnOnOffPayload"},
                },
            },
            "schemas": {
                "lightMeasuredPayload": {
                    "type": "object",
                    "properties": {
                        "lumens": {
                            "type": "integer",
                            "minimum": 0,
                            "description": "Light intensity measured in lumens.",
                        },
                        "sentAt": {
                            "type": "string",
                            "format": "date-time",
                            "description": "Date and time when the message was sent.",
                        },
                    },
                },
                "turnOnOffPayload": {
                    "type": "object",
                    "properties": {
                        "command": {
                            "type": "string",
                            "enum": ["on", "off"],
                            "description": "Whether to turn on or off the light.",
                        },
                        "sentAt": {
                            "type": "string",
                            "format": "date-time",
                            "description": "Date and time when the message was sent.",
                        },
                    },
                },
                "sentAt": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Date and time when the message was sent.",
                },
            },
            "securitySchemes": {
                "sasl-scram": {
                    "type": "scramSha256",
                    "description": "Provide your username and password for SASL/SCRAM authentication",
                },
                "certs": {
                    "type": "X509",
                    "description": "Download the certificate files from service provider",
                },
            },
            "parameters": {
                "streetlightId": {"description": "The ID of the streetlight."},
                "direction": {
                    "description": "Direction of the streetlight.",
                    "enum": ["on", "off"],
                },
            },
            "messageTraits": {
                "commonHeaders": {
                    "headers": {
                        "type": "object",
                        "properties": {
                            "my-app-header": {
                                "type": "integer",
                                "minimum": 0,
                                "maximum": 100,
                            }
                        },
                    }
                }
            },
            "operationTraits": {
                "kafka": {"bindings": {"kafka": {"clientId": "my-app-id"}}}
            },
        },
    }


def main():
    """Main example function."""

    # Create example AsyncAPI document
    streetlights_doc = create_streetlights_example()

    # Print the document
    print("AsyncAPI 3.0.0 Streetlights Example:")
    print("=" * 50)
    print(json.dumps(streetlights_doc, indent=2))

    # When pydantic is installed, you could validate like this:
    from asyncapi_pydantics import AsyncAPI

    validated_doc = AsyncAPI(**streetlights_doc)
    print(f"Validated document ID: {validated_doc.id}")
    print(f"API Title: {validated_doc.info.title}")
    print(f"API Version: {validated_doc.info.version}")


if __name__ == "__main__":
    main()
