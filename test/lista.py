import os
pasta = './res2'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        # print(os.path.join(diretorio, arquivo))
        print("res2/" + arquivo)
        # print(diretorio)
        # print(subpastas)
        # print(arquivo)