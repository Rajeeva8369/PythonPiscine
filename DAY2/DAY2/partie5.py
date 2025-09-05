import pandas as pd

data = {
    "Nom": ["Alice", "Bob", "Charlie"],
    "Âge": [25, 30, 35],
    "Ville": ["Paris", "Lyon", "Marseille"]
}

df = pd.DataFrame(data)
df.to_excel("p.xlsx", sheet_name="Employés", index=False, engine="openpyxl")

