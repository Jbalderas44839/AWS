import sqlite3
import time


#Creatres a database file called 'products.sqlite' and connects to it 
try:
    connection = sqlite3.connect('sample')
    cur = connection.cursor()
    print('\nVery good! You have connected to the database successfully!')
    #the below is sql code for viewing tables
    #sql_query = """SELECT name FROM sqlite_master
    #WHERE type ='table';"""
    #the below executes the above sql code
    #cur.execute(sql_query)

    #question4 inserting into table 
    #=========================================================================
    #script = """INSERT INTO PRODUCTS
    #(id, name, inventory, unit)
    #VALUES
    #(1234321, 'stapler', 63, '$5.32'),
    #(2345432, 'calculator', 14, '$83.78') """
    #cur.execute(script)
    #print("The records have been inserted successfully into the sample db")
    #=========================================================================
    #print("List of tables\n")
    #the below fetches all the rows of the query 
    #print(cur.fetchall())

except Exception as e:
    print("Exception: {}".format(e))
    raise Exception(e)

#question4 creating table
#============================================================== 
#table = """CREATE TABLE PRODUCTS (
    #id VARCHAR(255) NOT NULL,
    #name CHAR(255) NOT NULL,
    #inventory VARCHAR(255),
    #unit cost VARCHAR(255)
    #);"""

    #cur.execute(table)

    #print("Table is ready")
#==============================================================
#Identifies version of sqlite installed
#cur.execute('select sqlite_version();')
#version = cur.fetchall()
#print('\nThe version of sqlite you have installed is: ',version)

#Closes connection to the database
print('\nTime to disconnect from the database. Please wait...')
cur.close()
time.sleep(3)

#Closes connection to the sqlite 'instance'
print('\nAnd now disconnecting form the server. Goodbye!')
connection.close()