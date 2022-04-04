import mysql.connector

#Establishing The connection between the Database
connection = mysql.connector.connect(host='localhost',
                                         database='keboards',
                                         user='root',
                                         password='')
#Creating cursor 
cursor = connection.cursor()
            
class School:
  
    def addstudents(self):
        try:
            name=input("Enter the Student name:")
            rno=int(input("Enter student roll no:"))
            mail=input("Enter the student mail:")
            age=int(input("Enter the student age:"))
            fname=input("Enter the fathers name:")
            mname=input("Enter the Mothers name:")
        except:
            print("")
        
        try:
            mySql_insert_query = """INSERT INTO student_details (name,rno,mail,age,fname,mname) 
                                VALUES (%s, %s, %s, %s,%s,%s) """

            record = (name,rno,mail,age,fname,mname)
            cursor.execute(mySql_insert_query, record)
            connection.commit()

            print("")
            print(cursor.rowcount, "Record  successfully inserted into the table")
            
        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))

        
    def removestudents(self):
        remove_rno=int(input("Enter the student roll number to remove from class:"))
        sql = "DELETE FROM student_details WHERE rno = %s"
        tuple1=()
        res=list(tuple1)
        res.append(remove_rno)
        tuple1=tuple(res)
        cursor.execute(sql,tuple1)
        connection.commit()
        #cursor.execute("SELECT * FROM student_details")
        print("Succesfully deleted the Records!")
        myresult = cursor.fetchall()

        for x in myresult:
            print(x)
            
    def getdetails(self):
        sql = "SELECT * FROM student_details WHERE rno=%s"
        roll_no=int(input("Enter Roll_no:"))
        name1=tuple()
        y=list(name1)
        y.append(roll_no)
        name1=tuple(y)
        
        cursor.execute(sql,name1)
        myresult = cursor.fetchall()
        print("")
        print("Student details")
        for x in myresult:
            print(x)
        
       
    def allstudents(self):
        cursor.execute("SELECT * FROM student_details")

        myresult = cursor.fetchall()

        for x in myresult:
            print(x)
    
    def closeconnection(self):
        cursor.close()
        connection.close()  
        print("Connection Terminated succesfully")
s=School()

print("-----------------------------------")
print("Welcome to KEBOARDS School Dharwad")
print("-----------------------------------")

print("")
option=0
try:
    while(option!=5):
        print("")
        print("Choose the option!")
        print("")
        print("1.Add students")
        print("2.Remove students")
        print("3.Get Student details")
        print("4.All Students Details")
        print("5.Exit")
        print("")
        option=int(input("Enter your option:"))


        if(option==1):
            s.addstudents()
        elif(option==2):
            s.removestudents()
        elif(option==3):
            s.getdetails()
        elif(option==4):
            s.allstudents()
        elif(option==5):
            print("Thank you Have a nice day!")
            s.closeconnection()
            break
        else:
            print(option," is invalid choice!!!")
except:
    print("Enter correctly!!")
