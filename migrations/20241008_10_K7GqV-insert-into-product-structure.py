"""
INSERT INTO Product_ Structure
"""

from yoyo import step

__depends__ = {'20241008_09_e0x3W-insert-into-structure','20241008_07_vKYZ9-insert-into-product'}

steps = [
    step(''' 
INSERT INTO Product_Structure (product_id, structure_id, quantity) VALUES
(2, 1, 0.67),
(2, 2, 0.33),
(3, 3, 0.87),
(5, 7, 0.09),
(7, 7, 0.11),
(12, 7, 0.21),
(8, 6, 0.12),
(11, 4, 0.15),
(4, 1, 0.34),
(6, 10, 0.11),
(2, 3, 0.01),
(14, 2, 0.23),
(15, 5, 0.01),
(16, 5, 0.10)''')
]
