from django.db.models.expressions import Col
from django.db.models.sql.compiler import SQLInsertCompiler
from django.db.backends.postgresql.base import DatabaseWrapper


class DecryptedCol(Col):
    def __init__(self, alias, target, output_field=None):
        self.target = target
        super(DecryptedCol, self).__init__(alias, target, output_field)

    def as_sql(self, compiler: SQLInsertCompiler, connection: DatabaseWrapper):
        """
        create SQL query with PostgreSQL decryption and casting
        """
        sql, params = super(DecryptedCol, self).as_sql(compiler, connection)
        sql = self.target.get_decrypt_sql(connection) % (sql, self.target.get_cast_sql())
        return sql, params
