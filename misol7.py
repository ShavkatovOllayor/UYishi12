def talaba_info(**malumotlar):
    for kalit, qiymat in malumotlar.items():
        key = kalit.capitalize()
        print(f"{key}: {qiymat}")


ism = input().strip()
kurs = int(input())
shahar = input().strip()

talaba_info(Ism=ism, Kurs=kurs, Shahar=shahar)
