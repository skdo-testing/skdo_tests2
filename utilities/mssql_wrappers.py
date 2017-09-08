import pyodbc

driver = 'SQL Server'
server = '94.130.56.45'
db1 = 'skdodb'
uname = 'skdo'
pword = 'skdo'
phone = "'%7(926) 440-34-80'"

sql_query = "select Value2 from dbo.SMSBuffer where Value1 LIKE %s and DateCreate = (select MAX(DateCreate) from SMSBuffer)" % phone

def sql_wrapper(sqlquery):
    cnxn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', host=server, database=db1, user=uname, password=pword)
    cursor = cnxn.cursor()
    cursor.execute(sqlquery)
    rows = cursor.fetchall()
    return rows

print(sql_wrapper(sql_query))