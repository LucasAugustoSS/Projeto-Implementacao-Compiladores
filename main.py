from parser import analisar

def main():
    with open("codigo/app.lin", "r") as arquivo:
        codigo = arquivo.read()

    analisar(codigo)

if __name__ == "__main__":
    main()
