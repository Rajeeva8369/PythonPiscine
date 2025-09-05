def native_csv_read(file: str) -> list[tuple]:
    resultat = []

    with open(file, "r") as f:
        lignes = iter(f)

        next(lignes)

        for index, ligne in enumerate(lignes):
            valeurs = ligne.strip().split(";")
            resultat.append((index, *valeurs))

    return resultat

input_file = "ressources/orders_semicolon2.csv"
t = native_csv_read(input_file)
print(t)





def native_csv_write(file: str, headers: list, data: list[tuple]):

    with open(file, "w", encoding="utf-8") as f:
        f.write(",".join(headers) + "\n")

        for row in data:
            f.write(",".join(map(str, row)) + "\n")

headers = ["Nom", "Âge", "Ville"]
data = [
    ("Alice", 25, "Paris"),
    ("Bob", 30, "Lyon"),
    ("Charlie", 22, "Marseille")
]

native_csv_write("personnes.csv", headers, data)






