
# Challenge name gives me the idea of weak keys in DES
#https://en.wikipedia.org/wiki/Weak_key
#you will find the keys in here : the first key gave me the flag


from Crypto.Cipher import DES
c = bytes.fromhex("7b43fb178c42f2bb5bb7c97d7294824fb62f7fd58e03fb1beac64d66cf5e376b")
key = b"\x01\x01\x01\x01\x01\x01\x01\x01"
cipher = DES.new(key, DES.MODE_ECB)
print(cipher.decrypt(c))
#flag is CYBERHUB{345y_45_12345_67890_:D}