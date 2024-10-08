"""
CREATE TABLE Product_Instance
"""

from yoyo import step

__depends__ = {'20241008_01_NYt5H-create-table-product'}

steps = [
    step('''
    CREATE TABLE Product_Instance (
    instance_id INT PRIMARY KEY,
    expiration_date DATE
)''')
]

