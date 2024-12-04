"""
create_product_info
"""

from yoyo import step

depends = {}

steps = [
    step("""
        DROP VIEW IF EXISTS product_info;
    """),
    step("""
        CREATE OR REPLACE VIEW public.product_info_2 AS
            SELECT 
                p.product_id,
                p.product_name,
                p.manufacturer_id,
                (SELECT pi.instance_id FROM product_instance pi WHERE pi.product_id = p.product_id LIMIT 1) AS instance_id,
                (SELECT pi.expiration_date FROM product_instance pi WHERE pi.product_id = p.product_id LIMIT 1) AS expiration_date,
                (SELECT m.title_name FROM manufacturer m WHERE m.manufacturer_id = p.manufacturer_id LIMIT 1) AS manufacturer_name
            FROM 
                product p;
    """)
]




