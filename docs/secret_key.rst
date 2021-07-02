Generate secret key
-------------------

.. code:: shell

    # generate private & public key
    gpg --gen-key # in password section do not enter password

    gpg --list-keys
    # output
    pub   rsa3072 2021-06-20 [SC] [expires: 2023-06-20]
          <test_token_generated>
    uid           [ultimate] Test <test@gmail.com>
    sub   rsa3072 2021-06-20 [E] [expires: 2023-06-20]

    gpg -a --export <test_token_generated> > public.key
    gpg -a --export-secret-keys <test_token_generated> > private.key