import bcrypt

password = b"SecretPass69"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)