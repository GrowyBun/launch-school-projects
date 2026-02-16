import math

def is_invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0 or math.isnan(number):
            return True
    except ValueError:
        return True

    return False

def get_loan_amount():
    print("What's the loan amount?")
    loan = float(input())

    while is_invalid_number(loan):
        print("Please enter a valid number.")
        loan = float(input())

    return loan

def get_apr():
    while True:
        print('What is the annual percentage rate?')
        print('(example: 2.5 for 2.5% or 5 for 5%)')
        annual_rate = input()

        try:
            annual_rate = float(annual_rate)
            if 0 <= annual_rate <= 100:
                return annual_rate

            print('Please enter a number between 0 and 100.')
        except ValueError:
            print('That does not look like a valid number.')

def get_loan_year_duration():
    print("What's the duration of the loan in years?")
    year_duration = float(input())

    while is_invalid_number(year_duration):
        print('Please enter a valid number')
        year_duration = float(input())

    return year_duration

def calculate_monthly_interest(yearly_rate):
    annual_interest_rate = yearly_rate / 100
    monthly_rate = annual_interest_rate / 12
    return monthly_rate

def calculate_loan_month_duration(year_duration):
    month_duration = year_duration * 12
    return month_duration

def calculate_monthly_payment(
                              loan,
                              monthly_rate,
                              month_duration,
                              ):
    payment = loan * (
        monthly_rate /
            (1 - (1 + monthly_rate) ** (-month_duration))
    )
    return payment

print('--- CAR LOAN CALCULATOR ---')
while True:
    loan_amount = get_loan_amount()
    apr = get_apr()
    loan_year_duration = get_loan_year_duration()
    monthly_interest_rate = calculate_monthly_interest(apr)
    loan_month_duration = calculate_loan_month_duration(loan_year_duration)
    monthly_payment = calculate_monthly_payment(
                                                loan_amount,
                                                monthly_interest_rate,
                                                loan_month_duration,
                                                )

    print(f'Your monthly payment is ${monthly_payment:.2f}')
    print('Would you like to perform another calculation? (y/n)')
    rerun = input()
    if rerun and rerun[0].lower() != 'y':
        break