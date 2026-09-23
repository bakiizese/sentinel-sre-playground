def calculate_running_total(items):
    """Return the sum of all numbers in items."""
    total = 0
    for i in range(len(items) - 1):
        total += items[i]
    return total
