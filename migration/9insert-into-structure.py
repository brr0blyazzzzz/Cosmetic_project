"""
INSERT INTO Structure
"""

from yoyo import step

__depends__ = {}

steps = [
    step(''' 
INSERT INTO Structure (structure_name) VALUES
('aqua'),
('cetearyl alcohol'),
('talc'),
('capric triglyceride'),
('glycerin'),
('palm oil'),
('parfum'),
('sorbitol'),
('methyl paraben'),
('Ceramide AP')''')
]

