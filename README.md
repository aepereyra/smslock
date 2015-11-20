# SMSLOCK
What is this?
THis soft is used to open physical lock using 2 factor authentication (with sms validating cellphone number and password)

This works with raspberry and uses GPIO17 to send open signal

How create the database

Just run 
python creatabla.py

to create a new user just  execute it
python insertuser.py {CELLNAMBER} {HASH SHA512 OF THE PASSWORD}

example
python insertuser.py 01159555555 5cf58927b41378bcc076b26b3b850a66ebcec3ace74f6b949da5405721dd39488a238f5afff793b5125038bb1dd7184c1c11c47f4844d1ccbb310c9c75893b65


