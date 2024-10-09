from yoyo import step

depends = {'2create-product', '4create-structure'}

steps = [
    step('''
    CREATE TABLE product_structure (
        product_id INT NOT NULL,
        structure_id INT NOT NULL,
        quantity NUMERIC(3 , 2) CHECK (quantity > 0 AND quantity <= 1),
        PRIMARY KEY (product_id, structure_id),
        FOREIGN KEY (product_id) REFERENCES Product(product_id),
        FOREIGN KEY (structure_id) REFERENCES Structure(structure_id)
    )
    ''')
]