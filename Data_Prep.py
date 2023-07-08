import pandas as pd


def Prepare_data():
    # Reading the DataSet from the Excel file
    df = pd.read_excel('retail_data_v1.xlsx')

    # Converting the date column to Pandas Datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Dropping the rows which contains missing values in any of the columns
    df = df.dropna()

    # Sorting the Dataframe based on CustomerID and Date
    sorted_df = df.sort_values(['CustomerID', 'Date'])

    # Creating a new column Named TotalAmount
    sorted_df['TotalAmount'] = sorted_df['Quantity'] * sorted_df['UnitPrice']

    return sorted_df


try:
    df = Prepare_data()
    print(df.columns)
except:
    print('Some Error Occured')

