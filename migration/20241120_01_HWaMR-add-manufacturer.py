"""
add-manufacturer
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
    DROP PROCEDURE IF EXISTS add_manufacturer(TEXT,TEXT,TEXT);
    CREATE OR REPLACE PROCEDURE add_manufacturer(
    IN p_title_country TEXT,
    IN p_address_of_manufacturer TEXT,
    IN p_contact_list TEXT
)
LANGUAGE plpgsql AS $$
BEGIN
    p_title_country := TRIM(p_title_country);
    p_address_of_manufacturer := TRIM(p_address_of_manufacturer);
    p_contact_list := TRIM(p_contact_list);

    IF LENGTH(p_title_country) = 0 OR LENGTH(p_address_of_manufacturer) = 0 OR LENGTH(p_contact_list) = 0 THEN
        RAISE EXCEPTION 'Параметры не могут быть пустыми или состоять только из пробелов';
    END IF;

    INSERT INTO manufacturer (title_country, address_of_manufacturer, contact_list) 
    VALUES (p_title_country, p_address_of_manufacturer, p_contact_list);
END;
$$;
    """
    )
]
