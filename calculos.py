from datetime import datetime, timedelta

def calcularfechas(start_date_str, end_date_str):
    # Convert date strings to datetime objects
    start_date = datetime.strptime(start_date_str, '%d/%m/%Y')
    end_date = datetime.strptime(end_date_str, '%d/%m/%Y')
    # Initialize list to hold month ranges
    month_ranges = []
    # Loop over each month between the start and end dates
    current_month = start_date

    while current_month <= end_date:
        # Get the last day of the current month
        next_month = current_month.replace(day=28) + timedelta(days=4)
        last_day = next_month - timedelta(days=next_month.day)
        # Append the first and last day of the current month to the list of month ranges
        month_ranges.append((current_month.strftime('%d/%m/%Y'), last_day.strftime('%d/%m/%Y')))
        # Move to the next month
        current_month = next_month.replace(day=1)

    return month_ranges

