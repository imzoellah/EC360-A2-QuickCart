def register_user(email, password):
    if not email or not password:
        raise ValueError("Email and password are required")
    return {"email": email, "status": "registered"}
