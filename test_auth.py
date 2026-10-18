from auth_service import register_user

def test_register_user():
    result = register_user("test@example.com", "Password123")
    assert result["email"] == "test@example.com"
    assert result["status"] == "registered"
