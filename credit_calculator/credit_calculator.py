"""Loan calculator"""
import argparse
import math


# Function to calculate differentiated payment for each month
def calculate_diff_payment(principal, periods, interest_rate, month):
    i = interest_rate / (12 * 100)  # monthly interest rate
    dm = (principal / periods) + i * (principal - (principal * (month - 1)) / periods)
    return math.ceil(dm)


# Function to calculate annuity payment
def calculate_annuity_payment(principal, periods, interest_rate):
    i = interest_rate / (12 * 100)  # monthly interest rate
    annuity_payment = principal * (i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)
    return math.ceil(annuity_payment)


# Function to calculate loan principal
def calculate_loan_principal(payment, periods, interest_rate):
    i = interest_rate / (12 * 100)  # monthly interest rate
    loan_principal = payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
    return int(loan_principal)


# Function to calculate the number of periods (months) required to repay the loan
def calculate_periods(principal, payment, interest_rate):
    i = interest_rate / (12 * 100)  # monthly interest rate
    periods = math.log(payment / (payment - i * principal)) / math.log(1 + i)
    return math.ceil(periods)


# Function to convert months to years and months format
def convert_months_to_years_and_months(months):
    years = months // 12
    remaining_months = months % 12
    if years == 0:
        return f"{remaining_months} months"
    elif remaining_months == 0:
        return f"{years} years"
    else:
        return f"{years} years and {remaining_months} months"


# Function to calculate the total overpayment
def calculate_overpayment(principal, periods, payment):
    overpayment = (payment * periods) - principal
    return int(overpayment)


# Main function
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Credit Calculator")
    parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payments: annuity or diff")
    parser.add_argument("--principal", type=float, help="Loan principal")
    parser.add_argument("--payment", type=float, help="Monthly payment")
    parser.add_argument("--periods", type=int, help="Number of periods (months)")
    parser.add_argument("--interest", type=float, help="Interest rate (percentage)")

    args = parser.parse_args()
    # Check for correct parameters
    if args.type is None or args.type not in ["annuity", "diff"]:
        print("Incorrect parameters")
        return
    # Calculate differentiated payment
    if args.type == "diff":
        if args.principal is None or args.periods is None or args.periods < 0 or args.interest is None:
            print("Incorrect parameters")
            return
        total_payment = 0
        for m in range(1, args.periods + 1):
            payment = calculate_diff_payment(args.principal, args.periods, args.interest, m)
            total_payment += payment
            print(f"Month {m}: payment is {payment}")

        overpayment = total_payment - args.principal
        print(f"\nOverpayment = {math.ceil(overpayment)}")
    # Calculate annuity payment or loan principal or number of periods
    if args.type == "annuity":
        if args.interest is None or args.periods < 0:
            print("Incorrect parameters")
            return
        if args.periods is None:
            periods = calculate_periods(args.principal, args.payment, args.interest)
            print(f"It will take {convert_months_to_years_and_months(periods)} to repay this loan!")
            print(f"Overpayment = {calculate_overpayment(args.principal, periods, args.payment)}")
        elif args.principal is None:
            loan_principal = calculate_loan_principal(args.payment, args.periods, args.interest)
            print(f"Your loan principal= {loan_principal}!")
            print(f"Overpayment = {calculate_overpayment(loan_principal, args.periods, args.payment)}")
        elif args.payment is None:
            annuity_payment = calculate_annuity_payment(args.principal, args.periods, args.interest)
            print(f"Your annuity payment = {annuity_payment}!")
            print(f"Overpayment = {calculate_overpayment(args.principal, args.periods, annuity_payment)}")


# Execute main function if the script is run directly
if __name__ == "__main__":
    main()
