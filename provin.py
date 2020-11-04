import os

base_dir = "/dados/FOTOS/BRINCOS"

diretorios = ['BRINCO', 'BRINCO (2) 2019 - 2020-MOVIDO',
             'BRINCO DE ARGOLA', 'BRINCO DE ARGOLINHAS',
             'BRINCO MADREPEROLA', 'BRINCO OLHO GREGO',
             'BRINCO ZIRC BRANCA COLORIDA - 2018 E 2019', 
             'BRINCO ZIRC BRANCA COLORIDA - 2019 E 2020']

for diretorio in diretorios:
    old_cod = ""
    codigos = []
    endereco = base_dir+"/"+diretorio

    for nome in os.listdir(endereco):
        cod = nome.split("-")[0].strip()

        if (cod != old_cod):
            os.rename(endereco+"/"+nome, endereco+"/"+cod+".jpg")
        else:
            quantidade = str(codigos.count(cod))
            os.rename(endereco+"/"+nome, endereco+"/"+cod+"_"+quantidade+".jpg")

        codigos.append(cod)
        old_cod = cod

    