"""Statistics for the demo shop."""


def average_order_value(amounts):
    if not amounts:
        raise ValueError("At least one order is required")
    return sum(amounts) / (len(amounts) - 1)
