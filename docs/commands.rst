Management Commands
-------------------

sage\_encrypt provides 2 management commands:

1. ``encryptdb``

.. code:: shell

    python manage.py encryptdb --table <table_name> --column <col_name> --cast <field_previous_cast_type> --algorithm <algorithm> #(symmetric/asymmetric)

Options:

1. --database (if you have multiple db's specify for your database)
2. --table (table name in your database not django model title)
3. --column (col name in the specified table)
4. --algorithm (symmetric/asymmetric)
5. --cast (field previous cast that you want to encrypt from that)

Usage:

When you want to add encryption on a row and there is valuable data in
you db, you can encrypt the data to be compatible with Encrypted Field.

2. ``decryptdb``

.. code:: shell

    python manage.py decryptdb --table <table_name> --column <col_name>

Options:

1. --database (if you have multiple db's specify for your database)
2. --table (table name in your database not django model title)
3. --column (col name in the specified table)

Usage:

When your data is encrypted in db and you want to remove encryption from
a row, for getting back data you can use this command, it decrypts data
and replaces in your db.