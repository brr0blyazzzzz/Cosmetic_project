"""
update-manufacturer
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
    DROP PROCEDURE IF EXISTS update_manufacturer(TEXT,TEXT,TEXT,TEXT);
    CREATE OR REPLACE PROCEDURE update_manufacturer(
    IN p_manufacturer_id TEXT, 
    IN p_new_title_country TEXT,
    IN p_new_address_of_manufacturer TEXT,
    IN p_new_contact_list TEXT
)
LANGUAGE plpgsql AS $$
BEGIN
    IF LENGTH(TRIM(p_manufacturer_id)) = 0 OR NOT TRIM(p_manufacturer_id) ~ '^[0-9]+$' THEN
        RAISE EXCEPTION 'The manufacturer ID must be a positive integer and cannot be empty ';
    END IF;
    DECLARE
        v_manufacturer_id INT := CAST(TRIM(p_manufacturer_id) AS INT);
    BEGIN
        IF NOT EXISTS (SELECT 1 FROM manufacturer WHERE manufacturer_id = v_manufacturer_id) THEN
            RAISE EXCEPTION 'Manufacturer with ID % not found', v_manufacturer_id;
        END IF;

        IF p_new_title_country IS NOT NULL AND TRIM(p_new_title_country) <> '' THEN
            UPDATE manufacturer 
            SET title_country = TRIM(p_new_title_country)
            WHERE manufacturer_id = v_manufacturer_id;
        END IF;

        IF p_new_address_of_manufacturer IS NOT NULL AND TRIM(p_new_address_of_manufacturer) <> '' THEN
            UPDATE manufacturer 
            SET address_of_manufacturer = TRIM(p_new_address_of_manufacturer)
            WHERE manufacturer_id = v_manufacturer_id;
        END IF;

        IF p_new_contact_list IS NOT NULL AND TRIM(p_new_contact_list) <> '' THEN
            UPDATE manufacturer 
            SET contact_list = TRIM(p_new_contact_list)
            WHERE manufacturer_id = v_manufacturer_id;
        END IF;
    END;
END;
$$;
    """)
]
