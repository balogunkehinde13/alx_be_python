from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date():
    numOfDays = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=numOfDays)
    print(f"Future Date: {future_date.strftime('%Y-%m-%d')}")

display_current_datetime()
calculate_future_date()