import pandas as pd

def create_multiindex(df: pd.DataFrame) -> pd.DataFrame:

    try:
        df_multi = df.set_index(["region", "date"])
        return df_multi
    except Exception as e:
        print(f"Erreur lors de la création du MultiIndex: {e}")
        return pd.DataFrame()


df_sales = pd.read_csv("sales.csv")

print("DataFrame original :")
print(df_sales.head(5))

df_multi = create_multiindex(df_sales)
print("\nDataFrame avec MultiIndex :")
print(df_multi.head(10))



