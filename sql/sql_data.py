sql_data = {
    "SELECT": ["column1", "column2"],
    "FROM": "table1",
    "JOIN": {
        "table2": {
            "type": "INNER",
            "on": {
                "left": "table1.column_id",
                "operator": "=",
                "right": "table2.column_id"
            }
        },
        "table3": {
            "type": "LEFT",
            "on": {
                "left": "table1.column_id",
                "operator": "=",
                "right": "table3.column_id"
            }
        }
    },
    "WHERE": {
        "condition1": {
            "operator": "=",
            "value": "value1"
        },
        "condition2": {
            "operator": ">",
            "value": "value2"
        },
        "condition3": {
            "operator": "LIKE",
            "value": "%value3%"
        }
    },
    "GROUP BY": ["column1", "column2"],
    "ORDER BY": ["column1 ASC", "column2 DESC"],
    "LIMIT": 10
}
