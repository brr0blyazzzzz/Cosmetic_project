
"""
CREATE TABLE product
"""

from yoyo import step

__depends__ = {'1create-manufacturer'}

steps = [
    step(''' 
    CREATE TABLE product (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    manufacturer_id INT not NULL,
    product_title VARCHAR(255) NOT NULL,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(manufacturer_id)
    )'''
    )
]

