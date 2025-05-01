class DateCalculator:
    def __init__(self, year: int, month: int, day: int):
        self.original_year = year
        self.month = month
        self.day = day

        # Adjust month and year if January or February
        if month == 1 or month == 2:
            self.month += 12
            self.year = year - 1
        else:
            self.year = year

    def calculate_day_of_week(self) -> str:
        q = self.day
        m = self.month
        K = self.year % 100
        J = self.year // 100

        # Zeller's formula
        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + (5 * J)) % 7

        # Day mapping: 0 = Saturday, 1 = Sunday, ..., 6 = Friday
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]


# Example usage
if __name__ == "__main__":
    # Try different dates here
    year = 1589
    month = 9
    day = 15

    calc = DateCalculator(year, month, day)
    weekday = calc.calculate_day_of_week()
    print(f"{day}-{month}-{year} was a {weekday}.")
