"""
create_product_stats
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
       DROP MATERIALIZED VIEW IF EXISTS public.manufacturer_stats;
   """),
    step("""
         CREATE MATERIALIZED VIEW public.manufacturer_stats
         TABLESPACE pg_default AS 
         SELECT m.manufacturer_id,
                m.title_name,
                m.title_country,
                m.contact_list,
                COUNT(DISTINCT p.product_id) AS total_products,
                DENSE_RANK() OVER (ORDER BY COUNT(DISTINCT p.product_id) DESC) AS product_rank
         FROM manufacturer m
         LEFT JOIN product p ON m.manufacturer_id = p.manufacturer_id
         LEFT JOIN product_instance pi ON p.product_id = pi.product_id
         LEFT JOIN product_structure ps ON p.product_id = ps.product_id
         GROUP BY m.manufacturer_id, m.title_name, m.title_country, m.contact_list
         ORDER BY m.manufacturer_id
         WITH DATA;
     """)
]
