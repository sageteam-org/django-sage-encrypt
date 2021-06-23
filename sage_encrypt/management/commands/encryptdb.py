from django.db import connections, connection
from django.core.management.base import BaseCommand

from sage_encrypt.services.setting import get_setting


class Command(BaseCommand):
    help = 'Encrypt all data in specific column.'

    def add_arguments(self, parser):
        """
        add arguments for command
        """
        parser.add_argument(
            '-d',
            '--database',
            type=str,
            help='database',
            required=False
        )
        parser.add_argument(
            '-t',
            '--table',
            type=str,
            help='database table',
            required=True
        )
        parser.add_argument(
            '-c',
            '--column',
            type=str,
            help='table column',
            required=True
        )
        parser.add_argument(
            '-a',
            '--algorithm',
            type=str,
            help='encryption algorithm(symmetric/asymmetric)',
            required=True
        )

    def create_sym_query(self, table_name, column_name):
        """
        create symmetric encrypt & replace sql query
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
                    SET {col_name} = pgp_sym_encrypt({col_name}::text, '{sym_key}');
                """.format(
            table_name=table_name,
            col_name=column_name,
            sym_key=ENCRYPT_KEY
        )

        return query

    def create_asym_query(self, table_name, column_name):
        """
        create asymmetric encrypt & replace sql query
        :param table_name: target table name
        :type table_name: str
        :param column_name: target column name
        :type column_name: str
        :return: SQL Query
        :rtype: str
        """
        ENCRYPT_PUBLIC_KEY = get_setting(connection, 'ENCRYPT_PUBLIC_KEY')
        query = """
                UPDATE {table_name}
                    SET {col_name} = pgp_pub_encrypt(({col_name}::text, dearmor('{asym_key}'));
                """.format(
            table_name=table_name,
            col_name=column_name,
            asym_key=ENCRYPT_PUBLIC_KEY
        )

        return query

    def handle(self, *args, **options):
        """
        execute raw sql to encrypt data
        """
        db_name = options['database']
        table_name = options['table']
        col_name = options['column']
        algorithm = options['algorithm']

        if algorithm == 'symmetric':
            sql_query = self.create_sym_query(table_name=table_name, column_name=col_name)
        elif algorithm == 'asymmetric':
            sql_query = self.create_asym_query(table_name=table_name, column_name=col_name)
        else:
            raise TypeError(
                'algorithm `{}` not defined, choices are `symmetric` and `asymmetric`'.format(algorithm)
            )

        if db_name:
            with connections[db_name].cursor() as cursor:
                cursor.execute(sql_query)
                message = f'Encryption applied.\nTable -> {table_name}\nColumn -> {col_name}\nAlgorithm -> {algorithm}'
        else:
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                message = f'Encryption applied.\nTable -> {table_name}\nColumn -> {col_name}\nAlgorithm -> {algorithm}'

        self.stdout.write(
            self.style.SUCCESS(message)
        )
