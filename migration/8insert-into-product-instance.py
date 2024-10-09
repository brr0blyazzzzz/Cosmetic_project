"""
INSERT INTO Product_Instance
"""

from yoyo import step

__depends__ = {'7insert-into-product'}

steps = [
    step(''' 
INSERT INTO Product_Instance (instance_id, expiration_date) VALUES
(1, '2027-05-01'),
(2, '2026-05-20'),
(3, '2026-10-05'),
(4, '2026-02-07'),
(5, '2026-12-14'),
(6, '2026-02-14'),
(7, '2025-05-14'),
(8, '2020-09-12'),
(9, '2029-07-16'),
(10, '2027-10-09')''')
]

