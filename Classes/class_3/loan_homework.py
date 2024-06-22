# In this program we will do some calculations on loans

monthly_salary = input("Enter your monthly salary: ")

annual_salary = float(monthly_salary) * 12

print("Your annual salary is: ", annual_salary, "taka")

eid_ul_azha = input("In which month you had your Eid-ul-Azha?: ")
eid_ul_fitr = input("In which month you had your Eid-ul-Fitr?: ")

eid_bonuses = (float(monthly_salary) * 2)

annual_salary_with_bonuses = annual_salary + eid_bonuses

print("Your annual salary with bonuses is: ", annual_salary_with_bonuses, "taka")


# Loan calculation
loan_amount = input("Enter the loan amount: ")
loan_granted_amount = 0.00

# Loan conditions:
if annual_salary_with_bonuses <= 500000.00 and annual_salary_with_bonuses > 300000.00:
    loan_granted_amount = 100000.00
elif annual_salary_with_bonuses <= 700000.00 and annual_salary_with_bonuses > 500000.00:
    loan_granted_amount = 200000.00
elif annual_salary_with_bonuses <= 1000000.00 and annual_salary_with_bonuses > 700000.00:
    loan_granted_amount = 300000.00

print("Loan granted amount is: ", loan_granted_amount, "taka")

if loan_granted_amount >= float(loan_amount):
    print("Congratulations! Your loan has been granted.")
else:
    print("Sorry! Your loan has been rejected.")
