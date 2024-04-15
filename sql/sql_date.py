import datetime

def get_last_n_date_range(n, unit):
    current_date = datetime.datetime.now()
    if unit == 'days':
        start_date = (current_date - datetime.timedelta(days=n - 1)).strftime('%Y-%m-%d')
    elif unit == 'weeks':
        start_date = (current_date - datetime.timedelta(weeks=n)).strftime('%Y-%m-%d')
    elif unit == 'months':
        start_date = (current_date - relativedelta(months=n)).strftime('%Y-%m-%d')
    elif unit == 'years':
        start_date = (current_date - relativedelta(years=n)).strftime('%Y-%m-%d')
    elif unit == 'quarters':
        start_date = (current_date - relativedelta(months=n*3)).strftime('%Y-%m-%d')
    else:
        raise ValueError("Invalid unit. Unit must be one of: 'days', 'weeks', 'months', 'years', 'quarters'")
    
    end_date = current_date.strftime('%Y-%m-%d')
    return  {"start": start_date, "end": end_date}

# Example usage
last_7_days_unit, last_7_days_range = get_last_n_date_range(7, 'days')
print("Last 7 days unit:", last_7_days_unit)
print("Last 7 days range:", last_7_days_range)

last_2_weeks_unit, last_2_weeks_range = get_last_n_date_range(2, 'weeks')
print("Last 2 weeks unit:", last_2_weeks_unit)
print("Last 2 weeks range:", last_2_weeks_range)
