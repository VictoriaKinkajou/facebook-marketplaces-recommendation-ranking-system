import pandas as pd

def clean_images_csv():
    images_df = pd.read_csv('Images.csv')
    nanfree_images_df = images_df.dropna(how='any')
    check_nans_removed(nanfree_images_df)

def clean_products_csv():
    products_df = pd.read_csv('Products.csv', lineterminator='\n')
    nanfree_products_df = products_df.dropna(how='any')
    check_nans_removed(nanfree_products_df)
    products_df['price'] = products_df['price'].replace('[\£,]','', regex=True).astype(float)

def check_nans_removed(df_name):
    nan_check = df_name.isna().sum()
    print(nan_check)

def clean_data():
    clean_images_csv()
    clean_products_csv()

clean_data()

