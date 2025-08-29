"""Simple validation example using the AsyncAPI Pydantic models.

This example demonstrates basic validation functionality.
"""

import sys
import os

# Add the package to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

try:
    from asyncapi_pydantics import AsyncAPI, Info

    def test_simple_validation():
        """Test simple AsyncAPI document validation."""

        # Valid document
        valid_doc = {
            "asyncapi": "3.0.0",
            "info": {"title": "Test API", "version": "1.0.0"},
        }

        try:
            api = AsyncAPI(**valid_doc)
            print(f"✓ Valid document parsed successfully!")
            print(f"  Title: {api.info.title}")
            print(f"  Version: {api.info.version}")
            print(f"  AsyncAPI Version: {api.asyncapi}")
            return True
        except Exception as e:
            print(f"✗ Failed to parse valid document: {e}")
            return False

    def test_validation_error():
        """Test validation error handling."""

        # Invalid document (missing required fields)
        invalid_doc = {
            "asyncapi": "3.0.0",
            "info": {
                "title": "Test API"
                # Missing required "version" field
            },
        }

        try:
            api = AsyncAPI(**invalid_doc)
            print("✗ Should have failed validation!")
            return False
        except Exception as e:
            print(f"✓ Correctly caught validation error: {e}")
            return True

    def test_info_object():
        """Test Info object validation."""

        info_data = {
            "title": "My API",
            "version": "2.1.0",
            "description": "A test API",
            "contact": {"name": "API Team", "email": "api@example.com"},
        }

        try:
            info = Info(**info_data)
            print(f"✓ Info object created successfully!")
            print(f"  Title: {info.title}")
            print(f"  Contact: {info.contact.name if info.contact else 'None'}")
            return True
        except Exception as e:
            print(f"✗ Failed to create Info object: {e}")
            return False

    def main():
        """Run validation examples."""
        print("AsyncAPI Pydantic Validation Examples")
        print("=" * 40)

        tests = [test_simple_validation, test_validation_error, test_info_object]

        passed = 0
        for test in tests:
            print(f"\nRunning {test.__name__}:")
            if test():
                passed += 1

        print(f"\n{passed}/{len(tests)} tests passed!")

        if passed == len(tests):
            print("🎉 All validation examples completed successfully!")
        else:
            print("❌ Some tests failed.")

    if __name__ == "__main__":
        main()

except ImportError as e:
    print(f"Import error: {e}")
    print(
        "Note: Pydantic models are not yet fully functional due to missing dependencies in the isolated environment."
    )
    print("Run 'uv pip install pydantic' to install the required dependencies.")
