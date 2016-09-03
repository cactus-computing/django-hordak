# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-03 11:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hordak', '0004_auto_20160902_1612'),
    ]

    operations = [
        migrations.RunSQL(
            """
                CREATE OR REPLACE FUNCTION check_leg()
                    RETURNS trigger AS
                $$
                DECLARE
                    transaction_sum DECIMAL(13, 2);
                BEGIN

                    IF (TG_OP = 'DELETE') THEN
                        SELECT SUM(amount) INTO transaction_sum FROM hordak_leg WHERE transaction_id = OLD.transaction_id;
                    ELSE
                        SELECT SUM(amount) INTO transaction_sum FROM hordak_leg WHERE transaction_id = NEW.transaction_id;
                    END IF;

                    IF transaction_sum != 0 THEN
                        RAISE EXCEPTION 'Sum of transaction amounts must be 0';
                    END IF;
                    RETURN NEW;
                END;
                $$
                LANGUAGE plpgsql
            """
            ,
            'DROP FUNCTION check_leg()'
        ),

        migrations.RunSQL(
            """
                CREATE CONSTRAINT TRIGGER check_leg_trigger
                AFTER INSERT OR UPDATE OR DELETE ON hordak_leg
                DEFERRABLE INITIALLY DEFERRED
                FOR EACH ROW EXECUTE PROCEDURE check_leg();
            """
            ,
            'DROP TRIGGER IF EXISTS check_leg_trigger ON hordak_leg'
        ),
    ]