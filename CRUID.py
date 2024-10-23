import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
def StructureCreate():
    data_to_insert = []

    while True:
        structure_name = input("Название (или нажмите Enter для завершения ввода): ")
        if structure_name.strip():
            data_to_insert.append(structure_name)
        else:
            if data_to_insert:
                break
            print("Название не может быть пустым. Пожалуйста, введите корректное название.")

    if data_to_insert:
        try:
            cursor.executemany("INSERT INTO Structure (structure_name) VALUES (%s)", [(name,) for name in data_to_insert])
            conn.commit()
            print("Данные успешно добавлены.")
        except Exception as e:
            conn.rollback()
            print(f"Ошибка при добавлении данных: {e}")
    else:
        print("Нет данных для добавления!")


def StructureRetrieveAll():
    cursor.execute("SELECT * FROM Structure")
    results = cursor.fetchall()
    if results:
        for result in results:
            print(result)
    else:
        print("Нет данных.")


def StructureRetrieve():
    id = input("Введите ID: ")
    if id and id.isdigit():
        cursor.execute("SELECT * FROM Structure WHERE structure_id = %s", (id,))
        result = cursor.fetchone()
        if result:
            print(result)
        else:
            print("Элемент с таким ID не найден.")
    else:
        print("ID не введен или введен некорректно.")


def StructureUpdate():
    id = input("Введите ID для обновления: ")
    if id and id.isdigit():
        structure_name = input("Введите новое название: ").strip()
        if not structure_name:
            print("Название не может быть пустым или состоять только из пробелов. Пожалуйста, введите корректное название.")
        else:
            try:
                cursor.execute("UPDATE Structure SET structure_name = %s WHERE structure_id = %s", (structure_name, id))
                if cursor.rowcount > 0:
                    conn.commit()
                    print("Данные успешно обновлены.")
                else:
                    print("Элемент с таким ID не найден.")
            except Exception as e:
                conn.rollback()
                print(f"Ошибка при обновлении данных: {e}")
    else:
        print("ID не введен или введен некорректно.")


def StructureDelete():
    id = input("Введите ID для удаления: ")
    if id and id.isdigit():
            cursor.execute("DELETE FROM Structure WHERE structure_id = %s", (id,))
            conn.commit()
            if cursor.rowcount > 0:
                print("Элемент успешно удален.")
            else:
                print("Элемент с таким ID не найден.")
    else:
        print("ID не введен или введен некорректно.")


def StructureDeleteAll():
    data = input("Введите ID через пробел для удаления: ")
    ids = list(map(str.strip, data.split()))
    if ids:
        for id in ids:
            if id.isdigit():
                try:
                    cursor.execute("DELETE FROM Structure WHERE structure_id = %s", (id,))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print(f"Элемент с ID {id} успешно удален.")
                    else:
                        print(f"Элемент с ID {id} не найден.")
                except Exception as e:
                    conn.rollback()
                    print(f"Ошибка при удалении данных: {e}")
    else:
        print("Нет данных для удаления!")

def menu():
    while True:
        print("Выберите действие:")
        print("1. Добавить элементы")
        print("2. Вывести все элементы")
        print("3. Вывести элемент по id")
        print("4. Изменить элемент по id")
        print("5. Удалить элемент по id")
        print("6. Удалить список элементов")
        print("7. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            StructureCreate()
        elif choice == '2':
            StructureRetrieveAll()
        elif choice == '3':
            StructureRetrieve()
        elif choice == '4':
            StructureUpdate()
        elif choice == '5':
            StructureDelete()
        elif choice == '6':
            StructureDeleteAll()
        elif choice == '7':
            break
        else:
            print("Некорректный выбор, попробуйте еще раз.")

menu()

cursor.close()
conn.close()
