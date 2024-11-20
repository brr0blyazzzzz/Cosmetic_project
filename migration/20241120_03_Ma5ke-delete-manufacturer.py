"""
delete-manufacturer
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
    DROP PROCEDURE IF EXISTS delete_manufacturer(TEXT);
    CREATE OR REPLACE PROCEDURE delete_manufacturer(IN p_manufacturer_id TEXT)
LANGUAGE plpgsql AS $$
DECLARE
    man_id INT;
BEGIN
    man_id := NULLIF(TRIM(p_manufacturer_id), '');
    IF man_id IS NULL OR NOT (p_manufacturer_id ~ '^[0-9]+$') THEN
        RAISE EXCEPTION 'The manufacturer ID must be a positive integer and cannot be empty';
    END IF;
    man_id := CAST(man_id AS INT);
    IF NOT EXISTS (SELECT 1 FROM manufacturer WHERE manufacturer.manufacturer_id = man_id) THEN
        RAISE EXCEPTION 'Manufacturer with ID % not found', man_id;
    END IF;
    DELETE FROM manufacturer WHERE manufacturer.manufacturer_id = man_id;
END;
$$;
    """)
]
