has_high_income = input("Do you have high income? (True/False): ")
has_good_credit = input("Do you have good credit? (True/False): ")
has_criminal_record = input("Do you have a criminal record? (True/False): ")

has_high_income = bool(has_high_income)
has_good_credit = bool(has_good_credit)
has_criminal_record = bool(has_criminal_record)

if has_high_income and has_good_credit:
    print("Eligible for loan") 
elif has_high_income or has_good_credit:
    print("Eligible for loan")
elif has_good_credit and not has_criminal_record:
    print("Eligible for loan")
elif has_good_credit and has_criminal_record:
    print("Not Eligible for loan")
elif has_high_income or has_good_credit and not has_criminal_record:
    print("Eligible for loan")

