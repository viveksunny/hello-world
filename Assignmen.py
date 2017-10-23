import cx_Oracle
connection = cx_Oracle.connect('hr/HR@XE')
cursor = connection.cursor()
#To get the columns
querystring = "select * from Employees"
cursor.execute(querystring)
fo = open("Employee.txt",'a+')
for row_elements in cursor:
    for column_element in row_elements:
        if column_element == 7:
            fo.write(float(column_element))
            fo.write(',')
        else:
            fo.write(str(column_element)+',')
    fo.write("\n")
fo.close()
#to read the file line by line and write in another file
fo = open("Employee.txt",'r')
nfo = open("Updated.txt",'w+')#to save the updated text
for each_row_line in fo.readlines():
    each_row_line = each_row_line.split(",")
    if each_row_line[6] == "IT_PROG":
        each_row_line[7]=float(each_row_line[7])*1.1
        each_row_line[7]=str(each_row_line[7])
        Update_string = "update Employees set salary = "+ each_row_line[7] +" where EMPLOYEE_ID = " + each_row_line[0]
        cursor.execute(Update_string)
        nfo.write(str(each_row_line))
        nfo.write('\n')
Commit_string="commit"
cursor.execute(Commit_string)
print("Update Successful")
fo.close()
nfo.close()
connection.close()
