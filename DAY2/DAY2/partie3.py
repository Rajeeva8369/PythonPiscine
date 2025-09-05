import sys
import pandas as pd


def create_series() -> pd.Series:

    args = sys.argv[1:]

    int_args = [int(x) for x in args]

    return pd.Series(int_args)


if __name__ == "__main__":
    sys.argv = ["script.py", "5", "10", "15", "20"]

    serie = create_series()
    print("Voici la Series créée à partir des arguments :")
    print(serie)







import sys
import pandas as pd


def create_series() -> pd.Series:

    args = sys.argv[1:]
    int_args = [int(x) for x in args]
    return pd.Series(int_args)


def series_operations(series: pd.Series) -> (int, float, float):

    somme = series.sum()
    moyenne = series.mean()
    ecart_type = series.std()
    return (somme, moyenne, ecart_type)



if __name__ == "__main__":
    sys.argv = ["script.py", "5", "10", "15", "20"]

    t = create_series()
    print("Series utilisée :")
    print(t)

    print("\nRésultats des opérations (somme, moyenne, écart-type) :")
    print(series_operations(t))







import pandas as pd


def create_dataframe(products: list[str], quantities: list[int], prices: list[float]) -> pd.DataFrame:

    orders = pd.DataFrame({
        "Product": products,
        "Quantity": quantities,
        "Price": prices
    })

    return orders


if __name__ == "__main__":
    products = ["Pomme", "Banane", "Orange"]
    quantities = [10, 5, 8]
    prices = [0.5, 0.3, 0.7]

    df = create_dataframe(products, quantities, prices)

    print("Voici le DataFrame 'orders' créé :")
    print(df)






import pandas as pd


def dataframe_accession(data: pd.DataFrame) -> tuple:

    products_list = data["Product"].tolist()
    second_row = data.loc[1].to_dict()
    third_quantity = data.loc[2, "Quantity"]

    return (products_list, second_row, third_quantity)


if __name__ == "__main__":
    products = ['Smartphone', 'Headphones', 'Printer', 'Keyboard']
    quantities = [7, 4, 8, 5]
    prices = [4911.924342502764, 753.3786756443856, 4701.49172549989, 5099.099081811153]

    df = pd.DataFrame({
        "Product": products,
        "Quantity": quantities,
        "Price": prices
    })

    res = dataframe_accession(df)

    for elem in res:
        print(elem)





