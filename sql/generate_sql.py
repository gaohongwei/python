//

import datetime

def get_last_year_date_range():
    current_date = datetime.datetime.now()
    last_year_start = (current_date - datetime.timedelta(days=current_date.timetuple().tm_yday + 365)).strftime('%Y-%m-%d')
    last_year_end = (current_date - datetime.timedelta(days=current_date.timetuple().tm_yday)).strftime('%Y-%m-%d')
    return last_year_start, last_year_end

def get_last_7_days_date_range():
    current_date = datetime.datetime.now()
    last_7_days_start = (current_date - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    last_7_days_end = current_date.strftime('%Y-%m-%d')
    return last_7_days_start, last_7_days_end

def generate_sql_with_conditions_dict(table_name, columns, conditions_dict=None):
    conditions = []
    if conditions_dict:
        for column, value in conditions_dict.items():
            conditions.append(f"{column} = '{value}'")

    # Add conditions for "last year" or "last 7 days"
    if 'last_year' in conditions_dict:
        last_year_start, last_year_end = get_last_year_date_range()
        conditions.append(f"order_date >= '{last_year_start}' AND order_date <= '{last_year_end}'")
    elif 'last_7_days' in conditions_dict:
        last_7_days_start, last_7_days_end = get_last_7_days_date_range()
        conditions.append(f"order_date >= '{last_7_days_start}' AND order_date <= '{last_7_days_end}'")

    where_clause = ""
    if conditions:
        where_clause = "WHERE " + " AND ".join(conditions)

    sql_query = f"SELECT {', '.join(columns)} FROM {table_name} {where_clause};"
    return sql_query

# Example usage
columns = ["customer_id", "order_date", "total_amount"]
conditions_dict = {"region": "North", "last_year": True}
sql_query = generate_sql_with_conditions_dict("orders", columns, conditions_dict)
print(sql_query)

conditions_dict = {"region": "North", "last_7_days": True}
sql_query = generate_sql_with_conditions_dict("orders", columns, conditions_dict)
print(sql_query)
