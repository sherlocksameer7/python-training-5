import sqlite3

connection  = sqlite3.connect("college.db")    # creating a database 1st step,

# In this Student was starts with Cap S letter
connection.execute('''   Create Table Student(   
                           Id Integer Primary Key Autoincrement,
                           Name Text,
                           Rollnumber Integer,
                           Admnno Integer,
                           College Text

);     ''')     # created successfully

print("Table Created Successfully")

get_Name = input("Enter Name: ")
get_Rollnumber = input("Enter Rollnumber: ")
get_Admission_No = input("Enter Admission Number: ")
get_College_name = input("Enter College Name: ")
connection.execute("Insert into Student(Name, Rollnumber, Admnno, College) \
                   Values('"+get_Name+"',"+get_Rollnumber+","+get_Admission_No+",'"+get_College_name+"')")  # This was Student was in S in Capital Letter
connection.commit()
connection.close()
print("Inserted Successfully")