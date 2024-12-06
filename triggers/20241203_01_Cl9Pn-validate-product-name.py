"""
validate_product_name
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
       DROP TRIGGER IF EXISTS trg_clean_product_name ON public.product;
   """),
    step("""
       DROP FUNCTION IF EXISTS public.validate_product_name();
   """),
    step("""
            CREATE OR REPLACE FUNCTION public.validate_product_name()
            RETURNS trigger
            LANGUAGE plpgsql
            AS $function$
            BEGIN
                NEW.product_name := trim(NEW.product_name);
                NEW.product_name := initcap(NEW.product_name);
                RETURN NEW;
            END;
            $function$;
        """),
    step("""
            CREATE TRIGGER trg_clean_product_name
            BEFORE INSERT OR UPDATE ON public.product
            FOR EACH ROW EXECUTE FUNCTION public.validate_product_name();
        """)
]
