"""
CREATE TABLE Product_ Structure
"""

from yoyo import step

__depends__ = {'20241008_01_NYt5H-create-table-product', '20241008_04_UWXvi-create-table-structure'}

steps = [
    step('''
    CREATE TABLE Product_Structure (
    product_id INT not NULL,
    structure_id INT not NULL,
    quantity NUMERIC(1,10),
    PRIMARY KEY (product_id, structure_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id),
    FOREIGN KEY (structure_id) REFERENCES Structure(structure_id)
)''')
]

