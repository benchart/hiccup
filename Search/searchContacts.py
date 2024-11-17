

contactTable = 'Contacts'
firstNameCol = 'first_name'
lastNameCol = 'last_name'
emailCol = 'email'
usernameCol= 'username'
locationCol = 'location'
positionCol = 'position'
userIDCol = 'user_id'
query = ''

#Store the variables in an Array to be passed to the API file
contactsVarList = [contactTable, firstNameCol, lastNameCol, emailCol, usernameCol, locationCol, positionCol, userIDCol]

searchString = f"""
        SELECT {userIDCol}
        FROM {contactTable}
        WHERE {firstNameCol} LIKE :query 
        OR {lastNameCol} LIKE :query
        OR {emailCol} LIKE :query
        OR {usernameCol} LIKE :query
        OR {locationCol} LIKE :query
        OR {positionCol} LIKE :query;
"""

def searchContacts(query):
    from databaseAPI import contactsDB
    from sqlalchemy import text

    query = f"%{query.lower()}%"
    escaped_query = query.replace('%', '\\%').replace('_', '\\_')
    with contactsDB.connect() as connection:
        result = connection.execute(text(searchString), {'query': escaped_query})
    return result.fetchAll()

