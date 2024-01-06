import pandas as pd


def initialize_empty_dataframe():
    try:
        df = pd.DataFrame()
        return df
    except Exception as ex:
        print(ex)
        return None


def concat_dataframes(df1, df2):
    try:
        df = pd.concat([df1,df2], ignore_index= True)
        return df
    except Exception as ex:
        print(ex)
        return None

def normalize_data(data):
    try:
        df = pd.json_normalize(data)
        return df
    except Exception as ex:
        print(ex)
        return None


def drop_columns_by_names(dataframe, drop_cols):
    try:
        temp_drop_cols = drop_cols.copy()
        try:
            dropped_col_df = dataframe.drop(temp_drop_cols, axis=1)
            return dropped_col_df
        except Exception as ex:
            err = str(ex)
            column_not_found = err.split("[")[1].split("]")[0].replace("'","").split(", ")
            for i in column_not_found:
                temp_drop_cols.remove(i)
            dropped_col_df = dataframe.drop(temp_drop_cols, axis=1)
            return dropped_col_df
    except Exception as exc:
        print(exc)
        return None


def convert_to_date(date_col, format):
    try:
        date_col = pd.to_datetime(date_col).dt.strftime(format)
        return date_col
    except Exception as ex:
        print(ex)
        return None


def rename_column_headers(dataframe, new_columns):
    try:
        dataframe.columns = new_columns
        return dataframe
    except Exception as ex:
        print(ex)
        return None


def reorder_column_headers(dataframe, new_col_order):
    try:
        dataframe = dataframe[new_col_order]
        return dataframe
    except Exception as ex:
        print(ex)
        return None
