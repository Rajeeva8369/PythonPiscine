import pandas as pd

def read_parquet(filename: str) -> pd.DataFrame:

    try:
        df = pd.read_parquet(filename, engine="pyarrow")
        return df.head(10)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier Parquet: {e}")
        return pd.DataFrame()

df = read_parquet("flights.parquet")
print(df)





import pandas as pd

def read_parquet_columns(filename: str, columns: list) -> pd.DataFrame:

    try:
        df = pd.read_parquet(filename, columns=columns, engine="pyarrow")
        return df
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier Parquet: {e}")
        return pd.DataFrame()


df_cols = read_parquet_columns("flights.parquet", ["FL_DATE", "DEP_DELAY", "ARR_DELAY"])
print(df_cols.head(10))






import pyarrow.parquet as pq
import pandas as pd

def read_parquet_batch(filename: str, batch_size: int) -> pd.DataFrame:

    try:
        table = pq.ParquetFile(filename)
        dfs = []

        for batch in table.iter_batches(batch_size=batch_size):
            df_batch = batch.to_pandas()
            dfs.append(df_batch.head(2))

        if dfs:
            return pd.concat(dfs, ignore_index=True)
        else:
            return pd.DataFrame()

    except Exception as e:
        print(f"Erreur lors de la lecture par lots du fichier Parquet: {e}")
        return pd.DataFrame()

df_batches = read_parquet_batch("flights.parquet", batch_size=1000)
print(df_batches.head(20))






import pandas as pd

def save_to_parquet(df: pd.DataFrame, filename: str):

    try:
        df.to_parquet(filename, engine="pyarrow", compression="snappy", index=False)
        print(f"Fichier sauvegardé avec succès : {filename}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde en Parquet: {e}")



data = {
    "FL_DATE": ["2013-01-01", "2013-01-02", "2013-01-03"],
    "DEP_DELAY": [2, -3, 5],
    "ARR_DELAY": [4, -1, 10],
    "DISTANCE": [800, 900, 850]
}
df_test = pd.DataFrame(data)

save_to_parquet(df_test, "test_output.parquet")


df_check = pd.read_parquet("test_output.parquet", engine="pyarrow")
print(df_check)
