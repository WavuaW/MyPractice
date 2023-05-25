import bcrypt

password = b"SecretPass69"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

if bcrypt.checkpw(password, hashed):
    print('Match')
else:
    print('Try Again Loser')