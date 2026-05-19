sapa = "tuliskan"
pesanbaru = []

def swap(pesan, pesanbaru, simpan= ""):
    if type(pesan) == str:
        simpan = pesan
        pesan = list(pesan)
    if pesan == []:
        print(f"{simpan} = ", end= "")
        for x in pesanbaru:
            print(x, end= "")
    else:
        hasil = pesan.pop()
        pesanbaru.append(hasil)
        swap(pesan, pesanbaru, simpan)

swap(sapa, pesanbaru)


