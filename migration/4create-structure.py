"""
CREATE TABLE structure
"""

from yoyo import step

__depends__ = {}

steps = [
    step('''CREATE TABLE structure (
    structure_id SERIAL PRIMARY KEY,
    structure_name VARCHAR(255) NOT NULL
)'''
)
]
