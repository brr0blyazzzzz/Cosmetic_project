from yoyo import step

depends = {'20241008_01_NYt5H-create-table-product', '20241008_04_UWXvi-create-table-structure'}

steps = [
    step('''
    CREATE TABLE Product_Structure (
        product_id INT NOT NULL,
        structure_id INT NOT NULL,
        quantity NUMERIC(3 , 2) CHECK (quantity > 0 AND quantity < 1),
        PRIMARY KEY (product_id, structure_id),
        FOREIGN KEY (product_id) REFERENCES Product(product_id),
        FOREIGN KEY (structure_id) REFERENCES Structure(structure_id)
    )
    ''')
]


