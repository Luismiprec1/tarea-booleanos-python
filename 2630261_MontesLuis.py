# Student: Luis Angel Montes Hernandez
# Student ID: 2630261
# Group: IM3
# Assignment: Numeric and Boolean Values in Python
# File: 2630261_MontesLuis.py

# Executive Summary
# In Python, int is used for whole numbers and float is used for decimal values.
# A float can represent measurements and money amounts that have decimal parts.
# A bool stores one of two values: True or False.
# Comparisons such as >= and == create boolean results.
# Arithmetic operators can add, subtract, multiply, divide, and find remainders.
# Logical operators such as and, or, and not combine conditions for decisions.
# Input validation helps stop negative or invalid values before doing calculations.
# This file has six problems with descriptions, inputs, outputs, validations, and test cases.

# Good Practices
# - Use int for counters and whole values, and float for decimal quantities.
# - Save intermediate results in clear variables instead of repeating expressions.
# - Validate data before calculations, especially before division.
# - Use descriptive variable names and error messages that are easy to understand.
# - Explain what true and false mean for each result.

import math

ABSOLUTE_ZERO_C = -273.15
HIGH_TEMPERATURE_C = 30.0
REGULAR_HOURS_LIMIT = 40.0
OVERTIME_MULTIPLIER = 1.5
DISCOUNT_RATE = 0.10
MIN_LOAN_INCOME = 8000.0
MAX_DEBT_RATIO = 0.40
MIN_CREDIT_SCORE = 650


def get_finite_float(value_text):
    """Convert text or a number to a finite float."""
    try:
        number_value = float(value_text)
    except (ValueError, TypeError, OverflowError):
        raise ValueError("invalid input") from None

    if not math.isfinite(number_value):
        raise ValueError("invalid input")
    return number_value


def read_float(prompt_text):
    return get_finite_float(input(prompt_text).strip())


def read_integer(prompt_text):
    try:
        return int(input(prompt_text).strip())
    except (ValueError, TypeError, OverflowError):
        raise ValueError("invalid input") from None


# Problem 1: Temperature converter and range flag
# Description: Converts Celsius to Fahrenheit and Kelvin.
# It also marks the temperature as high when Celsius is at least 30 degrees.
# Inputs:
# - temp_c: a finite number in Celsius.
# Outputs:
# - Fahrenheit, Kelvin, and High temperature (true or false).
# Validations:
# - The value must be numeric and finite.
# - Celsius cannot be lower than absolute zero (-273.15).
# Test cases:
# 1) Normal: 25 -> Fahrenheit 77.00, Kelvin 298.15, high false.
# 2) Border: -273.15 -> Fahrenheit -459.67, Kelvin 0.00, high false.
# 3) Error: -300 -> Error: invalid input.
def calculate_temperature(temp_c):
    temp_c = get_finite_float(temp_c)
    if temp_c < ABSOLUTE_ZERO_C:
        raise ValueError("invalid input")

    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15
    is_high_temperature = temp_c >= HIGH_TEMPERATURE_C
    return temp_f, temp_k, is_high_temperature


def run_problem_1():
    print("Problem 1: Temperature converter")
    try:
        temp_c = read_float("Enter temperature in Celsius: ")
        temp_f, temp_k, is_high_temperature = calculate_temperature(temp_c)
        print(f"Fahrenheit: {temp_f:.2f}")
        print(f"Kelvin: {temp_k:.2f}")
        print(f"High temperature: {str(is_high_temperature).lower()}")
    except ValueError:
        print("Error: invalid input")


# Problem 2: Work hours and overtime payment
# Description: Calculates regular pay and overtime pay for one week.
# Hours above 40 are paid at 150 percent of the regular hourly rate.
# Inputs:
# - hours_worked: finite weekly hours, zero or more.
# - hourly_rate: finite hourly pay greater than zero.
# Outputs:
# - Regular pay, overtime pay, total pay, and Has overtime.
# Validations:
# - Hours cannot be negative and the rate must be greater than zero.
# Test cases:
# 1) Normal: 45 hours, rate 100 -> regular 4000, extra 750, total 4750, true.
# 2) Border: 0 hours, rate 1 -> all pay 0, overtime false.
# 3) Error: -2 hours, rate 100 -> Error: invalid input.
def calculate_weekly_pay(hours_worked, hourly_rate):
    hours_worked = get_finite_float(hours_worked)
    hourly_rate = get_finite_float(hourly_rate)
    if hours_worked < 0 or hourly_rate <= 0:
        raise ValueError("invalid input")

    regular_hours = min(hours_worked, REGULAR_HOURS_LIMIT)
    overtime_hours = max(hours_worked - REGULAR_HOURS_LIMIT, 0.0)
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > REGULAR_HOURS_LIMIT
    return regular_pay, overtime_pay, total_pay, has_overtime


def run_problem_2():
    print("Problem 2: Weekly pay")
    try:
        hours_worked = read_float("Enter hours worked: ")
        hourly_rate = read_float("Enter hourly rate: ")
        regular_pay, overtime_pay, total_pay, has_overtime = calculate_weekly_pay(
            hours_worked, hourly_rate
        )
        print(f"Regular pay: {regular_pay:.2f}")
        print(f"Overtime pay: {overtime_pay:.2f}")
        print(f"Total pay: {total_pay:.2f}")
        print(f"Has overtime: {str(has_overtime).lower()}")
    except ValueError:
        print("Error: invalid input")


# Problem 3: Discount eligibility with booleans
# Description: Checks if a customer qualifies for a 10 percent discount.
# A student, a senior, or a purchase of at least 1000 qualifies.
# Inputs:
# - purchase_total: finite purchase amount of zero or more.
# - is_student_text and is_senior_text: YES or NO answers.
# Outputs:
# - Discount eligible (true or false) and the final total.
# Validations:
# - The purchase cannot be negative.
# - Both answers are normalized with strip() and upper(), then checked.
# Test cases:
# 1) Normal: 1200, NO, YES -> eligible true, final total 1080.00.
# 2) Border: 0, NO, NO -> eligible false, final total 0.00.
# 3) Error: 100, MAYBE, NO -> Error: invalid input.
def calculate_discount(purchase_total, is_student_text, is_senior_text):
    purchase_total = get_finite_float(purchase_total)
    if purchase_total < 0:
        raise ValueError("invalid input")

    student_answer = is_student_text.strip().upper()
    senior_answer = is_senior_text.strip().upper()
    if student_answer not in ("YES", "NO") or senior_answer not in ("YES", "NO"):
        raise ValueError("invalid input")

    is_student = student_answer == "YES"
    is_senior = senior_answer == "YES"
    discount_eligible = is_student or is_senior or purchase_total >= 1000.0
    if discount_eligible:
        final_total = purchase_total * (1 - DISCOUNT_RATE)
    else:
        final_total = purchase_total
    return discount_eligible, final_total


def run_problem_3():
    print("Problem 3: Discount eligibility")
    try:
        purchase_total = read_float("Enter purchase total: ")
        is_student_text = input("Is the customer a student? (YES/NO): ")
        is_senior_text = input("Is the customer a senior? (YES/NO): ")
        discount_eligible, final_total = calculate_discount(
            purchase_total, is_student_text, is_senior_text
        )
        print(f"Discount eligible: {str(discount_eligible).lower()}")
        print(f"Final total: {final_total:.2f}")
    except (ValueError, AttributeError):
        print("Error: invalid input")


# Problem 4: Basic statistics of three integers
# Description: Finds the sum, average, maximum, and minimum of three integers.
# It also checks if all three numbers are even.
# Inputs:
# - n1, n2, and n3: integer values; negative values are allowed.
# Outputs:
# - Sum, average, max, min, and All even (true or false).
# Validations:
# - Each input must be convertible to an integer.
# Test cases:
# 1) Normal: 2, 4, 6 -> sum 12, average 4.00, max 6, min 2, true.
# 2) Border: 0, -2, -4 -> sum -6, average -2.00, max 0, min -4, true.
# 3) Error: 3.5, 4, 6 -> Error: invalid input because 3.5 is not an integer.
def calculate_integer_stats(n1, n2, n3):
    values = (n1, n2, n3)
    if any(not isinstance(value, int) or isinstance(value, bool) for value in values):
        raise ValueError("invalid input")

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(values)
    min_value = min(values)
    all_even = n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0
    return sum_value, average_value, max_value, min_value, all_even


def run_problem_4():
    print("Problem 4: Statistics of three integers")
    try:
        n1 = read_integer("Enter first integer: ")
        n2 = read_integer("Enter second integer: ")
        n3 = read_integer("Enter third integer: ")
        sum_value, average_value, max_value, min_value, all_even = calculate_integer_stats(
            n1, n2, n3
        )
        print(f"Sum: {sum_value}")
        print(f"Average: {average_value:.2f}")
        print(f"Max: {max_value}")
        print(f"Min: {min_value}")
        print(f"All even: {str(all_even).lower()}")
    except ValueError:
        print("Error: invalid input")


# Problem 5: Loan eligibility
# Description: Calculates the share of income used for monthly debt payments.
# It checks income, debt ratio, and credit score to decide loan eligibility.
# Inputs:
# - monthly_income and monthly_debt: finite decimal amounts.
# - credit_score: a non-negative integer.
# Outputs:
# - Debt ratio and Eligible (true or false).
# Validations:
# - Income must be greater than zero, debt cannot be negative, and score cannot be negative.
# - Checking income first avoids division by zero.
# Test cases:
# 1) Normal: income 10000, debt 3000, score 700 -> ratio 0.30, eligible true.
# 2) Border: income 8000, debt 3200, score 650 -> ratio 0.40, eligible true.
# 3) Error: income 0, debt 0, score 700 -> Error: invalid input.
def check_loan_eligibility(monthly_income, monthly_debt, credit_score):
    monthly_income = get_finite_float(monthly_income)
    monthly_debt = get_finite_float(monthly_debt)
    if not isinstance(credit_score, int) or isinstance(credit_score, bool):
        raise ValueError("invalid input")
    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        raise ValueError("invalid input")

    debt_ratio = monthly_debt / monthly_income
    eligible = (
        monthly_income >= MIN_LOAN_INCOME
        and debt_ratio <= MAX_DEBT_RATIO
        and credit_score >= MIN_CREDIT_SCORE
    )
    return debt_ratio, eligible


def run_problem_5():
    print("Problem 5: Loan eligibility")
    try:
        monthly_income = read_float("Enter monthly income: ")
        monthly_debt = read_float("Enter monthly debt: ")
        credit_score = read_integer("Enter credit score: ")
        debt_ratio, eligible = check_loan_eligibility(
            monthly_income, monthly_debt, credit_score
        )
        print(f"Debt ratio: {debt_ratio:.2f}")
        print(f"Eligible: {str(eligible).lower()}")
    except ValueError:
        print("Error: invalid input")


# Problem 6: BMI and category flags
# Description: Calculates body mass index (BMI) using weight and height.
# Three boolean flags show if the BMI is underweight, normal, or overweight.
# Inputs:
# - weight_kg and height_m: finite numbers greater than zero.
# Outputs:
# - BMI rounded to two decimals and three category flags.
# Validations:
# - Weight and height must both be greater than zero.
# - Positive height also prevents division by zero.
# Test cases:
# 1) Normal: 70 kg, 1.75 m -> BMI 22.86, normal true.
# 2) Border: 18.5 kg, 1.0 m -> BMI 18.50, normal true.
# 3) Error: 70 kg, 0 m -> Error: invalid input.
def calculate_bmi(weight_kg, height_m):
    weight_kg = get_finite_float(weight_kg)
    height_m = get_finite_float(height_m)
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("invalid input")

    bmi = weight_kg / (height_m * height_m)
    is_underweight = bmi < 18.5
    is_normal = 18.5 <= bmi < 25.0
    is_overweight = bmi >= 25.0
    return round(bmi, 2), is_underweight, is_normal, is_overweight


def run_problem_6():
    print("Problem 6: BMI calculator")
    try:
        weight_kg = read_float("Enter weight in kilograms: ")
        height_m = read_float("Enter height in meters: ")
        bmi, is_underweight, is_normal, is_overweight = calculate_bmi(weight_kg, height_m)
        print(f"BMI: {bmi:.2f}")
        print(f"Underweight: {str(is_underweight).lower()}")
        print(f"Normal: {str(is_normal).lower()}")
        print(f"Overweight: {str(is_overweight).lower()}")
    except ValueError:
        print("Error: invalid input")


def main():
    print("NUMERIC AND BOOLEAN PRACTICE")
    run_problem_1()
    print()
    run_problem_2()
    print()
    run_problem_3()
    print()
    run_problem_4()
    print()
    run_problem_5()
    print()
    run_problem_6()


if __name__ == "__main__":
    main()

# Conclusions
# Int and float values are both useful because not every calculation is whole.
# Comparisons create booleans that can be used in if statements.
# I learned to combine conditions with and and or when making decisions.
# Checking ranges keeps negative values from entering calculations that need positives.
# Checking before division also prevents a zero division error.
# These examples show how numbers and conditions can work together in everyday problems.
# Becuase of the checks, the program can give a clear error instead of crashing.

# References
# 1) Python documentation - Numeric Types: int, float, and complex
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 2) Python documentation - Boolean Type: bool
#    https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# 3) Python documentation - Built-in Functions
#    https://docs.python.org/3/library/functions.html
# 4) Python documentation - Expressions and operators
#    https://docs.python.org/3/reference/expressions.html
# 5) Python Tutorial - if Statements
#    https://docs.python.org/3/tutorial/controlflow.html#if-statements
