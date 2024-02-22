# Given values
remaining_months =296  # Remaining months of payment
remaining_balance = 101629.46  # Current remaining balance
yearly_interest_rate = 6.11 / 100  # Yearly loan interest rate converted to decimal
early_repayment_amount = 10000  # Amount of early repayment

# Updated remaining balance after early repayment
updated_balance = remaining_balance - early_repayment_amount

# Monthly interest rate
monthly_interest_rate = yearly_interest_rate / 12

# Function to calculate total interest paid over the remaining term using the formula for an amortizing loan
def calculate_total_interest(principal, monthly_rate, months):
    # If the interest rate is 0, the total interest is 0 as well, because all payment goes to principal
    if monthly_rate == 0:
        return 0
    else:
        # Monthly payment calculation using the formula for an annuity
        monthly_payment = principal * (monthly_rate / (1 - (1 + monthly_rate) ** -months))
        total_payment = monthly_payment * months
        total_interest = total_payment - principal
        return total_interest

# Total interest paid if no early repayment is made
total_interest_without_early_repayment = calculate_total_interest(remaining_balance, monthly_interest_rate, remaining_months)

# Total interest paid after making an early repayment
total_interest_with_early_repayment = calculate_total_interest(updated_balance, monthly_interest_rate, remaining_months)

# Interest saved by making the early repayment
interest_saved = total_interest_without_early_repayment - total_interest_with_early_repayment

print("Payment in % total=", total_interest_with_early_repayment, "Your saving=", interest_saved)

# Calculate the new monthly payment after reducing the principal by the early repayment, keeping the interest rate the same,
# but reducing the number of months to keep the monthly payment amount the same.

# Original monthly payment calculation using the annuity formula
original_monthly_payment = remaining_balance * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -remaining_months))

# Function to find the new number of months required to pay off the updated balance with the same monthly payment amount
def find_new_term(principal, monthly_payment, monthly_rate):
    if monthly_rate == 0:
        return principal / monthly_payment
    else:
        # Using the formula for the number of payment periods in an annuity, solving for n
        from math import log
        months = log(monthly_payment / (monthly_payment - principal * monthly_rate)) / log(1 + monthly_rate)
        return months

# New term in months to pay off the updated balance with the original monthly payment amount
new_term_months = find_new_term(updated_balance, original_monthly_payment, monthly_interest_rate)

# Total interest paid over the new term with the same monthly payment
total_interest_new_term = calculate_total_interest(updated_balance, monthly_interest_rate, new_term_months)
new__term_interest_saved = total_interest_without_early_repayment - total_interest_new_term

print("New amount of months=", new_term_months, "Payment in % total=", total_interest_new_term, "Your saving=", new__term_interest_saved)

