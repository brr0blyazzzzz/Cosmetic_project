"""
delete-manufacturers
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
     DROP FUNCTION IF EXISTS delete_list_of_manufacturers(TEXT[]);
    CREATE OR REPLACE FUNCTION delete_list_of_manufacturers(p_manufacturer_ids TEXT[])
RETURNS INTEGER AS $$
DECLARE
    v_manufacturer_id INT;
    v_deleted_count INT := 0; 
    id TEXT; 
BEGIN
    FOREACH id IN ARRAY p_manufacturer_ids LOOP
        IF id IS NULL OR NOT id ~ '^[0-9]+$' THEN
            RAISE NOTICE 'ID% is not valid.', id;
            CONTINUE; 
        END IF;
        v_manufacturer_id := id::INT;
        IF EXISTS (SELECT 1 FROM manufacturer WHERE manufacturer_id = v_manufacturer_id) THEN
            DELETE FROM manufacturer WHERE manufacturer_id = v_manufacturer_id;
            v_deleted_count := v_deleted_count + 1;  
        ELSE
            RAISE NOTICE 'The manufacturer with ID % was not found.', v_manufacturer_id;
        END IF;
    END LOOP;

    RAISE NOTICE 'Removed manufacturers: %', v_deleted_count;
    RETURN v_deleted_count;  
END;
$$ LANGUAGE plpgsql;

    """)
]
