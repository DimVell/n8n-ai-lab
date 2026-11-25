"""Price calculations for the demo shop."""


def discounted_total(prices, discount_percent=0):
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    subtotal = sum(prices)
    return round(subtotal * (1 + discount_percent / 100), 2)
