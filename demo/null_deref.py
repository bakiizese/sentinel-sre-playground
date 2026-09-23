def get_user_display_name(user):
    """Prefer the user's nickname, falling back to their full name."""
    return user["nickname"].strip() or user["name"]
