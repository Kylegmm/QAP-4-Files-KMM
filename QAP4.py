#Created by: Kyle March-MacCuish
#Created on: 2023-11-25
#program is for One Stop Insurance Company to calucalate insurance


from datetime import datetime

# Function to set default values
def set_default_values():
    default_values = {
        "next_policy_number": 1944,
        "basic_premium": 869.00,
        "discount_additional_cars": 0.25,
        "cost_extra_liability": 130.00,
        "cost_glass_coverage": 86.00,
        "cost_loaner_car": 58.00,
        "HST_rate": 0.15,
        "processing_fee_monthly": 39.99
    }
    return default_values

# Function to validate province
def validate_province(province):
    valid_provinces = ["ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "NL", "PE"]
    return province.upper() in valid_provinces

# Function to validate postal code
def validate_postal_code(postal_code):
    return len(postal_code) == 6 and postal_code[0].isalpha() and postal_code[1].isdigit() and postal_code[2].isalpha() and postal_code[3].isdigit() and postal_code[4].isalpha() and postal_code[5].isdigit()

# Function to validate phone number
def validate_phone_number(phone_number):
    return len(phone_number) == 10 and phone_number.isdigit()

# Function to validate payment method
def validate_payment_method(payment_method):
    valid_methods = ["Full", "Monthly", "Down Pay"]
    return payment_method.capitalize() in valid_methods

# Function to calculate insurance premium
def calculate_insurance_premium(num_cars, extra_liability, glass_coverage, loaner_car, basic_premium, discount_additional_cars,
                                cost_extra_liability, cost_glass_coverage, cost_loaner_car):
    total_premium = basic_premium + (num_cars - 1) * (basic_premium * discount_additional_cars)
    extra_costs = 0
    if extra_liability == 'Y':
        extra_costs += num_cars * cost_extra_liability
    if glass_coverage == 'Y':
        extra_costs += num_cars * cost_glass_coverage
    if loaner_car == 'Y':
        extra_costs += num_cars * cost_loaner_car
    total_premium += extra_costs
    return total_premium

def generate_receipt(first_name, last_name, address, city, province, postal_code, phone_number, num_cars, extra_liability,
                     glass_coverage, loaner_car, payment_method, down_payment, claims, insurance_premium, HST_rate,
                     processing_fee_monthly):
    formatted_claims = "\n".join([f"{i + 1}. {claim['date']} {' ' * (12 - len(claim['date']))}${claim['amount']:,.2f}"
                                  for i, claim in enumerate(claims)])
    receipt = f"""
    {'*' * 50}
     !!!!!           One Stop Insurance Company
     ! 1 !
     !!!!!         Receipt for Insurance Purchase
    {'*' * 50}

    Customer Information:
                 Name: {first_name.capitalize()} {last_name.capitalize()}
                 Address: {address}
                 City: {city.title()}
                 Province: {province.upper()}
                 Postal Code: {postal_code}
                 Phone Number: {phone_number}

   Insurance Information:
                 Number of Cars: {num_cars}
                 Extra Liability: {extra_liability}
                 Glass Coverage: {glass_coverage}
                 Loaner Car: {loaner_car}
                 Payment Method: {payment_method.capitalize()}
                 Down Payment: ${down_payment:.2f} 

    {'-' * 50}
      Insurance Premium: ${insurance_premium:.2f}
              HST (15%): ${insurance_premium * HST_rate:.2f}
             Total Cost: ${insurance_premium + (insurance_premium * HST_rate):.2f}
    {'-' * 50}

    Previous Claims:
    Claim #    Claim Date    Amount
    {'-' * 30}
    {formatted_claims}
    {'-' * 30}
    """
    print(receipt)

# Main program
def main():
    default_values = set_default_values()
    while True:
        claims = [
            {"date": "2023-01-15", "amount": 500.00},
            {"date": "2023-04-22", "amount": 800.00},
            {"date": "2023-08-10", "amount": 1200.00}
        ]

        # Gather customer information
        first_name = input("Enter customer's first name (type 'end' to finish): ")
        if first_name.lower() == 'end':
            break

        last_name = input("Enter customer's last name: ")
        address = input("Enter address: ")
        city = input("Enter city: ")
        province = input("Enter province (2 letter code): ")
        while not validate_province(province):
            province = input("Enter a valid province (2 letter code): ")
        postal_code = input("Enter postal code: ")
        while not validate_postal_code(postal_code):
            postal_code = input("Enter a valid postal code: ")
        phone_number = input("Enter phone number: ")
        while not validate_phone_number(phone_number):
            phone_number = input("Enter a valid phone number: ")

        num_cars = int(input("Enter number of cars: "))
        extra_liability = input("Extra liability coverage? (Y/N): ").upper()
        while extra_liability not in ['Y', 'N']:
            extra_liability = input("Enter 'Y' for Yes or 'N' for No: ").upper()
        glass_coverage = input("Glass coverage? (Y/N): ").upper()
        while glass_coverage not in ['Y', 'N']:
            glass_coverage = input("Enter 'Y' for Yes or 'N' for No: ").upper()
        loaner_car = input("Loaner car coverage? (Y/N): ").upper()
        while loaner_car not in ['Y', 'N']:
            loaner_car = input("Enter 'Y' for Yes or 'N' for No: ").upper()
        payment_method = input("Payment method (Full/Monthly/Down Pay): ").capitalize()
        while not validate_payment_method(payment_method):
            payment_method = input("Enter a valid payment method: ").capitalize()
        down_payment = 0.0
        if payment_method == "Down Pay":
            down_payment = float(input("Enter the down payment amount: "))
            payment_method = "Monthly"  # Changing to Monthly as down payment is usually followed by monthly payments

        # Calculate insurance premium
        insurance_premium = calculate_insurance_premium(num_cars, extra_liability, glass_coverage, loaner_car,
                                                        default_values["basic_premium"],
                                                        default_values["discount_additional_cars"],
                                                        default_values["cost_extra_liability"],
                                                        default_values["cost_glass_coverage"],
                                                        default_values["cost_loaner_car"])

        # Calculate total cost
        total_cost = insurance_premium + (insurance_premium * default_values["HST_rate"])

        # Adjust total cost for 'Down Pay' scenario
        if down_payment > 0:
            total_cost -= down_payment

        # Generate receipt
        generate_receipt(first_name, last_name, address, city, province, postal_code, phone_number, num_cars,
                         extra_liability, glass_coverage, loaner_car, payment_method, down_payment, claims,
                         insurance_premium, default_values["HST_rate"], default_values["processing_fee_monthly"])

if __name__ == "__main__":
    main()