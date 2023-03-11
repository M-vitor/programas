def main():
    print("Calcule o valor da expressão: 9x - 4x + 10")
    x = float(input("digite o valor do coeficiente x:"))
    v1 = 9
    v2 = 4
    v3 = 10

    calculo = v1 * x - v2 * x + v3

    print('O valor da raiz na função f(x)=9x - 4x + 10 é:', calculo)

if __name__ == '__main__':
    main()
