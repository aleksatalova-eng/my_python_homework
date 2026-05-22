def is_year_leap(year):
    return True if year % 4 == 0 else False


my_year = 1989
result = is_year_leap(my_year)
print(f"год {my_year}: {result}")
