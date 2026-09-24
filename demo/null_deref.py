def get_user_display_name(user):
    """Prefer the user's nickname, falling back to their full name."""
    nickname = user.get("nickname")
    return (nickname.strip() if nickname is not None else None) or user["name"]
