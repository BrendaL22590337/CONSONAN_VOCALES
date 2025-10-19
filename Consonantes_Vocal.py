# contar_vocales_consonantes.py

def contar_vocales_consonantes(texto):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    num_vocales = sum(1 for c in texto if c in vocales)
    num_consonantes = sum(1 for c in texto if c in consonantes)

    return num_vocales, num_consonantes


# Programa principal
def main():
    texto = input("Escribe un texto: ")
    v, c = contar_vocales_consonantes(texto)
    print(f"Número de vocales: {v}")
    print(f"Número de consonantes: {c}")


if __name__ == "__main__":
    main()
