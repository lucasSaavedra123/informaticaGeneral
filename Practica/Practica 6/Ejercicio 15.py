def agregarDicEle3(dic,dni,datos):
    dic[dni] = datos
    return


def imprimirDic(dic):

    for i in dic.keys():
        print("{}:{}".format(i,dic[i]))

    return

def imprimirDicOrd(dic):

    dniLista = list(dic.keys())

    for i in range(len(dniLista)):
        for ix in range(len(dniLista)):
            
            if dniLista[i] < dniLista[ix]:
                memoria = dniLista[i]
                dniLista[i]  = dniLista[ix]
                dniLista[ix] = memoria

    for i in dniLista:
        print("{}:{}".format(i,dic[i]))

    return

def main():

    dic = {}

    agregarDicEle3(dic,41834525,[["Lucas", "Saavedra"],[8,5,6]])
    agregarDicEle3(dic,48000001,[["Roberto", "Kolpo"],[4,1,2]])
    agregarDicEle3(dic,35000000,[["Manik", "Ortega"],[9,5,5]])
    
    imprimirDic(dic)
    print()
    imprimirDicOrd(dic)

    return

main()