
"""
CREATE TABLE product_instance
"""

from yoyo import step

__depends__ = {'2create-product'}

steps = [
    step('''
    CREATE TABLE product_instance (
    instance_id INT PRIMARY KEY,
    expiration_date DATE NOT NULL CHECK (expiration_date > CURRENT_DATE),
    product_id INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(product_id)
)''')
]
