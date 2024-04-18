sql_join = {
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
}
