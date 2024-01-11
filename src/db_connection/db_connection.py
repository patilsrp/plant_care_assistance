import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    password="abc123",
    database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS login (
        username VARCHAR(255),
        password VARCHAR(255)
    )
''')
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS register (
        username VARCHAR(255),
        password VARCHAR(255)
    )
''')

mycursor.execute('''
        CREATE TABLE IF NOT EXISTS plants (
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            type VARCHAR(255),
            name VARCHAR(255),
            fertilizers VARCHAR(1000),
            waterschedule VARCHAR(255),
            sunlightrequirement VARCHAR(255),
            botanicalname VARCHAR(255),
            caretips VARCHAR(255),
            lifespan VARCHAR(255),
            growingseason VARCHAR(255)     
        )
    ''')