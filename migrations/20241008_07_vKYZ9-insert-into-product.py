"""
INSERT INTO Product
"""

from yoyo import step

__depends__ = {'20241008_06_A9fil-insert-into-manufacturer'}

steps = [
    step(''' 
INSERT INTO Product (product_id, product_name, manufacturer_id, product_title) VALUES
(1, 'Гидролаты растений', 1, 'Тоник для лица'),
(2, '18 colors expert', 2, 'Палетка теней для век'),
(3, 'Marvel', 3, 'Тушь для ресниц'),
(4, 'Ночной The Act', 4, 'Крем для лица'),
(5, 'Выравнивающий The Act', 4, 'Крем для век'),
(6, 'Дневной The Act', 4, 'Крем для лица'),
(7, 'More Therapy', 7, 'Бальзам для волос'),
(8, 'Суфле Сливочное', 8, 'Крем для лица'),
(9, 'Matte Color', 10, 'Карандаш для губ'),
(10, 'MISS DIOR PERFUME', 2, 'Крем для рук')''')
]

