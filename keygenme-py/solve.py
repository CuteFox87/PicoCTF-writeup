import hashlib

bUsername_trial = b"GOUGH"

list = [4,5,3,6,2,7,1,8]

print("picoCTF{1n_7h3_|<3y_of_",end='')
for i in list:
    print(hashlib.sha256(bUsername_trial).hexdigest()[i],end='')
print('}')