
def calculate_bills(unit):
    if unit < 0:
        return "invalid please enter a positive value"

    total = 0
    fixed_charge = 100

    if unit <= 100:
        total = unit * 5
    elif unit <= 300:
        total = (100 * 5) + ((unit - 100) * 7)
    else:
        total = (100 * 5) + (200 * 7) + ((unit - 300) * 10)

    total = total + fixed_charge
    return total


print(calculate_bills(250))
