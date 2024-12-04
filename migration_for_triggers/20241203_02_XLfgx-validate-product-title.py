"""
validate_product_title
"""

from yoyo import step

__depends__ = {'20241203_01_Cl9Pn-validate-product-name'}

steps = [
    step(
        """
        DROP FUNCTION IF EXISTS public.validate_product_title;
        """,
        """
        CREATE OR REPLACE FUNCTION public.validate_product_title()
        RETURNS trigger
        LANGUAGE plpgsql
        AS $function$
        BEGIN
            NEW.product_title := trim(NEW.product_title);
            IF NEW.product_title = '' THEN
                RAISE EXCEPTION 'product_title cannot be empty';
            END IF;
            NEW.product_title := initcap(NEW.product_title);
            RETURN NEW;
        END;
        $function$;
        """
    ),
    step(
        """
        DROP TRIGGER IF EXISTS trg_clean_product_title ON public.product;
        """,
        """
        CREATE TRIGGER trg_clean_product_title
        BEFORE INSERT OR UPDATE ON public.product
        FOR EACH ROW EXECUTE FUNCTION public.validate_product_title();
        """
    )
]
