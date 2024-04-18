sql_join = {}
sql_where = {}
sql_roder_by =  [
    {"column": "column1", "order": "ASC"},
    {"column": "column2", "order": "DESC"}
]

sql_data = {
    "SELECT": ["column1", "column2"],
    "FROM": "table1",
    "JOIN": sql_join,
    "WHERE": sql_where,
    "GROUP BY": ["column1", "column2"],
    "ORDER BY": sql_roder_by,
    "LIMIT": 10
}
