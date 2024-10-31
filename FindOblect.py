import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()


def product_search(search_values, limit=5, offset=0):
    query = "SELECT * FROM Product "
    conditions = []
    params = []

    if search_values.get('product_name'):
        conditions.append("product_name ILIKE %s")
        params.append('%' + search_values['product_name'] + '%')

    if search_values.get('product_title'):
        conditions.append("product_title ILIKE %s")
        params.append('%' + search_values['product_title'] + '%')

    if search_values.get('manufacturer_ids'):
        manufacturer_ids = search_values['manufacturer_ids']
        if isinstance(manufacturer_ids, list) and manufacturer_ids:
            placeholders = ', '.join(['%s'] * len(manufacturer_ids))
            conditions.append(f"manufacturer_id IN ({placeholders})")
            params.extend(manufacturer_ids)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += " LIMIT %s OFFSET %s"
    params.append(limit)
    params.append(offset)

    cursor.execute(query, params)
    results = cursor.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print("Нет объектов, удовлетворяющих условиям поиска.")


while True:
    product_name = input("Введите product_name: ")
    product_title = input("Введите product_title: ")
    manufacturer_ids = input("Введите manufacturer_id: ")

    limit = input("Введите limit: ")
    offset = input("Введите offset: ")

    if limit.isdigit():
        limit = int(limit)
    else:
        limit = 5
        print("Параметр limit задан неверно. Параметр задан по умолчанию.")

    if offset.isdigit():
        offset = int(offset)
    else:
        offset = 0
        print("Параметр offset задан неверно. Параметр задан по умолчанию.")


    if manufacturer_ids.strip() == "":
        manufacturer_ids = None
    else:
        manufacturer_ids = [int(id.strip()) for id in manufacturer_ids.split(' ') if id.strip().isdigit()]

    search_values = {
        'product_name': product_name if product_name else None,
        'product_title': product_title if product_title else None,
        'manufacturer_ids': manufacturer_ids
    }

    product_search(search_values, limit=limit, offset=offset)

cursor.close()
conn.close()
