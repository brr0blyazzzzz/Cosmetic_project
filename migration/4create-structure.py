from yoyo import step

depends = {}

steps = [
    step('''CREATE TABLE structure (
        structure_id SERIAL PRIMARY KEY,
        structure_name VARCHAR(255) NOT NULL,
        CONSTRAINT structure_check CHECK (structure_name <> ''),
        CONSTRAINT structure_unique UNIQUE (structure_name)
    )''')
]
