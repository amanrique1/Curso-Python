import hashlib
m = hashlib.sha256()
txt="hola"
m.update(txt.encode())
print(m.digest(), m.hexdigest())


