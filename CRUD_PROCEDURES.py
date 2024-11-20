import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
def add_manufacturer():
    title_country = input("Введите название страны производителя: ")
    address_of_manufacturer = input("Введите адрес производителя: ")
    contact_list = input("Введите контактный список: ")

    try:
        cursor.execute("CALL add_manufacturer(%s, %s, %s)", (title_country, address_of_manufacturer, contact_list))
        conn.commit()
        print("Производитель успешно добавлен.")
    except Exception as e:
        conn.rollback()
        print(e)

def get_all_manufacturers():
    cursor.execute("SELECT * FROM get_all_manufacturers()")
    rows = cursor.fetchall()
    max_lengths = [0] * len(rows[0])

    for row in rows:
        for i, value in enumerate(row):
            max_lengths[i] = max(max_lengths[i], len(str(value)))
    format_string = " ".join(["{:<" + str(length + 3) + "}" for length in max_lengths])
    for row in rows:
        print(format_string.format(*row))

def get_manufacturer_by_id():
    manufacturer_id = input("Введите ID производителя: ")

    try:
        cursor.execute("SELECT * FROM get_manufacturer_by_id(%s)", (manufacturer_id,))
        result = cursor.fetchone()

        if result:
            print("{:<20} {}".format("manufacturer_id:", result[0]))
            print("{:<20} {}".format("title_country:", result[1]))
            print("{:<20} {}".format("address:", result[2]))
            print("{:<20} {}".format("contact_list:", result[3]))



        else:
            print(f"Manufacturer with ID {manufacturer_id} not found.")

    except Exception as e:
        conn.rollback()
        print(e)


def update_manufacturer():
    manufacturer_id = input("Введите ID производителя для обновления: ")
    new_title_country = input("Введите новое название страны: ")
    new_address_of_manufacturer = input("Введите новый адрес: ")
    new_contact_list = input("Введите новый контактный список: ")

    try:
        cursor.execute("CALL update_manufacturer(%s, %s, %s, %s)",
                       (manufacturer_id.strip(), new_title_country, new_address_of_manufacturer, new_contact_list))
        conn.commit()
        print("Производитель успешно обновлен.")

    except Exception as e:
        conn.rollback()
        print(e)


def delete_manufacturer():
    manufacturer_id = input("Введите ID производителя для удаления: ")
    try:
        cursor.execute("CALL delete_manufacturer(%s)", (manufacturer_id.strip(),))
        conn.commit()
        print("Производитель успешно удален.")
    except Exception as e:
        conn.rollback()
        print(f"Произошла ошибка: {e}")


def delete_manufacturers():
    ids_input = input("Введите ID производителей для удаления через пробел: ")

    ids = ids_input.split()

    try:
        cursor.execute("SELECT delete_list_of_manufacturers(%s)", (ids,))
        deleted_count = cursor.fetchone()[0]
        conn.commit()
        print(f"Удалено производителей: {deleted_count}")
    except Exception as e:
        conn.rollback()
        print(e)

def menu():
    while True:
        print(" Выберите действие:")
        print("1. Добавить производителя")
        print("2. Вывести всех производителей")
        print("3. Вывести производителя по ID")
        print("4. Изменить производителя по ID")
        print("5. Удалить производителя по ID")
        print("6. Удалить список производителей")
        print("7. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            add_manufacturer()
        elif choice == '2':
            get_all_manufacturers()
        elif choice == '3':
            get_manufacturer_by_id()
        elif choice == '4':
            update_manufacturer()
        elif choice == '5':
            delete_manufacturer()
        elif choice == '6':
            delete_manufacturers()
        elif choice == '7':
            break
        else:
            print("Некорректный выбор, попробуйте еще раз.")


menu()

cursor.close()
conn.close()

