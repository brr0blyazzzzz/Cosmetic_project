from yoyo import step

depends = {}

steps = [
    step("""
        DROP TABLE IF EXISTS public.animals_3;

        CREATE TABLE public.animals_3 (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT NULL,
            left_g INT NOT NULL,
            right_g INT NOT NULL
        );
    """)
]
