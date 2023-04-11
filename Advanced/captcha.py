from random import randrange, choice

mala="qwertzuiopasdfghjklyxcvbnm"
velka=mala.upper()
cisla="1234567890"

while True:
    captcha=""
    prepis=""
    for i in range(5):
        v=randrange(2)
        if v==0:
            captcha+=choice(mala)
        elif v==1:
            captcha+=choice(velka)
        else :
            captcha+=choice(cisla)
    print("Zadej - ",captcha)
    prepis=input("> ")
    if captcha==prepis:
        print("môžeš")
        break
    else:
        print("idi na chuj")
            