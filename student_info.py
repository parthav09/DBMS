import psycopg2 as pg2
print("Welcome to student info")
print("We help you save information about your friends")
print("Enter the task you want to enter\n 1 for stident information\n2 for student marks")
ch=int(input("Enter your choice"))
if(ch==1):
    con=pg2.connect(dbname='college',user='postgres',password='<your password>',host='localhost')
    cur=con.cursor()
    n=int(input("enter the number of students"))
    cur.execute("create table IF NOT EXISTS student(name TEXT,roll REAL,gender TEXT,sapid REAL)")
    for x in range(n):
        name=input("enter the name of the students")
        roll=int(input("enter the roll no"))
        gender=input("enter the gender of the persin")
        sapid=int(input("enter the sap id of the student"))
        cur.execute("insert into student values(%s,%s,%s,%s)",(name,roll,gender,sapid))
    cur.execute("select * from student;")
    for row in cur.fetchall():
        print(row)
        print(cur.fetchall())
        con.commit()
elif(ch==2):
    con=pg2.connect(dbname='college',user='postgres',password='shekhar17',host='localhost')
    cur=con.cursor()
    n=int(input("Enter the number of students"))
    cur.execute("CREATE TABLE IF NOT EXISTS marks(roll_no INTEGER,m1 INTEGER,m2 INTEGER,total INTEGER)")
    for x in range(n):
        roll=int(input("Enter the roll number"))
        m1=int(input("Enter your m1 marks in maths"))
        m2=int(input("Enter your m2 marks maths"))
        total=m1+m2
        cur.execute("INSERT INTO marks VALUES(%s,%s,%s,%s)",(roll,m1,m2,total))
        cur.execute("SELECT * FROM marks")
    for row in cur.fetchall():
        print(row)
        print(cur.fetchall())
        con.commit()

