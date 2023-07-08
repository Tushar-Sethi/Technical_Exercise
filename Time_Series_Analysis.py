import pandas as pd
from Data_Prep import *
from Customer_Segmentation import *
import matplotlib.pyplot as plt


try:
    # Getting the Data from the Data_Prep script
    sorted_df = Prepare_data()

    # Getting the Month from the date column
    sorted_df['Month'] = sorted_df['Date'].dt.month

    # Getting the Monthly Total Amount 
    monthly_totals = sorted_df.groupby('Month')['TotalAmount'].sum().reset_index()
    print('Monthly Total Amount:')
    print(monthly_totals)


    # Visualization For Total Amount Monthly:
    print('Plot For Total Amount Monthly:')
    plt.plot(monthly_totals['Month'], monthly_totals['TotalAmount'], marker='o')
    plt.title('Total Amount Over Months')
    plt.xlabel('Month')
    plt.ylabel('Total Amount')
    plt.xticks(monthly_totals['Month'])
    plt.ticklabel_format(style='plain', axis='y', useOffset=False)
    # for i, txt in enumerate(monthly_totals['TotalAmount']):
    #     plt.text(monthly_totals['Month'][i], txt, f"{txt:,}", ha='center', va='bottom')
    plt.grid(True)
    plt.show()


    # Top 50 Selling Products.
    top_selling_products = sorted_df.groupby('ProductName')['TotalAmount'].sum().nlargest(50)
    print('Top 50 Selling Products:')
    print(top_selling_products)

    # Visualization for Top Selling Products in form of Horizontal Bar graph
    plt.figure(figsize=(15, 15))
    plt.barh(top_selling_products.index, top_selling_products.values)
    plt.title('Top 50 Selling Products')
    plt.xlabel('Total Amount')
    plt.ylabel('Product Name')
    plt.gca().invert_yaxis()
    plt.show()


    # Analyzing total purchase amount by country.
    purchase_by_country = sorted_df.groupby('Country')['TotalAmount'].sum().sort_values(ascending=False)
    # purchase_by_country Percentage calculation
    purchase_percentage = purchase_by_country / purchase_by_country.sum() * 100

    # Creating a dataframe with country, purchase amount, and percentage columns
    df_summary_country = pd.DataFrame({'Country': purchase_by_country.index,
                            'Purchase Amount': purchase_by_country.values,
                            'Percentage': purchase_percentage.values})
    print('Total purchase amount by country:')
    print(df_summary_country)


    # Top 5 best selling products for each country
    country_product_df = sorted_df[['ProductName','Country','TotalAmount']]
    top_products_by_country = country_product_df.groupby('Country').apply(lambda x: x.nlargest(5, 'TotalAmount')).reset_index(drop=True)
    print('Top 5 Best selling Products for Each Country')
    print(top_products_by_country)

    # Top 5 Customers for each month
    top_customers_by_month = sorted_df.groupby('Month').apply(lambda x: x.nlargest(5, 'TotalAmount'))[['CustomerID', 'TotalAmount', 'Country', 'Month']].reset_index(drop=True)
    print('Top 5 Customers every Month')
    print(top_customers_by_month)

    # Customer Segmentation as per Total Amount Spent
    customer_totals = get_customer_segmentation()
    print('Customers Segmentation on basis of their Total Amount Spent')
    print(customer_totals)
    print('Visualization for Customers Segmentation')

    customer_count = customer_totals['Category'].value_counts()
    # Bar Graph
    plt.figure(figsize=(10, 8))
    plt.bar(customer_count.index, customer_count.values, color=['red', 'orange', 'green'])
    plt.title('Number of Customers by Category')
    plt.xlabel('Category')
    plt.ylabel('Number of Customers')
    plt.show()

except:
    print('Some Error Occured')


