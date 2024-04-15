def generate_sql(table_name, columns, joins=None, conditions_dict=None, functions=None, order_by=None):
    # Generate the SELECT clause
    select_clause = ", ".join(columns)
    if functions:
        select_clause = ", ".join(functions)

    # Generate the JOIN clause
    join_clause = ""
    if joins:
        join_pairs = []
        for join_info in joins:
            join_type = join_info['type']
            join_table = join_info['table']
            join_condition_dict = join_info['condition']
            join_condition = " AND ".join([f"{join_condition_dict['left_table']}.{join_condition_dict['left_column']} = {join_condition_dict['right_table']}.{join_condition_dict['right_column']}" for key, value in join_condition_dict.items()])
            join_pairs.append(f"{join_type} JOIN {join_table} ON {join_condition}")
        join_clause = " ".join(join_pairs)

    # Generate the WHERE clause
    where_clause = ""
    if conditions_dict:
        where_conditions = []
        for column, value in conditions_dict.items():
            where_conditions.append(f"{column} = '{value}'")
        where_clause = "WHERE " + " AND ".join(where_conditions)

    # Generate the ORDER BY clause
    order_by_clause = ""
    if order_by:
        order_by_functions = []
        for order in order_by:
            order_by_functions.append(order['function'] + "(" + order['column'] + ")" + " " + order['direction'])
        order_by_clause = "ORDER BY " + ", ".join(order_by_functions)

    # Combine clauses to form the SQL query
    sql_query = f"SELECT {select_clause} FROM {table_name} {join_clause} {where_clause} {order_by_clause};"
    return sql_query
