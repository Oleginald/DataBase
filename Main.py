from Lib import *

def main():

    filename = 'DATABASE'
    Es = Employees()
    Ds = Departments(Es)
    print('База данных "Итоговая аттестация v.1337"')
    while True:
        uinput = input()

        if uinput in COMMANDS:
            if uinput == 'exit':
                sys.exit()

            if uinput == 'commands':
                print(COMMANDS)

            if uinput == 'doc':
                doc()

            if uinput == 'load':
                Es.loadFromJSON(filename)
                Ds.loadFromJSON(filename)

            if uinput == 'save':
                Es.writeToJSON(filename)
                Ds.writeToJSON(filename)

            if uinput == 'path':
                print(f'Введите название файла: ', end='')
                filename = input()

            if uinput == 'path -curr':
                print(filename)





            if uinput == 'number -E':
                print(Es.rows)

            if uinput == 'show -E':
                Es.show()

            if uinput == 'add -e':
                a = userInputE()
                Es.addEmployee(a[0],a[1],a[2],a[3],a[4],a[5])

            if uinput == 'findid -e':
                a = userInputE()
                a.pop()
                Es.idByAttrs(a[0],a[1],a[2],a[3],a[4],a[5])

            if uinput == 'del -e':
                print(f'Введите id: ', end='')
                try:
                    idE = int(input())
                    deleteEmployee(idE, Es, Ds)
                except ValueError:
                    print(f'Некорректный ввод id')

            if uinput == 'show -e':
                print(f'Введите id: ', end='')
                try:
                    id = int(input())
                    Es.printEmployee(id)
                except ValueError:
                    print(f'Некорректный ввод id')

            if uinput == 'filt -e':
                print(f'Введите Атрибут: ', end='')
                Attr = input()
                print(f'Введите Фильтр: ', end='')
                Filter = input()
                try:
                    a = Es.filterAttr(Attr, Filter)
                    for id in a:
                        Es.printEmployee(id)
                except TypeError:
                    print(f'', end='')





            if uinput == 'number -D':
                print(Ds.rows)

            if uinput == 'show -D':
                Ds.show()

            if uinput == 'add -d':
                a = userInputD()
                Ds.addDepartment(a[0],a[1],a[2])

            if uinput == 'findid -d':
                print(f'Введите Name отдела: ', end='')
                try:
                    Name = input()
                    print(Ds.filterAttr('Name',Name)[0])
                except TypeError:
                    print(f'',end='')

            if uinput == 'del -d':
                print(f'Введите id: ', end='')
                try:
                    idD = int(input())
                    Ds.delDepartment(idD)
                except ValueError:
                    print(f'Некорректный ввод id')

            if uinput == 'show -d':
                print(f'Введите id: ', end='')
                try:
                    id = int(input())
                    Ds.printDepartment(id)
                except ValueError:
                    print(f'Некорректный ввод id')

            if uinput == 'add -ed':
                try:
                    print(f'Введите idE: ', end='')
                    idE = int(input())
                    print(f'Введите idD: ', end='')
                    idD = int(input())
                    Ds.addEmployeetoDepartment(idE, idD)
                    print(f'Сотрудник с idE:{idE}')
                    print(f'успешно добавлен к отделу: {Ds.Dict["Name"][idD]}.')
                except ValueError:
                    print(f'Некорректный ввод id')

            if uinput == 'del -ed':
                try:
                    print(f'Введите idE: ', end='')
                    idE = int(input())
                    print(f'Введите idD: ', end='')
                    idD = int(input())
                    Ds.delEmployeefromDepartment(idE,idD)
                    print(f'Сотрудник с idE:{idE}')
                    print(f'успешно удален из отдела: {Ds.Dict["Name"][idD]}.')
                except ValueError:
                    print(f'Некорректный ввод id. Сотрудника с таким idE нет в отделе с idD')

        else:
            print(f'Такой КОМАНДЫ не существует.')

if __name__ == '__main__':
    main()
