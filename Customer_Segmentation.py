import pandas as pd
from Data_Prep import *



try:
    def get_customer_segmentation():
        # Getting the Data from the Data_Prep script
        sorted_df = Prepare_data()

        customer_totals = sorted_df.groupby('CustomerID')['TotalAmount'].sum().reset_index()

        # Calculating the percentiles
        percentiles = customer_totals['TotalAmount'].quantile([0.5, 0.9])

        # Defining the category thresholds
        low_threshold = percentiles[0.5]
        high_threshold = percentiles[0.9]

        # Categorizing customers based on total purchase amount.
        customer_totals['Category'] = pd.cut(customer_totals['TotalAmount'], bins=[float('-inf'), low_threshold, high_threshold, float('inf')], labels=['Low', 'Medium', 'High'])

        return customer_totals

    customer_totals = get_customer_segmentation()

    print(customer_totals.columns)
    print(customer_totals.shape)
except:
    print('Some Error Occured')