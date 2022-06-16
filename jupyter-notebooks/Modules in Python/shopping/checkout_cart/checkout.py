def checkout_items(items_dict):
    """
    Takes a dictionary of items and their prices and returns the total price
    """
    total = 0
    for price in items_dict.values():
        total += price
    return total
