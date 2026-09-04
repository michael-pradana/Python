import random

welcome_message = "main game yuk!"
marmut_possesion = random.randint (1, 4)


print (welcome_message)

nama_user = input("masukkan namamu : ")
print (f'''
halo {nama_user}!
dimana si marmut?

[_]  [_]  [_]  [_]''')
option_user = int(input("ada di 1/2/3/4 ?  "))
print (f'''

kamu nebak {(option_user)}

''')
# kamu nebak {type(option_user)}

if option_user == marmut_possesion:
    print (f'''dan benar, tebakan kamu adalah {option_user} !
           ''')
else:
    print (f'''haha salah cok, masak {option_user} !
           ''')
    
print (f"yang bener {marmut_possesion}")
