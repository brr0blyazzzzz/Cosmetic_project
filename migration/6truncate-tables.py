from yoyo import step

depends = {}

steps = [
    step('''
         TRUNCATE TABLE manufacturer CASCADE;
         TRUNCATE TABLE product CASCADE;
         TRUNCATE TABLE product_instance CASCADE;
         TRUNCATE TABLE structure CASCADE;
         TRUNCATE TABLE product_structure CASCADE;
         ''')
]
