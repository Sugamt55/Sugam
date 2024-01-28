def get_positive_integer(prompt):
    while True:
        try:
            # Get user input and convert it to an integer
            value = int(input(prompt))

            # Check if the entered value is a positive integer
            if value >= 0:
                return value
            else:
                print("Please enter a positive integer!")

        except ValueError:
            print("Please enter a valid number!")


def get_yes_or_no_input(prompt):
    while True:
        # Get user input and convert it to lowercase for case-insensitivity
        answer = input(prompt).lower()

        # Check if the entered value is 'y' or 'n'
        if answer == 'y' or answer == 'n':
            return answer
        else:
            print('Please answer "Y" or "N".')


def calculate_pizza_price(num_pizzas, delivery_required, is_tuesday, used_app):
    # Define constants for pricing and discounts
    base_price_per_pizza = 10.00
    delivery_charge = 2.50
    discount_percentage = 0.25
    app_discount = 0

    # Calculate total price without discounts or delivery charge
    total_price = num_pizzas * base_price_per_pizza

    # Add delivery charge if required
    if delivery_required.lower() == 'y' or delivery_required.lower() == 'yes':
        total_price += delivery_charge

    # Apply app discount if used
    if used_app.lower() == 'y' or delivery_required.lower() == 'yes':
        app_discount = total_price * discount_percentage
        total_price -= app_discount

    # Apply Tuesday discount
    if is_tuesday.lower() == 'y' or delivery_required.lower() == 'yes':
        total_price *= 0.5

    # Round the total price to two decimal places
    total_price = round(total_price, 2)

    return total_price


try:
    # Welcome message
    print("Welcome to Thapa Pizza House!\n=======================")

    # Get user inputs
    num_pizzas = get_positive_integer("How many pizzas would you like to order? ")
    delivery_required = get_yes_or_no_input("Do you want delivery for the pizzas? (Y/N) ")
    is_tuesday = get_yes_or_no_input("Is today Tuesday? (Y/N) ")
    used_app = get_yes_or_no_input("Did you connect us via our app? (Y/N) ")

    # Calculate total price based on user inputs
    total_price = calculate_pizza_price(num_pizzas, delivery_required, is_tuesday, used_app)

    # Display order summary
    print("\nTotal Order:")
    print(f"Number of Pizzas: {num_pizzas}")
    print(f"Delivery: {'Yes' if delivery_required == 'y' else 'No'}")
    print(f"Tuesday Discount: {'Yes' if is_tuesday == 'y' else 'No'}")
    print(f"App Discount: {'Yes' if used_app == 'y' else 'No'}")

    # Display total price
    print(f"\nTotal Price: £{total_price:.2f}")

except ValueError:
    print("Invalid input. Please enter a valid value.")

