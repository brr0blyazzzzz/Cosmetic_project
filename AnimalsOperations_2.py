import psycopg2
class AnimalTree:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname="animals",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
        )
        self.cursor = self.conn.cursor()

    def add_leaf(self, parent_id, name, description):
        if parent_id is not None:
            self.cursor.execute("SELECT path FROM animals_2 WHERE id = %s", (parent_id,))
            parent_path = self.cursor.fetchone()
            if parent_path:
                new_path = f"{parent_path[0]}"
            else:
                new_path = "1/"
        else:
            new_path = "1/"
        self.cursor.execute(
            "INSERT INTO animals_2 (name, description, path) VALUES (%s, %s, %s) RETURNING id",
            (name, description, new_path)
        )
        new_id = self.cursor.fetchone()[0]
        final_path = f"{new_path}{new_id}/"
        self.cursor.execute(
            "UPDATE animals_2 SET path = %s WHERE id = %s",
            (final_path, new_id)
        )
        self.conn.commit()

    def delete_leaf(self, leaf_id):
        self.cursor.execute("DELETE FROM animals_2 WHERE id = %s", (leaf_id,))
        self.conn.commit()

    def delete_subtree(self, parent_id):
        self.cursor.execute("SELECT path FROM animals_2 WHERE id = %s", (parent_id,))
        parent_path = self.cursor.fetchone()

        if parent_path:
            path_pattern = f"{parent_path[0]}%"
            self.cursor.execute("DELETE FROM animals_2 WHERE path LIKE %s", (path_pattern,))
            self.conn.commit()

    def delete_node_with_subtree(self, node_id):
        self.cursor.execute("SELECT path FROM animals_2 WHERE id = %s", (node_id,))
        current_path = self.cursor.fetchone()

        if current_path is not None:
            self.cursor.execute("DELETE FROM animals_2 WHERE path LIKE %s", (f"{current_path[0]}%",))

        self.conn.commit()

    def get_direct_children(self, parent_id):
        self.cursor.execute("SELECT path FROM animals_2 WHERE id = %s", (parent_id,))
        parent_path = self.cursor.fetchone()
        if parent_path:
            parent_path = parent_path[0]
            path_pattern = f"{parent_path}%"
            self.cursor.execute("SELECT * FROM animals_2 WHERE path LIKE %s", (path_pattern,))
            return self.cursor.fetchall()

        return []

    def get_element(self, node_id):
        self.cursor.execute("SELECT * FROM animals_2 WHERE id = %s", (node_id,))
        return self.cursor.fetchone()

    def get_direct_parent(self, node_id):
        self.cursor.execute("SELECT path FROM animals_2 WHERE id = %s", (node_id,))
        node_path = self.cursor.fetchone()

        if node_path:
            node_path = node_path[0]
            last_slash_index = node_path.rfind('/')
            node_path = node_path[:last_slash_index]
            last_slash_index = node_path.rfind('/')
            node_path = node_path[:last_slash_index]
            if last_slash_index != -1:
                parent_path = node_path[:last_slash_index] + '/'
                self.cursor.execute("SELECT * FROM animals_2 WHERE path = %s", (parent_path,))
                return self.cursor.fetchone()

        return None

    def get_all_descendants(self, node_id):
        descendants = []
        self.cursor.execute("SELECT path FROM animals_2 WHERE id = %s", (node_id,))
        current_path = self.cursor.fetchone()

        if current_path is not None:
            path_prefix = current_path[0]
            self.cursor.execute("SELECT * FROM animals_2 WHERE path LIKE %s", (f"{path_prefix}%",))
            all_descendants = self.cursor.fetchall()

            for descendant in all_descendants:
                descendant_path = descendant[3]
                if descendant_path != path_prefix:
                    level = descendant[3].count('/') - path_prefix.count('/')
                    descendants.append((descendant, level))

        return descendants

    def get_all_ancestors(self, node_id):
        ancestors = []
        self.cursor.execute("SELECT path FROM animals_2 WHERE id = %s", (node_id,))
        current_path_result = self.cursor.fetchone()

        if current_path_result is None:
            print(f"No node found with id {node_id}")
            return ancestors

        current_path = current_path_result[0]
        self.cursor.execute("SELECT * FROM animals_2 WHERE %s LIKE CONCAT(path, '%%')", (current_path,))
        all_ancestors = self.cursor.fetchall()

        for ancestor in all_ancestors:
            ancestor_path = ancestor[3]
            if ancestor_path != current_path:
                level = ancestor[3].count('/') - current_path.count('/')
                ancestors.append((ancestor, level))

        return ancestors

    def close(self):
        self.cursor.close()
        self.conn.close()
def get_valid_int(prompt):
    while True:
        conn = psycopg2.connect(
            dbname="animals",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        user_input = input(prompt).strip()
        if user_input.isdigit():
            num = int(user_input)
            if num > 0:
                cursor.execute("SELECT COUNT(*) FROM animals_2 WHERE id = %s", (num,))
                exists = cursor.fetchone()[0] > 0
                if exists:
                    return num
                else:
                    print("Такого числа не существует в базе данных.")
            else:
                print("Пожалуйста, введите корректное положительное целое число.")
        else:
            print("Пожалуйста, введите корректное положительное целое число.")
        cursor.close()
        conn.close()

def get_valid_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Ввод не может быть пустым или состоять только из пробелов. Пожалуйста, попробуйте снова.")

def main():
    animal_tree = AnimalTree(dbname="animals", user="postgres", password="root", host="localhost", port="5432")

    while True:
        print("Меню:")
        print("1. Добавить животное")
        print("2. Удалить узел по ID")
        print("3. Удалить поддерево по ID родителя")
        print("4. Удалить узел без поддерева по ID узла")
        print("5. Получить прямых детей по ID родителя")
        print("6. Получить прямого родителя по ID узла")
        print("7. Получить всех потомков по ID узла")
        print("8. Получить всех предков по ID узла")
        print("9. Выход")
        user_input = input("Выберите действие: ").strip()
        if user_input.isdigit():
            choice = int(user_input)
        if choice == 1:
            parent_id = get_valid_int("Введите ID родителя: ")
            name = get_valid_input("Введите имя животного: ")
            description = get_valid_input("Введите описание животного: ")
            animal_tree.add_leaf(parent_id, name, description)
            print("Животное добавлено.")

        elif choice == 2:
            leaf_id = get_valid_int("Введите ID узла для удаления: ")
            animal_tree.delete_leaf(leaf_id)
            print("Узел удален.")

        elif choice == 3:
            parent_id = get_valid_int("Введите ID родителя для удаления поддерева: ")
            animal_tree.delete_subtree(parent_id)
            print("Поддерево удалено.")

        elif choice == 4:
            leaf_id = get_valid_int("Введите ID узла для удаления: ")
            animal_tree.delete_node_with_subtree(leaf_id)
            print("Узел удален.")

        elif choice == 5:
            parent_id = get_valid_int("Введите ID родителя для получения детей: ")
            children = animal_tree.get_direct_children(parent_id)
            if children:
                print("Исходный узел: " + f"'{children[0][0]}', " + f"{children[0][1]}, " + f"{children[0][2]}, " + f""
                                                                                                            f"{children[0][3]}")
                children.pop(0)
                print("Прямые дети:")
                for child in children:
                    print(f"'{child[0]}', '{child[2]}', '{child[3]}'")
            else:
                print("У данного родителя нет детей.")

        elif choice == 6:
            node_id = get_valid_int("Введите ID узла для получения родителя: ")
            parent = animal_tree.get_direct_parent(node_id)
            print("Прямой родитель:", parent)

        elif choice == 7:
            node_id = get_valid_int("Введите ID узла для получения потомков: ")
            descendants = animal_tree.get_all_descendants(node_id)
            result = animal_tree.get_element(node_id)

            print(f"Исходный узел: {result}")
            print("Все потомки:")
            for descendant, level in descendants:
                print(f"'{descendant[0]}'" + " " * (level * 4) + f"'{descendant[1]}','{descendant[2]}'")

        elif choice == 8:
            node_id = get_valid_int("Введите ID узла для получения предков: ")
            ancestors = animal_tree.get_all_ancestors(node_id)
            result = animal_tree.get_element(node_id)
            print(f"Исходный узел: {result}")
            print("Все предки:")
            for ancestor, level in ancestors:
                print(f"'{ancestor[0]}'" + " " *(abs(level + 4) * 4) + f"'{ancestor[1]}', '{ancestor[2]}'")

        elif choice == 9:
            break

        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

    animal_tree.close()


if __name__ == "__main__":
    main()