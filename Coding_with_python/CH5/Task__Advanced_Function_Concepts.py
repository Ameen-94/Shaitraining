# Define a function to process the cake and optional order details
def cake_order(size, *args, **kwargs):
    """
    Process a cake order with optional details.

    Parameters:
    - size (str): The size of the cake (e.g., small, medium, large).
    - *args: Additional details about the cake (e.g., flavors or layers).
    - **kwargs: Optional details for the order (e.g., drinks, delivery info, captain reward).
    """
    # Display the cake size
    print(f"Order Details:")
    print(f"- Cake Size: {size}")

    # Check if there are additional details about the cake
    if args:
        print(f"- Cake Details:")
        for detail in args:
            print(f"  * {detail}")

    # Check for optional order details in kwargs
    if kwargs:
        print(f"- Optional Details:")
        for key, value in kwargs.items():
            print(f"  * {key.capitalize()}: {value}")

# Example usage of the function
cake_order("large", "chocolate flavor", "three layers", drinks="Orange Juice, Lemonade", delivery="Home Address: 123 Sweet Lane", captain_reward="5 USD")
