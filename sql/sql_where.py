

where_conditions = [
    {
        "table_name": "sales",
        "column": "product",
        "opr": "=",
        "value": "A"
    },
    {
        "table_name": "sales",
        "column": "region",
        "opr": "=",
        "value": "East"
    },
    {
        "table_name": "sales",
        "column": "sales_date",
        "opr": "BETWEEN",
        "value": {"start": "2023-01-01", "end": "2023-12-31"}
    },
    {
        "table_name": "sales",
        "column": "sales_amount",
        "opr": ">",
        "value": {"type": "fixed_value", "data": 10000}
    },
    {
        "table_name": "sales",
        "column": "discount_percentage",
        "opr": ">",
        "value": {"type": "function", "name": "calculate_discount_threshold", "column": "sales_amount"}
    },
    {
        "table_name": "sales",
        "column": "order_date",
        "opr": "before",
        "value": "2023-06-30"
    },
    {
        "table_name": "sales",
        "column": "delivery_date",
        "opr": "after",
        "value": "2023-07-01"
    },
    {
        "table_name": "sales",
        "column": "quantity",
        "opr": "greater",
        "value": 100
    }
]
