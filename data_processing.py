import pandas as pd

def process_data():
    df1 = pd.read_csv('data/daily_sales_data_0.csv')
    df2 = pd.read_csv('data/daily_sales_data_1.csv')
    df3 = pd.read_csv('data/daily_sales_data_2.csv')

    df1['price'] = df1['price'].str.replace('$', '').astype('float32')
    df2['price'] = df2['price'].str.replace('$', '').astype('float32')
    df3['price'] = df3['price'].str.replace('$', '').astype('float32')

    df1 = df1[df1['product'] == 'pink morsel']
    df1['sales'] = df1['quantity'] * df1['price']
    df1 = df1[['sales', 'date', 'region']]

    df2 = df2[df2['product'] == 'pink morsel']
    df2['sales'] = df2['quantity'] * df2['price']
    df2 = df2[['sales', 'date', 'region']]

    df3 = df3[df3['product'] == 'pink morsel']
    df3['sales'] = df3['quantity'] * df3['price']
    df3 = df3[['sales', 'date', 'region']]

    final_df = pd.concat([df1, df2, df3])
    return final_df


def save_to_csv(dataframe, output_filename):
    dataframe.to_csv(output_filename, index=False)



result_df = process_data()

save_to_csv(result_df, 'output.csv')

