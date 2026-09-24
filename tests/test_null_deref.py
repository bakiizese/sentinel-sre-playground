import pytest

def get_user_display_name(user):
    """Prefer the user's nickname, falling back to their full name."""
    nickname = user.get("nickname")
    return (nickname.strip() if nickname is not None else None) or user["name"]

def test_get_user_display_name_with_nickname():
    user = {"name": "John Doe", "nickname": "  Johnny  "}
    assert get_user_display_name(user) == "Johnny"

def test_get_user_display_name_with_none_nickname():
    user = {"name": "John Doe", "nickname": None}
    # This previously raised AttributeError: 'NoneType' object has no attribute 'strip'
    assert get_user_display_name(user) == "John Doe"

def test_get_user_display_name_without_nickname_key():
    user = {"name": "John Doe"}
    assert get_user_display_name(user) == "John Doe"

def test_get_user_display_name_with_empty_nickname():
    user = {"name": "John Doe", "nickname": "   "}
    # "   ".strip() is "", which is falsy, so it should fall back to "John Doe"
    assert get_user_display_name(user) == "John Doe"
