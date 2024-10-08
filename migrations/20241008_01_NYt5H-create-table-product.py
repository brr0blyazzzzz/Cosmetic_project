"""
CREATE TABLE Product
"""

from yoyo import step

__depends__ = {'20241008_03_hqFJa-create-table-manufacturer'}

steps = [
    step(''' 
    CREATE TABLE Product (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    manufacturer_id INT not NULL,
    product_title VARCHAR(255) NOT NULL,
    FOREIGN KEY (manufacturer_id) REFERENCES Manufacturer(manufacturer_id)
    )'''
    )
]

