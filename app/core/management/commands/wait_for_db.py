# wait for database get connected
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    # contruct command to wait for database
    def handle(self, *args, **options):
        self.stdout.write('Connecting to database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Successfully connected to database')) # noqa
