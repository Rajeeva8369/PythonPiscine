import pandas as pd


def pandas_csv_read(file: str) -> pd.DataFrame:

    df = pd.read_csv(file)
    return df

if __name__ == "__main__":
    df = pandas_csv_read("personnes.csv")

    print("Voici le DataFrame lu avec pandas :")
    print(df)





import pandas as pd


def pandas_csv_write(file: str, headers: list, data: list[tuple]):

    df = pd.DataFrame(data, columns=headers)
    df.to_csv(file, index=False)

headers = ["Nom", "Âge", "Ville"]
data = [
    ("Alice", 25, "Paris"),
    ("Bob", 30, "Lyon"),
    ("Charlie", 35, "Marseille")
]

pandas_csv_write("personnes.csv", headers, data)
