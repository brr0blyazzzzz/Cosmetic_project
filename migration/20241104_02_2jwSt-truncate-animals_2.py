from yoyo import step

depends = {}

steps = [
    step('''
         TRUNCATE TABLE animals_2 CASCADE;
         ''')
]