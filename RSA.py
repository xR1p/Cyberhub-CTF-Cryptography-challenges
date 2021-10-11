from Crypto.Util.number import inverse, long_to_bytes


p=   416064700201658306196320137931
q=  590872612825179551336102196593
e=1
ct= 233905076332791116493645125943542075246931702864018268067376

n= p * q
phi= (p-1) * (q-1)
d=inverse(e,phi)

msg=pow(ct,d,n)

print(long_to_bytes(msg))
