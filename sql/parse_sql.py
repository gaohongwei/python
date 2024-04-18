import sqlparse

def split_sql_into_dict_v1(sql):
    parsed_sql = sqlparse.parse(sql)[0]
    parsed_dict = {}

    for token in parsed_sql.tokens:
        if isinstance(token, sqlparse.sql.IdentifierList):
            parsed_dict["SELECT"] = [str(t) for t in token.get_identifiers()]
        elif token.normalized == "LIMIT":
            parsed_dict["LIMIT"] = str(token)
        elif token.normalized == "ORDER BY":
            parsed_dict["ORDER BY"] = str(token)
        elif token.normalized == "GROUP BY":
            parsed_dict["GROUP BY"] = str(token)
        elif token.normalized == "JOIN":
            parsed_dict["JOIN"] = str(token)
        elif token.normalized == "WHERE":
            parsed_dict["WHERE"] = str(token)

    return parsed_dict


def split_sql_into_dict_v2(sql):
    parsed_sql = sqlparse.parse(sql)[0]
    parsed_dict = {}

    for token in parsed_sql.tokens:
        if isinstance(token, sqlparse.sql.IdentifierList):
            parsed_dict["SELECT"] = [str(t) for t in token.get_identifiers()]
        elif token.normalized == "LIMIT":
            parsed_dict["LIMIT"] = str(token)
            # Extract the value from the next token
            next_token = token.next_token
            if next_token and next_token.ttype in sqlparse.tokens.Literal:
                parsed_dict["LIMIT_VALUE"] = next_token.value
        elif token.normalized == "ORDER BY":
            parsed_dict["ORDER BY"] = str(token)
            # Extract the value from the next token
            next_token = token.next_token
            if next_token:
                parsed_dict["ORDER BY_VALUE"] = next_token.value
        elif token.normalized == "GROUP BY":
            parsed_dict["GROUP BY"] = str(token)
            # Extract the value from the next token
            next_token = token.next_token
            if next_token:
                parsed_dict["GROUP BY_VALUE"] = next_token.value
        elif token.normalized == "JOIN":
            parsed_dict["JOIN"] = str(token)
            # Extract the value from the next token
            next_token = token.next_token
            if next_token:
                parsed_dict["JOIN_VALUE"] = next_token.value
        elif token.normalized == "WHERE":
            parsed_dict["WHERE"] = str(token)
            # Extract the value from the next token
            next_token = token.next_token
            if next_token:
                parsed_dict["WHERE_VALUE"] = next_token.value

    return parsed_dict

# Example usage:
sql = "SELECT column1, column2 FROM table1 WHERE condition1 ORDER BY column1 LIMIT 10"
result = split_sql_into_dict(sql)
print(result)

# Example usage:
sql = "SELECT column1, column2 FROM table1 WHERE condition1 ORDER BY column1 LIMIT 10"
result = split_sql_into_dict(sql)
print(result)



