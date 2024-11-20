"""
get-manufacturers
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
    DROP FUNCTION IF EXISTS get_manufacturers();
   CREATE OR REPLACE FUNCTION get_all_manufacturers()
   RETURNS TABLE(manufacturer_id INT, title_country VARCHAR(255), address_of_manufacturer TEXT, contact_list TEXT) AS $$
   BEGIN
       RETURN QUERY SELECT m.manufacturer_id, m.title_country, m.address_of_manufacturer, m.contact_list 
                    FROM manufacturer AS m ORDER BY m.manufacturer_id;
   END;
   $$ LANGUAGE plpgsql;
    """)
]
