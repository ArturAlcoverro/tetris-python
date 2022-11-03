import sys

if __name__ == '__main__':
    try:
        num = int(sys.argv[1])
        if num < 0: raise ValueError('')
        aux = [0, 1]
        arr = []
        while len(aux) < num:
            aux.append(
                aux[len(aux) - 1] + aux[len(aux) - 2]
            )

        for i in range(num):
            arr.append(aux[i])

        print(aux)

    except ValueError:
        print("Argumento invalido!")