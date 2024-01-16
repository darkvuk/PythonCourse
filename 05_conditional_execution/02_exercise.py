# SIMPLE INTEREST
# PRINCIPAL = PRINCIPAL + INTEREST (%) * PRINCIPAL * DURATION_IN_YEARS

def calculate_simple_interest(principal, interest, duration_in_years):
    return principal + principal * 0.01 * interest * duration_in_years

print(calculate_simple_interest(1000, 5, 5))