from django.db import connections, connection
from django.db.utils import InternalError
from django.core.management.base import BaseCommand

from sage_encrypt.services.setting import get_setting


class Command(BaseCommand):
    help = 'Decrypt all encrypted data in specific column.'

    def add_arguments(self, parser):
        """
        add arguments for command
        """
        parser.add_argument('-d', '--database', type=str, help='database')
        parser.add_argument('-t', '--table', type=str, help='database table')
        parser.add_argument('-c', '--column', type=str, help='table column')

    def create_sym_query(self, table_name, column_name):
        """
        create symmetric decrypt & replace sql query
        :param table_name: target table name
        :type table_name: str
        :param column_name: target column name
        :type column_name: str
        :return: SQL Query
        :rtype: str
        """
        ENCRYPT_KEY = get_setting(connection, 'ENCRYPT_KEY')
        query = """
                UPDATE {table_name}
                    SET {col_name} = pgp_sym_decrypt({col_name}::bytea, '{sym_key}');
                """.format(
            table_name=table_name,
            col_name=column_name,
            sym_key=ENCRYPT_KEY
        )

        return query

    def create_asym_query(self, table_name, column_name):
        """
        create asymmetric decrypt & replace sql query
        :param table_name: target table name
        :type table_name: str
        :param column_name: target column name
        :type column_name: str
        :return: SQL Query
        :rtype: str
        """
        ENCRYPT_PRIVATE_KEY = get_setting(connection, 'ENCRYPT_PRIVATE_KEY')
        query = """
                UPDATE {table_name}
                    SET {col_name} = pgp_pub_decrypt({col_name}::bytea, dearmor('{asym_key}'));
                """.format(
            table_name=table_name,
            col_name=column_name,
            asym_key=ENCRYPT_PRIVATE_KEY
        )

        return query

    def handle(self, *args, **options):
        """
        execute raw sql to replace encrypted data
        """
        db_name = options['database']
        table_name = options['table']
        col_name = options['column']

        sym_sql_query = self.create_sym_query(table_name=table_name, column_name=col_name)
        asym_sql_query = self.create_asym_query(table_name=table_name, column_name=col_name)

        if db_name:
            with connections[db_name].cursor() as cursor:
                try:
                    cursor.execute(sym_sql_query)
                    message = 'symmetric decryption applied.'
                except InternalError:
                    cursor.execute(asym_sql_query)
                    message = 'asymmetric decryption applied.'
        else:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sym_sql_query)
                    message = 'symmetric decryption applied.'
                except InternalError:
                    cursor.execute(asym_sql_query)
                    message = 'asymmetric decryption applied.'

        self.stdout.write(
            self.style.SUCCESS(message)
        )
