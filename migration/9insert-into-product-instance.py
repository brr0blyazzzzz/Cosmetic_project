"""
INSERT INTO Product_Instance
"""

from yoyo import step

__depends__ = {'8insert-into-product'}

steps = [
    step(''' 
INSERT INTO Product_Instance (instance_id,expiration_date,product_id) VALUES
(1,'2027-05-01',1),
(2,'2026-05-20',2),
(3,'2026-10-05',3),
(4,'2026-02-07',4),
(5,'2026-12-14',5),
(6,'2026-02-14',6),
(7,'2025-05-14',7),
(8,'2025-10-12',8),
(9,'2029-07-16',9),
(10,'2027-10-09',10)
''')
]

