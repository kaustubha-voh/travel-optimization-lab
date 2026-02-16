def calculate_cpp(cash_price, points, taxes):
    return ((cash_price - taxes)/points)*100

def calculate_luxury_score(cpp, cabin):
    multipliers = {
        "economy": 1.0,
        "business": 1.3,
        "first": 1.5
    }
    return cpp * multipliers.get(cabin.lower(), 1.0)

def main():
    cash_price = float(input("Enter cash price: "))
    points = float(input("Enter points required: "))
    taxes = float(input("Enter taxes: "))
    cabin = input("Enter cabin (economy/business/first): ")

    cpp = calculate_cpp(cash_price, points, taxes)
    luxury_score = calculate_luxury_score(cpp, cabin)

    print(f"Cents per point: {cpp:.2f}")
    print(f"Luxury-adjusted score: {luxury_score:.2f}")


if __name__ == "__main__":
    main()
