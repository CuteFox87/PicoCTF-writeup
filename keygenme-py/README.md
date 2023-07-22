# PicoCTF2021 - keygenme-py

## Information

分數 : **30 points**

分類 : **Reverse Engineering**

## Description

[keygenme-trial.py](./keygenme-trial.py)

## Hints

(None)

## Solutions

輸入b後會告訴你需要購買完整版才能進入。因此我們要透過破解它的完整版。

以下是輸入c後呼叫的函數enter_license
```py
def enter_license():
    user_key = input("\nEnter your license key: ")
    user_key = user_key.strip()

    global bUsername_trial
    
    if check_key(user_key, bUsername_trial):
        decrypt_full_version(user_key)
    else:
        print("\nKey is NOT VALID. Check your data entry.\n\n")
```
還有check_key的部分程式
```py
    if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
        return False
    else:
        i += 1

    if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
        return False
    else:
        i += 1

    if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
        return False
    else:
        i += 1

    if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
        return False
    else:
        i += 1

    if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
        return False
    else:
        i += 1

    if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
        return False
    else:
        i += 1

    if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
        return False
    else:
        i += 1

    if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
        return False
```

因此我們可以編寫解題程式
```py
import hashlib

bUsername_trial = b"GOUGH"

list = [4,5,3,6,2,7,1,8]

print("picoCTF{1n_7h3_|<3y_of_",end='')
for i in list:
    print(hashlib.sha256(bUsername_trial).hexdigest()[i],end='')
print('}')
```
即獲得flag

## Flag
``picoCTF{1n_7h3_|<3y_of_xxxxxxxx}``

## Concept
觀察
