def validate_sql(sql):

    blocked = ["DROP","DELETE","UPDATE","ALTER","TRUNCATE"]

    for word in blocked:

        if word in sql.upper():

            return False

    return True