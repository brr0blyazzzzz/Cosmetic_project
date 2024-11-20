"""
get-manufacturer-by-id
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
        DROP FUNCTION IF EXISTS get_manufacturer_by_id(TEXT);
        CREATE OR REPLACE FUNCTION get_manufacturer_by_id(IN p_manufacturer_id TEXT)
RETURNS TABLE(manufacturer_id INT, title_country VARCHAR(255), address_of_manufacturer TEXT, contact_list TEXT) AS $$
DECLARE
    v_id INT;
BEGIN
    p_manufacturer_id := TRIM(p_manufacturer_id);
    IF LENGTH(p_manufacturer_id) = 0 OR NOT p_manufacturer_id ~ '^[0-9]+$' THEN
        RAISE EXCEPTION 'The identifier must be a positive integer and cannot be empty';
    END IF;
    
    v_id := CAST(p_manufacturer_id AS INT);
    
    IF NOT EXISTS (SELECT 1 FROM manufacturer WHERE manufacturer.manufacturer_id = v_id) THEN
        RAISE EXCEPTION 'Manufacturer with ID % not found', v_id;
    END IF;
    
    RETURN QUERY SELECT * FROM manufacturer WHERE manufacturer.manufacturer_id = v_id;
END;
$$ LANGUAGE plpgsql;
    """,
         )
]
