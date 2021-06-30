ASYM_ENCRYPT_SQL_WITH_NULLIF = "pgp_pub_encrypt(nullif(%s, NULL)::text, dearmor('{}'))"
SYM_ENCRYPT_SQL_WITH_NULLIF = "pgp_sym_encrypt(nullif(%s, NULL)::text, '{}')"

ASYM_ENCRYPT_SQL = "pgp_pub_encrypt(%s, dearmor('{}'))"
SYM_ENCRYPT_SQL = "pgp_sym_encrypt(%s, '{}')"

ASYM_DECRYPT_SQL = "pgp_pub_decrypt(%s::bytea, dearmor('{}'))::%s"
SYM_DECRYPT_SQL = "pgp_sym_decrypt(%s::bytea, '{}')::%s"
