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
        self.cursor.execute(
            "INSERT INTO animals (parent_id, name, description) VALUES (%s, %s, %s)",
            (parent_id, name, description)
        )
        self.conn.commit()

    def delete_leaf(self, leaf_id):
        self.cursor.execute("DELETE FROM animals WHERE id = %s", (leaf_id,))
        self.conn.commit()

    def delete_subtree(self, parent_id):
        self.cursor.execute("DELETE FROM animals WHERE parent_id = %s", (parent_id,))
        self.cursor.execute("DELETE FROM animals WHERE id = %s", (parent_id,))
        self.conn.commit()

    def delete_node_with_subtree(self, node_id):
        self.cursor.execute(
            "SELECT parent_id FROM animals WHERE id = %s",
            (node_id,)
        )
        current_parent = self.cursor.fetchone()

        if current_parent is not None:
            current_parent_id = current_parent[0]
            self.cursor.execute(
                "UPDATE animals SET parent_id = %s WHERE parent_id = %s",
                (current_parent_id, node_id)
            )
        self.cursor.execute(
            "DELETE FROM animals WHERE id = %s",
            (node_id,)
        )

        self.conn.commit()

    def get_direct_children(self, parent_id):
        self.cursor.execute("SELECT * FROM animals WHERE parent_id = %s", (parent_id,))
        return self.cursor.fetchall()

    def get_element(self, node_id):
        self.cursor.execute("SELECT * FROM animals WHERE id = %s",
                            (node_id,))
        return self.cursor.fetchone()


    def get_direct_parent(self, node_id):
        self.cursor.execute("SELECT * FROM animals WHERE id = (SELECT parent_id FROM animals WHERE id = %s)",
                            (node_id,))
        return self.cursor.fetchone()

    def get_all_descendants(self, node_id):
        descendants = []

        def fetch_descendants(parent_id, level=0):
            self.cursor.execute("SELECT * FROM animals WHERE parent_id = %s", (parent_id,))
            children = self.cursor.fetchall()
            for child in children:
                descendants.append((child, level))
                fetch_descendants(child[0], level + 1)

        fetch_descendants(node_id)
        return descendants

    def get_all_ancestors(self, node_id):
        ancestors = []

        def fetch_ancestors(child_id, level=0):
            self.cursor.execute("SELECT * FROM animals WHERE id = (SELECT parent_id FROM animals WHERE id = %s)",
                                (child_id,))
            parent = self.cursor.fetchone()
            if parent:
                ancestors.append((parent, level))
                fetch_ancestors(parent[0], level + 1)

        fetch_ancestors(node_id)
        return ancestors

    def close(self):
        self.cursor.close()
        self.conn.close()


def get_valid_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Ввод не может быть пустым или состоять только из пробелов. Пожалуйста, попробуйте снова.")


def get_valid_int(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit():
            num = int(user_input)
            if num > 0:
                return num
        print("Пожалуйста, введите корректное положительное целое число.")


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

        choice = get_valid_int("Выберите действие: ")

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
            print("Прямые дети:")
            for child in children:
                print(f"'{child[0]}', '{child[2]}','{child[3]}'")

        elif choice == 6:
            node_id = get_valid_int("Введите ID узла для получения родителя: ")
            parent = animal_tree.get_direct_parent(node_id)
            print("Прямой родитель:", parent)

        elif choice == 7:
            node_id = get_valid_int("Введите ID узла для получения потомков: ")
            descendants = animal_tree.get_all_descendants(node_id)
            result = animal_tree.get_element(node_id)
            print (f"Исходный узел: {result}")
            print("Все потомки:")
            for descendant, level in descendants:
                print(f"'{descendant[0]}'" + " " * (
                            level * 4) + f"'{descendant[2]}','{descendant[3]}'")
        elif choice == 8:
            node_id = get_valid_int("Введите ID узла для получения предков: ")
            ancestors = animal_tree.get_all_ancestors(node_id)
            result = animal_tree.get_element(node_id)
            print(f"Исходный узел: {result}")
            print("Все предки:")
            for ancestor, level in reversed(ancestors):
                print(f"'{ancestor[0]}'" + " " * (abs(level - 4) * 4) + f"'{ancestor[2]}', '{ancestor[3]}'")

        elif choice == 9:
            break

        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

    animal_tree.close()


if __name__ == "__main__":
    main()