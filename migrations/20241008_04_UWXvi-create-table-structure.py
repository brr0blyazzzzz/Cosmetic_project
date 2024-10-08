"""
CREATE TABLE Structure
"""

from yoyo import step

__depends__ = {}

steps = [
    step('''CREATE TABLE Structure (
    structure_id SERIAL PRIMARY KEY,
    structure_name VARCHAR(255) NOT NULL
)'''
)
]
