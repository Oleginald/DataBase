import copy
import json
import sys
import datetime
import re

COMMANDS = ['exit', 'commands', 'doc', 'load', 'save', 'path', 'path -curr',
            'number -E', 'show -E', 'add -e', 'findid -e', 'del -e', 'show -e', 'filt -e',
            'number -D', 'show -D', 'add -d', 'findid -d', 'del -d', 'show -d',
            'add -ed', 'del -ed']

def doc():
    print(f'Введите команду:',end='')
    Key = input()


    if Key not in COMMANDS:
        print(f'Такой команды не существует.')
        return False


    if Key == 'exit':
        print(f'exit - выход из приложения.')
    if Key == 'commands':
        print(f'commands - просмотреть все доступные команды.')
    if Key == 'doc':
        print(f'Вывод сведений о команде.')
    if Key == 'load':
        print(f'Загрузить базу данных по адресу возвращаемому коммандой path -curr.')
    if Key == 'save':
        print(f'Сохранить внесенные изменения в базу данных(в оба файла *.emp и *.dep).')
    if Key == 'path':
        print(f'Изменяет название файлов с базой данных(по умолчанию DATABASE).')
    if Key == 'path -curr':
        print(f'Возвращает текущее название файлом с базой данных.')


    if Key == 'number -E':
        print(f'Возвращает общее количество сотрудников в базе данных')
    if Key == 'show -E':
        print(f'Выводит на экран всех сотруников в базе.')
    if Key == 'add -e':
        print(f'Добавляет сотрудника в базу. По умолчанию сотрудник вносится без указания отделов.')
    if Key == 'findid -e':
        print(f'Поиск сотрудника отдела по его атрибутам. Возвращает id сотрудника.')
    if Key == 'del -e':
        print(f'Удаляет сотрудника из базы данных.')
    if Key == 'show -e':
        print(f'Выводит на экран данные о конкретном сотруднике по его id')
    if Key == 'filt -e':
        print(f'Выводит на экран данные о сотрудниках с одинаковым значением определенного атрибута. Кроме атрибута отдела. Для этого есть команда fild -d')


    if Key == 'number -D':
        print(f'Выводит на экран данные о сотрудниках с одинаковым значением определенного атрибута.')
    if Key == 'show -D':
        print(f'Выводит на экран все отделы в базе.')
    if Key == 'add -d':
        print(f'Добавляет отдел в базу.')
    if Key == 'findid -d':
        print(f'Поиск отдела по его имени. Возвращает id отдела.')
    if Key == 'del -d':
        print(f'Удаляет отдел из базы данных.')
    if Key == 'show -d':
        print(f'Выводит на экран данные о конкретном отделе по его id')



    if Key == 'add -ed':
        print(f'Добавляет сотрудника в отдел.')
    if Key == 'del -ed':
        print(f'Удаляет сотрудника из отдела')


def userInputE():
    a = [] # под все аргументы
    print('Введите Name: ', end='')
    Name = input()
    print('Введите SecondName: ', end='')
    SecondName = input()
    print('Введите ThirdName: ', end='')
    ThirdName = input()
    print('Введите Address: ', end='')
    Address = input()
    print('Введите DateBirth: ', end='')
    DateBirth = input()
    print('Введите Position: ', end='')
    Position = input()
    a.append(Name)
    a.append(SecondName)
    a.append(ThirdName)
    a.append(Address)
    a.append(DateBirth)
    a.append(Position)
    return a

def userInputD():
    a = []
    r = []
    e = []
    print('Введите Name: ', end='')
    Name = input()
    print('Введите Список комнат (Rooms): ', end='')
    print('Когда закончите введите stop.')
    while True:
        print(f'Введите название комнаты или stop:',end='')
        tmp = input()
        if tmp == 'stop':
            break
        r.append(tmp)
    # r.pop(len(r)-1)
    print('Введите Список сотрудников.', end='')
    print('Когда закончите введите stop.')
    while True:
        print(f'Введите id сотрудника или stop:',end='')
        tmp = input()
        if tmp == 'stop':
            break
        tmp = int(tmp)
        e.append(tmp)
    # e.pop(len(e)-1)

    a.append(Name)
    a.append(r)
    a.append(e)
    return a

class Employees():
    '''Класс, отвечающий за всех сотрудников'''
    ATTRS = ['Name', 'SecondName', 'ThirdName', 'DateBirth', 'Address', 'Position', 'Department']
    '''Класс работника'''
    def __init__(self, Name = [], SecondName = [], ThirdName = [], Address = [], DateBirth = [], Position = [], Department = []):
        self.Dict = {}
        self.Dict['Name'] = Name
        self.Dict['SecondName'] = SecondName
        self.Dict['ThirdName'] = ThirdName
        self.Dict['DateBirth'] = DateBirth
        self.Dict['Address'] = Address
        self.Dict['Position'] = Position
        self.Dict['Department'] = Department
        self.rows = 0

    def show(self):
        if self.rows == 0:
            print(f'Сотрудников пока что еще не занесено в базу')
            return False
        print(f'____________________')
        for i in range(self.rows):
            print(f'id:{i}')
            self.printEmployee(i)
            print(f'____________________')

    def __rows_setter(self):
        self.rows = len(self.Dict['Name'])

    def __str__(self):
        return str(self.Dict)

    def printEmployee(self, id : int):
        if type(id) != int:
            print(f'Некорректные значения входных параметров')
            return False
        if id < 0 or id > self.rows-1:
            print(f'Неверный id. Такого количества элементов в базе нет или вы указываете отрицательный id.')
            return False
        try:
            print(f'Сотрудник:')
            for Attr in Employees.ATTRS:
                print(f'{Attr}: {self.Dict[Attr][id]}')
        except IndexError:
            print(f'Неверный id. Такого количества элементов в базе нет или вы указываете отрицательный id.')
            return False

    def findAttr(self, Attr : str, Name : str, a : list):
        '''Attr - атрибут из списка Employees.ATTRS, по которому искать. Name - что искать. a - id, которые просмотреть.
        Возвращает глабольные id.'''
        if Attr not in Employees.ATTRS:
            print('Такого атрибута не существует')
            return False

        b = []
        if a == False:
            return False
        else:
            for x in a:
                if self.Dict[Attr][x] == Name:
                    b.append(x)

        if not b:
            print('Сотрудника с таким Именем нет в базе.')
            return False
        else:
            return b

    def filterAttr(self, Attr : str, Name : str):
        '''Attr - атрибут из списка Employees.ATTRS, по которому искать. Name - что искать.
        Возвращает глобальные id'''

        if Attr == 'Department':
            print(f'Данный метод не обрабатывает атрибут Department')
            return False

        if Attr not in Employees.ATTRS:
            print('Такого атрибута не существует')
            return False

        a = []
        bi = 0

        if Name in self.Dict[Attr][0:1]:
            a.append(0)

        while True:
            if Name in self.Dict[Attr][bi + 1:]:
                i = self.Dict[Attr][bi + 1:].index(Name)
                bi += i + 1
                a.append(bi)
            else:
                break

        if not a:
            print(f'Сотрудников с таким {Attr} нет в базе.')
            return False
        else:
            return a

    def printByFilter(self, Attr : str, Name : str):
        a = self.filterAttr(Attr, Name)
        if a == False:
            return False
        print("____________________")
        for x in a:
            self.printEmployee(x)
            print("____________________")


    def __deleteEmployee(self, id : int):
        try:
            print(f'Сотрудник:')
            for Attr in Employees.ATTRS:
                print(f'{Attr}: {self.Dict[Attr][id]}')
                self.Dict[Attr].pop(id)
            print(f'был успешно удален.')
            self.rows -= 1
        except IndexError:
            print(f'Неверный id сотрудника. Такого количества элементов в базе нет или вы указываете отрицательный id.')
            return False

    def __notValidDateBirth(self, DateBirth : str):
        '''Проверка соответствует ли дата формату xx.yy.zzzz
        Реализуем с помощью регулярного выражения \d\d\.\d\d\.\d{4}'''
        # '''Проверка соответствует ли дата формату xx.yy.zzzz
        # xx - int < 31. yy - int < 12. zzzz - int < (текущий год - 16 лет)'''
        C = re.search(r'\d\d\.\d\d\.\d{4}', DateBirth)
        if not C:
            return True
        try:
            now = datetime.datetime.now() # текущее время
            xx = int(DateBirth[0:2])
            yy = int(DateBirth[3:5])
            zzzz = int(DateBirth[6:])
            if xx > 31 or xx < 0 or yy > 12 or yy < 0 or zzzz > now.year or zzzz < 1900:
                return True
        except ValueError:
            return True

        return False

    # def notValidDateBirth(self, DateBirth : str):
    #     '''Проверка соответствует ли дата формату xx.yy.zzzz
    #     Реализуем с помощью регулярного выражения \d\d\.\d\d\.\d{4}'''
    #     # '''Проверка соответствует ли дата формату xx.yy.zzzz
    #     # xx - int < 31. yy - int < 12. zzzz - int < (текущий год - 16 лет)'''
    #     if len(DateBirth) != 10:
    #         return True
    #     if DateBirth[2] != '.' or DateBirth[5] != '.':
    #         return True
    #     try:
    #         now = datetime.datetime.now() # текущее время
    #         xx = int(DateBirth[0:2])
    #         yy = int(DateBirth[3:5])
    #         zzzz = int(DateBirth[6:])
    #         if xx > 31 or xx < 0 or yy > 12 or yy < 0 or zzzz > now.year or zzzz < 1900:
    #             return True
    #     except ValueError:
    #         return True
    #
    #     return False

    def addEmployee(self, Name : str, SecondName : str, ThirdName : str, Address : str, DateBirth : str, Position : str):
        # try:
        #     Name = str(Name)
        #     SecondName = str(SecondName)
        #     ThirdName =str(ThirdName)
        #     Address = str(Address)
        #     DateBirth = str(DateBirth)
        # except ValueError:
        #     return False
        if type(Name) != str:
            print(f'Некорректный ввод для атрибута Name.')
            return False
        if Name == '':
            print('Некорректное значение атриббута Name')
            return False
        if type(SecondName) != str:
            print(f'Некорректный ввод для атрибута SecondName.')
            return False
        if SecondName == '':
            print('Некорректное значение атриббута SecondName')
            return False
        if type(ThirdName) != str:
            print(f'Некорректный ввод для атрибута ThirdName.')
            return False
        if ThirdName == '':
            print('Некорректное значение атриббута ThirdName')
            return False

        if type(Address) != str:
            print(f'Некорректный ввод для атрибута Address.')
            return False
        if Address == '':
            print('Некорректное значение атриббута Address')
            return False

        if DateBirth == '' or self.__notValidDateBirth(DateBirth):
            print('Некорректное значение атриббута DateBirth')
            return False

        self.Dict['Name'].append(Name)
        self.Dict['SecondName'].append(SecondName)
        self.Dict['ThirdName'].append(ThirdName)
        self.Dict['Address'].append(Address)
        self.Dict['DateBirth'].append(DateBirth)
        self.Dict['Position'].append(Position)
        self.Dict['Department'].append([])
        self.rows += 1
        self.printEmployee(self.rows-1)
        print(f'был успешно добавлен.')

    def idByAttrs(self, Name : str, SecondName : str, ThirdName : str, Address : str, DateBirth : str, Position : str):
        a = self.filterAttr('Name', Name)
        a = self.findAttr('SecondName',SecondName,a)
        a = self.findAttr('ThirdName',ThirdName,a)
        a = self.findAttr('Address',Address,a)
        a = self.findAttr('DateBirth', DateBirth,a)
        a = self.findAttr('Position', Position,a)
        if type(a) == bool:
            print(f'Что-то пошло не так в функции idByAttrs')
            return False
        else:
            a = int(a[0])
            print(a)
            return a

    def resetDepartments(self):
        '''Очищает принадлежность всех сотрудников к отделам'''
        for i in range(self.rows):
            self.Dict['Department'][i] = []

    def addDepartmentToEmployee(self, id:int, Department : str):
        '''id - все понятно с ним. Department - Name департмента'''
        self.Dict['Department'][id].append(Department)

    def delDepartmentFromEmployee(self, id:int, Department : str):
        '''id - все понятно с ним. Department - Name департмента'''
        index = self.Dict['Department'][id].index(Department)
        self.Dict['Department'][id].pop(index)

    def writeToJSON(self, filename):
        try:
            filename += '.emp'
            with open(filename, 'w') as file:
                json.dump(self.Dict, file)
        except FileNotFoundError:
            print(f'Не найдено файла {filename}.')


    def loadFromJSON(self, filename):
        try:
            filename += '.emp'
            with open(filename, 'r') as file:
                self.Dict = json.load(file)
            self.__rows_setter()
        except:
            print(f'Не найдено файла {filename}.')


class Departments():
    '''Класс, отвечающий за все отделы'''

    ATTRS = ['Name', 'Rooms', 'Employees']

    def __init__(self,Es : Employees, Name = [], EmpCount = [], Rooms = []):
        self.Es = Es
        self.Dict = {}
        self.Dict['Name'] = []
        self.Dict['Rooms'] = []
        self.Dict['Employees'] = []
        self.rows = 0

    def __rows_setter(self):
        self.rows = len(self.Dict['Name'])

    def printDepartment(self, id : int):
        try:
            print(f'Отдел:')
            for Attr in Departments.ATTRS:
                print(f'{Attr}: {self.Dict[Attr][id]}')
        except IndexError:
            print(f'Неверный id отдела. Такого количества элементов в базе нет или вы указываете отрицательный id.')
            return False

    def show(self):
        if self.rows == 0:
            print(f'Отделов пока что еще не занесено в базу')
            return False
        print(f'____________________')
        for i in range(self.rows):
            print(f'id:{i}')
            self.printDepartment(i)
            print(f'____________________')

    def addDepartment(self, Name : str, Rooms : list, Employees : list):
        '''Name - название отдела. Rooms - список из str с названиями комнат(почему не int, потому что может быть 'комната 200а, 205б и т.п.').
        Employees - список из int содержащий id. Es - база с со всеми сотрудниками, в которую вносить изменения.'''
        if type(Name) != str:
            print(f'Некорректный ввод для атрибута Name.')
            return False
        if Name == '':
            print(f'Название отдела не может быть пустым.')
            return False
        if type(Rooms) != list:
            print(f'Некорректный ввод для атрибута Rooms.')
            return False
        if Rooms == []:
            print(f'Отдел не может существовать без помещений.')
            return False
        if type(Employees) != list:
            print(f'Некорректный ввод для атрибута Employees.')
            return False
        if Employees == []:
            print(f'Отдел не может состоять из 0 сотрудников.')
            return False
        # Возможно чек валидности id не такой оптмиальный и стоит его совместить с циклом ниже, но зато просто и работает
        if max(Employees) > self.Es.rows or min(Employees) < 0:
            print(f'Некоррекное значение id сотрудника в списке Employees.\nСотрудника с таким id нет.')
            return False

        self.Dict['Name'].append(Name)
        self.Dict['Rooms'].append(Rooms)
        self.Dict['Employees'].append(Employees)
        self.Dict['Employees'][self.rows].sort()
        self.rows += 1
        # после того, как добавили информацию о сотрудников в отдел
        # занесем изменения в Employees
        for id in Employees:
            self.Es.addDepartmentToEmployee(id,Name)

        self.printDepartment(self.rows-1)
        print(f'был успешно добавлен.')

    def filterAttr(self, Attr, Name):
        '''Attr - атрибут из списка Employees.ATTRS, по которому искать. Name - что искать.
        Возвращает глобальные id. Работает только с атрибутом Name(пока что(собственно другого и не надо))'''

        if Attr not in Departments.ATTRS:
            print('Такого атрибута не существует')
            return False

        a = []
        bi = 0

        if Name in self.Dict[Attr][0:1]:
            a.append(0)

        while True:
            if Name in self.Dict[Attr][bi + 1:]:
                i = self.Dict[Attr][bi + 1:].index(Name)
                bi += i + 1
                a.append(bi)
            else:
                break

        if not a:
            print(f'Отделов с таким {Attr} нет в базе.')
            return False
        else:
            return a

    def __checkIDValid(self, idE:int, idD:int):
        '''Проверка валидности индексов'''
        if type(idE) != int or type(idD) != int:
            print(f'Некорректные значения входных параметров')
            return False
        if idE in self.Dict['Employees'][idD] == False:
            print(f'Сотрудник с id:{idE} не числится в этом отделе.')
            return False
        if idD < 0 or idD > self.rows-1:
            print(f'Отдела с таким id:{idD} нет в базе.')
            return False

    def addEmployeetoDepartment(self, idE : int, idD : int):
        if type(idE) != int or type(idD) != int:
            print(f'Некорректные значения входных параметров')
            return False
        if idD < 0 or idD > self.rows-1:
            print(f'Отдела с таким id:{idD} нет в базе.')
            return False
        if idE < 0 or idE > self.Es.rows-1:
            print(f'Сотрудника с таким id:{idE} нет в базе.')
            return False
        # Проверим, находится ли сотрудник уже в отделе
        if idE in self.Dict['Employees'][idD]:
            print(f'Сотрудник уже находится в отделе')
            return False
        self.Dict['Employees'][idD].append(idE)
        self.Dict['Employees'][idD].sort()
        DepName = self.Dict['Name'][idD]
        self.Es.Dict['Department'][idE].append(DepName)

    def delEmployeefromDepartment(self, idE : int, idD : int):
        if self.__checkIDValid(idE, idD) == False:
            return False
        # Сначала удаляем id сотрудника(idE) из списка сотрудиников отдела с id: idD
        index = self.Dict['Employees'][idD].index(idE)
        # print(f'index={index}')
        self.Dict['Employees'][idD].pop(index)

        # Теперь надо удалить запись об отделе у сотрудниками
        DepName = self.Dict['Name'][idD]
        # print(f'Depname={DepName}')
        index = self.Es.Dict['Department'][idE].index(DepName)
        self.Es.Dict['Department'][idE].pop(index)

    def delDepartment(self, idD : int):
        if type(idD) != int:
            print(f'Некорректные значения входных параметров')
            return False
        if idD < 0 or idD > self.rows-1:
            print(f'Отдела с таким id:{idD} нет в базе.')
            return False
        # Сначала трем информацию у сотрудников
        for id in self.Dict['Employees'][idD]:
            self.Es.delDepartmentFromEmployee(id,self.Dict['Name'][idD])

        self.printDepartment(idD)

        # Теперь трем информацию в отделах
        self.Dict['Name'].pop(idD)
        self.Dict['Rooms'].pop(idD)
        self.Dict['Employees'].pop(idD)
        self.rows -=1
        print(f'был успешно удален.')

    def writeToJSON(self, filename):
        try:
            filename += '.dep'
            with open(filename, 'w') as file:
                json.dump(self.Dict, file)
        except FileNotFoundError:
            print(f'Не найдено файла {filename}.')


    def loadFromJSON(self, filename):
        try:
            filename += '.dep'
            with open(filename, 'r') as file:
                self.Dict = json.load(file)
            self.__rows_setter()
        except:
            print(f'Не найдено файла {filename}.')

def deleteEmployee(idE : int, Es : Employees, Ds : Departments):
    '''Функция удаляет сотрудника.
    Функция вынесена сюда из класса Employees. Одноименный метод в классе Employees больше не используется'''
    if type(idE) is int == False:
        print(f'Некорректный ввод id сотрудника или список сотрудников пуст.')
    if idE < 0 or idE > Es.rows-1:
        print(f'Такого id сотрудника не существует.')
        return False

    print(f'Сотрудник:')
    # Трем сначала записи о сотрудниках у каждого отдела
    buffer = copy.deepcopy(Es.Dict['Department'][idE])
    for DepName in buffer:
        # print(f'Deps={Es.Dict["Department"][idE]}')
        # print(f'DepName={DepName}')
        idD = Ds.filterAttr('Name',DepName)[0]
        # print(f'idD={idD}')
        Ds.delEmployeefromDepartment(idE,idD)
        # Смещаем айди записей сотрудников у отделов. У самих сотрудников(у класса Employees) индексы автоматически уменьшатся после работы функции.
        # Уменьшаем индекс на 1 у тех сотрудников id которых расположен правее(то есть больше), чем id удаляемого сотрудника idE.
        Ds.Dict['Employees'][idD] = list(map(lambda x: x-1 if x > idE else x,  Ds.Dict['Employees'][idD]))

    # Теперь трем запись сотрудника
    for Attr in Employees.ATTRS:
        print(f'{Attr}: {Es.Dict[Attr][idE]}')
        Es.Dict[Attr].pop(idE)
    print(f'был успешно удален.')
    Es.rows -= 1
