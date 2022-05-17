#Скрипт предназначен для обращения к базе данных и вывода определеенных строк для последующей обработки

from pdb import pm
import pymysql#Для подключения к серверу
import datetime

'''
def query_env ():

    mycursor = mydb.cursor() #cursor created

    select_query = "SELECT * FROM diplom_test.input_data ORDER BY id DESC LIMIT 500"#Выгрузка всей БД

    mycursor.execute(select_query)
    
    rows = mycursor.fetchall()

    pmh = [] #Массив атмосферного давления
    alt = [] #Массив высоты над уровнем моря
    temp = [] #Массив температуры
    time_line = [] #Массив временного промежутка

    for row in rows:
        pmh.append(row[11])
        alt.append(row[12])
        temp.append(row[13])
        time_line.append(row[17])

    return pmh, alt, temp, time_line

'''

def query_acc_z ():
  #server connection
  mydb = pymysql.connect(
  host="localhost",
  user="root",
  database="diplom_test", #database
  passwd="BMSTU_rk9_diplom"
  ) 

  mycursor = mydb.cursor() #cursor created

  select_query = "SELECT acc_z FROM diplom_test.input_data ORDER BY id DESC LIMIT 500"

  mycursor.execute(select_query)
    
  rows = mycursor.fetchall()

  acc_z = [] #значений акселлерометра по оси z

  for row in rows:
    acc_z.append(row[0])

  acc_z.reverse()#Делаем реверс массива (переворачиваем)

  mycursor.close()
  mydb.close()

  return acc_z

#print(query_acc_z())#Проверка показала, что данный кусок кода выводит все актуально и нормально