"""
check_dublicate_products
"""

from yoyo import step

__depends__ = {'20241203_03_ZEzaA-validate-manufacturer-id'}

steps = [
    step(
        """
        DROP FUNCTION IF EXISTS public.check_duplicate_product;
        """,
        """
        CREATE OR REPLACE FUNCTION public.check_duplicate_product()
        RETURNS trigger
        LANGUAGE plpgsql
        AS $function$
        BEGIN
            IF EXISTS (
                SELECT 1 
                FROM public.product 
                WHERE product_name = NEW.product_name 
                  AND manufacturer_id = NEW.manufacturer_id 
                  AND product_title = NEW.product_title
            ) THEN
                RAISE EXCEPTION 'Duplicate product exists!';
            END IF;

            RETURN NEW;
        END;
        $function$;
        """
    ),
    step(
        """
        DROP TRIGGER IF EXISTS trigger_check_duplicate_product ON public.product;
        """,
        """
        CREATE TRIGGER trigger_check_duplicate_product
        BEFORE INSERT ON public.product
        FOR EACH ROW EXECUTE FUNCTION public.check_duplicate_product();
        """
    )
]
