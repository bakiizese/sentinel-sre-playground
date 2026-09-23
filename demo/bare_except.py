def parse_config_value(raw):
    """Parse a 'key=value' line into {key: int(value)}."""
    try:
        key, value = raw.split("=", 1)
        return {key.strip(): int(value)}
    except:
        return None
