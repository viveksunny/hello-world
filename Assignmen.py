import cx_Oracle
connection = cx_Oracle.connect('hr/HR@XE')
cursor = connection.cursor()
#To get the columns
querystring = "select * from Employees"
cursor.execute(querystring)
fo = open("Employee.txt",'a+')
for i in cursor:
    for j in i:
        if j == 7:
            fo.write(float(j))
            fo.write(',')
        else:
            fo.write(str(j)+',')
    fo.write("\n")
fo.close()
#to read the file line by line and write in another file
fo = open("Employee.txt",'r')
nfo = open("Updated.txt",'w+')#to save the updated text
for line in fo.readlines():
    line=line.split(",")
    if line[6] == "IT_PROG":
        line[7]=float(line[7])*1.1
        line[7]=str(line[7])
        qstring = "update Employees set salary = "+ line[7] +" where EMPLOYEE_ID = " + line[0]
        cursor.execute(qstring)
        nfo.write(str(line))
        nfo.write('\n')
qstring="commit"
cursor.execute(qstring)
print("Update Successful")
fo.close()
nfo.close()
connection.close()