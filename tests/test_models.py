"""Test the actual Pydantic models work."""

import pytest
from asyncapi_pydantics import AsyncAPI, Info, Contact, License


def test_info_object_creation():
    """Test that we can create an Info object."""
    info = Info(title="Test API", version="1.0.0", description="A test API")
    assert info.title == "Test API"
    assert info.version == "1.0.0"
    assert info.description == "A test API"


def test_info_with_contact_and_license():
    """Test Info object with contact and license."""
    contact = Contact(
        name="API Support",
        email="support@example.com",
        url="https://example.com/support",
    )

    license_obj = License(name="MIT", url="https://opensource.org/licenses/MIT")

    info = Info(title="Test API", version="1.0.0", contact=contact, license=license_obj)

    assert info.contact.name == "API Support"
    assert info.license.name == "MIT"


def test_basic_asyncapi_document():
    """Test creating a basic AsyncAPI document."""
    info = Info(title="Test API", version="1.0.0")

    doc = AsyncAPI(asyncapi="3.0.0", info=info)

    assert doc.asyncapi == "3.0.0"
    assert doc.info.title == "Test API"


def test_asyncapi_document_with_id():
    """Test AsyncAPI document with ID."""
    info = Info(title="Test API", version="1.0.0")

    doc = AsyncAPI(asyncapi="3.0.0", id="urn:example:test:api", info=info)

    assert doc.id == "urn:example:test:api"


def test_asyncapi_version_validation():
    """Test that AsyncAPI version validation works."""
    info = Info(title="Test API", version="1.0.0")

    # Valid version
    doc = AsyncAPI(asyncapi="3.0.0", info=info)
    assert doc.asyncapi == "3.0.0"

    # Valid version with patch
    doc = AsyncAPI(asyncapi="3.0.1", info=info)
    assert doc.asyncapi == "3.0.1"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
