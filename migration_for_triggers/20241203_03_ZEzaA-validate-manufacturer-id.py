"""
validate_manufacturer_id
"""

from yoyo import step

__depends__ = {'20241203_02_XLfgx-validate-product-title'}

steps = [
    step(
        """
        DROP FUNCTION IF EXISTS public.validate_manufacturer_id;
        """,
        """
        CREATE OR REPLACE FUNCTION public.validate_manufacturer_id()
        RETURNS trigger
        LANGUAGE plpgsql
        AS $function$
        BEGIN
            NEW.manufacturer_id := trim(NEW.manufacturer_id::text)::integer;

            IF NEW.manufacturer_id IS NULL THEN
                RAISE EXCEPTION 'manufacturer_id cannot be NULL';
            END IF;

            IF NEW.manufacturer_id <= 0 THEN
                RAISE EXCEPTION 'manufacturer_id must be a positive integer';
            END IF;

            IF NOT EXISTS (SELECT 1 FROM public.manufacturer WHERE manufacturer_id = NEW.manufacturer_id) THEN
                RAISE EXCEPTION 'manufacturer_id % does not exist in manufacturer table', NEW.manufacturer_id;
            END IF;

            RETURN NEW;
        END;
        $function$;
        """
    ),
    step(
        """
        DROP TRIGGER IF EXISTS trg_validate_manufacturer_id ON public.product;
        """,
        """
        CREATE TRIGGER trg_validate_manufacturer_id
        BEFORE INSERT OR UPDATE ON public.product
        FOR EACH ROW EXECUTE FUNCTION public.validate_manufacturer_id();
        """
    )
]
