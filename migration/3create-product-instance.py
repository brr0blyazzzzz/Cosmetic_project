
"""
CREATE TABLE Product_Instance
"""

from yoyo import step

__depends__ = {'2create-product'}

steps = [
    step('''
    CREATE TABLE Product_Instance (
    instance_id INT PRIMARY KEY,
    expiration_date DATE
)''')
]
