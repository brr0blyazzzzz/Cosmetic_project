"""
create_product_info
"""

from yoyo import step

__depends__ = {}
from yoyo import step

__depends__ = {}

steps = [
    step(
        """
        DROP TRIGGER IF EXISTS product_info_update ON public.product_info;
        """,
        """
        -- No rollback action needed for trigger
        """
    ),
    step(
        """
        DROP FUNCTION IF EXISTS public.update_product();
        """,
        """
        -- No rollback action needed for function
        """
    ),
    step(
        """
        DROP VIEW IF EXISTS public.product_info;
        """,
        """
        -- No rollback action needed for view
        """
    ),
step(
        """
        CREATE OR REPLACE VIEW public.product_info AS 
        SELECT 
            p.product_id,
            p.product_name,
            p.manufacturer_id,
            p.product_title,
            pi.instance_id,
            pi.expiration_date,
            m.manufacturer_id AS manufacturer_info_id,
            m.title_name,
            m.title_country,
            m.address_of_manufacturer,
            m.contact_list
        FROM 
            product p
        LEFT JOIN 
            product_instance pi ON p.product_id = pi.product_id
        LEFT JOIN 
            manufacturer m ON p.manufacturer_id = m.manufacturer_id;
        """,
        """
        DROP VIEW IF EXISTS public.product_info;
        """
    ),
    step(
        """
        CREATE OR REPLACE FUNCTION public.update_product()
        RETURNS trigger
        LANGUAGE plpgsql
        AS $function$
        BEGIN
            UPDATE public.product
            SET 
                product_name = NEW.product_name,
                manufacturer_id = NEW.manufacturer_id,
                product_title = NEW.product_title
            WHERE product_id = NEW.product_id;

            RETURN NEW; 
        END;
        $function$;
        """,
        """
        DROP FUNCTION IF EXISTS public.update_product();
        """
    ),
    step(
        """
        CREATE TRIGGER product_info_update
        INSTEAD OF UPDATE ON public.product_info
        FOR EACH ROW EXECUTE FUNCTION public.update_product();
        """,
        """
        DROP TRIGGER IF EXISTS product_info_update ON public.product_info;
        """
    )
]
