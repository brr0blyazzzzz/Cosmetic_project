"""
INSERT INTO Structure
"""

from yoyo import step

__depends__ = {}

steps = [
    step(''' 
INSERT INTO Structure (structure_id,structure_name) VALUES
(1,'aqua'),
(2,'cetearyl alcohol'),
(3,'talc'),
(4,'capric triglyceride'),
(5,'glycerin'),
(6,'palm oil'),
(7,'parfum'),
(8,'sorbitol'),
(9,'methyl paraben'),
(10,'Ceramide AP')''')
]

