import request_MySQL as req #Обращаемся к выгрузке

def arr_block_acc_z(): #Разбиение массива данных на блоки максимум и минимум

    arr_acc_z = req.query_acc_z()#Выгруженный массив
    print(arr_acc_z)

    stotage = []
    
    arr_block_max = []
    arr_block_min = []
    i = 0

    for row in arr_acc_z:
        #print(row)

        if i <= 40:
            stotage.append(row)#добавляем значение в хранилище
            i += 1
            #print(i)
        elif i > 40:
            #print(max(stotage))
            arr_block_max.append(float(max(stotage)))#выводим максимум из хранилища
            arr_block_min.append(float(min(stotage)))#минимум
            stotage.clear()
            i = 1#Чтобы не терялся элемент из массива, нужно добавить его в новое хранилище
            stotage.append(row)

    #print(arr_block_min)
    return arr_block_max, arr_block_min



def class_acc_z():
    arr_block_max, arr_block_min = arr_block_acc_z()

    arr_class_max = [] #для классификации точек, которые по оси max
    arr_class_min = [] #для классификации точек, которые по оси min

    arr_class = [] #вывод итогового значения классификации точек

    buf_un = 0
    buf_ac = 0

    point_unconscious = [-0.181, -0.194] #Координаты точек положения без сознания
    point_active = [1.293, 0.822]

    #Пробегаемся по точкам максимума
    for row in arr_block_max:

        #Сравниваем с лежачим положением по оси мах
        if row > point_unconscious[0]:
            buf_un = abs(row - point_unconscious[0])
        else:
            buf_un = abs(point_unconscious[0] - row)

        #Сравниваем со активным положением по оси  max
        if row > point_active[0]:
            buf_ac = abs(row - point_active[0])
        else:
            buf_ac = abs(point_active[0] - row)

        #Сравниваем два расстояния к точкам классификации. У кого значение меньше, тому и присваиваем
        if buf_un < buf_ac:
            arr_class_max.append('unconscious')
        else:
            arr_class_max.append('active')

    #Пробегаемся по точкам минимума
    for row in arr_block_min:

        #Сравниваем с лежачим положением по оси min
        if row > point_unconscious[1]:
            buf_un = abs(row - point_unconscious[1])
        else:
            buf_un = abs(point_unconscious[1] - row)

        #Сравниваем со активным положением по оси min
        if row > point_active[1]:
            buf_ac = abs(row - point_active[1])
        else:
            buf_ac = abs(point_active[1] - row)

        #Сравниваем два расстояния к точкам классификации. У кого значение меньше, тому и присваиваем
        if buf_un < buf_ac:
            arr_class_min.append('unconscious')
        else:
            arr_class_min.append('active')

    #Начинаем цикл вывода итогового значения массива
    for i in range(len(arr_class_min)):
        if arr_class_max[i] == arr_class_min[i]:
            arr_class.append(arr_class_max[i])
        else:
            arr_class.append('und')

    #Итоговое решение по состоянию рабочего
    persent_act = (arr_class.count('active') / len(arr_class)) * 100 #Вероятность в процентах, что рабочий активничает
    persent_un = (arr_class.count('unconscious') / len(arr_class)) * 100 #Вероятность в процентах, что рабочий без сознания


    if persent_un > persent_act:
        result =  f'ВНИМАНИЕ, РАБОЧИЙ ЛЕЖИТ БЕЗ СОЗНАНИЯ!!!\n(Вероятность данного события {persent_un})'
        return result
    else:
        result = f'Рабочий в порядке\n(Вероятность данного события {persent_act})'
        return result


#print(class_acc_z())#Данный кусок кода показал, что данные передаются нормально