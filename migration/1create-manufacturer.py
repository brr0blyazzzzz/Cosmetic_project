
"""
CREATE TABLE manufacturer
"""

from yoyo import step

__depends__ = {}

steps = [
    step('''
    CREATE TABLE manufacturer (
    manufacturer_id SERIAL PRIMARY KEY,
    title_country VARCHAR(255) NOT NULL,
    address_of_manufacturer TEXT NOT NULL,
    contact_list TEXT NOT NULL
)
         ''')
]

