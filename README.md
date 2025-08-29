# AsyncAPI Pydantic Models

A Python library providing Pydantic models for AsyncAPI 3.0.0 specification documents. This library allows you to parse, validate, and work with AsyncAPI documents in a type-safe manner using Python.

## Features

- **Complete AsyncAPI 3.0.0 Support**: Models for all AsyncAPI 3.0.0 specification objects
- **Type Safety**: Full type hints and validation using Pydantic v2
- **JSON Schema Validation**: Built-in validation for AsyncAPI documents
- **Easy to Use**: Simple API for parsing and creating AsyncAPI documents
- **Extensible**: Support for specification extensions (x-* fields)

## Installation

This project uses `uv` for dependency management. To install:

```bash
# Clone the repository
git clone <repository-url>
cd asyncapi-pydantics

# Install with uv
uv pip install -e .

# Or install from PyPI (when published)
uv pip install asyncapi-pydantics
```

## Quick Start

```python
from asyncapi_pydantics import AsyncAPI

# Parse an AsyncAPI document
asyncapi_doc = {
    "asyncapi": "3.0.0",
    "info": {
        "title": "My API",
        "version": "1.0.0"
    },
    "channels": {
        "user-events": {
            "address": "user/events",
            "messages": {
                "userSignedUp": {
                    "payload": {
                        "type": "object",
                        "properties": {
                            "userId": {"type": "string"},
                            "email": {"type": "string", "format": "email"}
                        }
                    }
                }
            }
        }
    },
    "operations": {
        "receiveUserEvents": {
            "action": "receive",
            "channel": {"$ref": "#/channels/user-events"}
        }
    }
}

# Validate and parse the document
api = AsyncAPI(**asyncapi_doc)

# Access the parsed data with full type safety
print(f"API Title: {api.info.title}")
print(f"API Version: {api.info.version}")
print(f"Channels: {list(api.channels.keys()) if api.channels else []}")
```

## Supported AsyncAPI Objects

This library provides Pydantic models for all AsyncAPI 3.0.0 objects:

### Core Objects
- `AsyncAPI` - Root AsyncAPI document
- `Info` - API metadata
- `Contact` - Contact information
- `License` - License information
- `Server` - Server connection details
- `ServerVariable` - Server URL variables

### Channel & Message Objects
- `Channel` - Communication channel
- `Message` - Message definition
- `Parameter` - Channel parameters
- `CorrelationId` - Message correlation

### Operation Objects
- `Operation` - API operation
- `OperationTrait` - Reusable operation properties
- `OperationReply` - Operation reply definition
- `OperationReplyAddress` - Reply address specification

### Schema Objects
- `Schema` - JSON Schema with AsyncAPI extensions
- `MultiFormatSchema` - Multi-format schema support

### Security Objects
- `SecurityScheme` - Security scheme definition
- `OAuthFlows` - OAuth flow configurations
- `OAuthFlow` - Individual OAuth flow

### Utility Objects
- `Components` - Reusable components
- `Tag` - Categorization tags
- `ExternalDocumentation` - External documentation links

## Examples

### Streetlights API Example

```python
from asyncapi_pydantics import AsyncAPI

# See examples/streetlights_example.py for a complete example
streetlights_api = AsyncAPI(**{
    "asyncapi": "3.0.0",
    "info": {
        "title": "Streetlights API",
        "version": "1.0.0",
        "description": "API for managing smart streetlights"
    },
    "servers": {
        "mqtt-broker": {
            "host": "mqtt.streetlights.com",
            "protocol": "mqtt"
        }
    },
    "channels": {
        "lighting-measured": {
            "address": "streetlights/{streetlightId}/lighting/measured",
            "messages": {
                "lightMeasured": {
                    "payload": {
                        "type": "object",
                        "properties": {
                            "lumens": {"type": "integer", "minimum": 0},
                            "timestamp": {"type": "string", "format": "date-time"}
                        }
                    }
                }
            }
        }
    }
})

print(f"API: {streetlights_api.info.title}")
print(f"Server: {list(streetlights_api.servers.keys())[0]}")
```

### Kafka API Example

```python
from asyncapi_pydantics import AsyncAPI

kafka_api = AsyncAPI(**{
    "asyncapi": "3.0.0",
    "info": {
        "title": "User Events API",
        "version": "2.0.0"
    },
    "servers": {
        "kafka-cluster": {
            "host": "kafka.example.com:9092",
            "protocol": "kafka",
            "security": [{"sasl": []}]
        }
    },
    "channels": {
        "user-events": {
            "address": "user.events.v1",
            "messages": {
                "userCreated": {
                    "contentType": "application/json",
                    "payload": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "name": {"type": "string"},
                            "email": {"type": "string", "format": "email"},
                            "createdAt": {"type": "string", "format": "date-time"}
                        },
                        "required": ["id", "name", "email", "createdAt"]
                    }
                }
            }
        }
    },
    "operations": {
        "publishUserCreated": {
            "action": "send",
            "channel": {"$ref": "#/channels/user-events"},
            "messages": [{"$ref": "#/channels/user-events/messages/userCreated"}]
        }
    }
})
```

## Development

This project uses `uv` for dependency management and development.

### Setup Development Environment

```bash
# Clone the repository
git clone <repository-url>
cd asyncapi-pydantics

# Install dependencies
uv pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=asyncapi_pydantics

# Run type checking
uv run mypy asyncapi_pydantics
```

### Code Formatting

```bash
# Format code
uv run black asyncapi_pydantics tests examples

# Sort imports
uv run isort asyncapi_pydantics tests examples

# Lint code
uv run ruff check asyncapi_pydantics tests examples
```

## Project Structure

```
asyncapi-pydantics/
├── asyncapi_pydantics/          # Main package
│   ├── __init__.py             # Package exports
│   ├── asyncapi.py             # Root AsyncAPI model
│   ├── info.py                 # Info, Contact, License models
│   ├── server.py               # Server models
│   ├── channel.py              # Channel and Message models
│   ├── operation.py            # Operation models
│   ├── schema.py               # Schema models
│   ├── security.py             # Security models
│   ├── components.py           # Components model
│   ├── tag.py                  # Tag model
│   └── external_docs.py        # External documentation model
├── examples/                    # Usage examples
│   └── streetlights_example.py # Complete example
├── tests/                       # Test suite
│   └── test_examples.py        # Example tests
├── pyproject.toml              # Project configuration
└── README.md                   # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Related Projects

- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/v3.0.0) - Official AsyncAPI specification
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation library used by this project
- [AsyncAPI Tools](https://www.asyncapi.com/tools) - Other AsyncAPI tools and libraries

## Changelog

### 0.1.0
- Initial release
- Complete AsyncAPI 3.0.0 specification support
- All core objects implemented
- Basic validation and parsing
- Example usage and documentation
