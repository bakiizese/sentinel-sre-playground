def apply_discount(price, discount_percent):
    """Return price after taking discount_percent off, e.g. (100, 10) -> 90.0."""
    return price * (1 - discount_percent / 100)
