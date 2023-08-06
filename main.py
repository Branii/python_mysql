import mysql.connector
from mysql.connector import Error
from config import config

#insert data into users tabale

def createDatabase(databasename) : #Accepts 1 parameter
    cursor = connection.cursor()
    query = "CREATE DATABASE IF NOT EXISTS ", databasename
    cursor.execute(query)
    connection.commit()
    print("Database created successfully")
    cursor.close()
    connection.close() # end of create database function | will create database when called
    
def createTable(tablename) : #Accepts 1 parameter
    cursor = connection.cursor()
    query = "CREATE TABLE IF NOT EXISTS ", tablename
    cursor.execute(query)
    connection.commit()
    print("Table created successfully")
    cursor.close()
    connection.close() # end of create table function | will create table when called

def addUser(username,email,password) : #Accepts 3 parameters
    cursor = connection.cursor()
    query = "INSERT INTO users(username,email,password) VALUES(%s,%s,%s)"
    params = (username,email,password)
    cursor.execute(query,params)
    connection.commit()
    print("User added successfully")
    cursor.close()
    connection.close() # end of insert data function | will insert new data with params when called
 
def selectUsers() : #Accepts 0 parameter
    cursor = connection.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Total number of rows is: ", cursor.rowcount)
    for row in rows:
        print(row)
    cursor.close()
    connection.close() # end of select data function | will select all data when called  

def updateUser(username,email,userid) : #Accepts 3 parameter
    cursor = connection.cursor()
    query = "UPDATE users SET username = %s, email = %s  WHERE uid = %s"
    params = (username,email,userid)
    cursor.execute(query,params)
    connection.commit()
    print("User updated successfully")
    cursor.close()
    connection.close() # end of update data function | will update data with params when called
    
def deleteUser(userid) : #Accepts 1 parameter
    cursor = connection.cursor()
    query = "DELETE FROM users WHERE uid = %s"
    params = (userid)
    cursor.execute(query,params)
    connection.commit()
    print("User deleted successfully")
    cursor.close()
    connection.close() # end of delete data function | will delete data with params when called
    
    
#basically run or test all your functions here by calling them 
try:
    connection = mysql.connector.connect(host = config['host'], database = config['database'], user = config['user'], passwd = config['password'])
    if connection.is_connected:
      #addnewuser("username","email","password");  
      #selectUsers()
      #updateUser("black","black@gmail.com",4) 
      #createDatabase("somename") 
      createTable("tablename")
        
        
except Error as err:
    print("Some error occured",err)
 