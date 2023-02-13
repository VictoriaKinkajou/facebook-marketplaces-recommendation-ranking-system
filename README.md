# Facebook Marketplace Recommendation Ranking System

## Milestone_3

The data is in products.csv, images.csv and a folder of jpeg images. I have imported pandas into the python files, which is an open-source library that facilitates data table manipulation.

clean_tabular_data.py contains code that checks for null values and removes rows containing NaNs if they are present. It also removes the pound signs and commas from each value in the price column, and converts it from string to float. 

Sandbox.ipynb contains the code for adding categories to the image IDs. The code extracts the root category from the category colummn of products.csv, removes duplicate categories and assigns a numerical label to each resulting root category. These category labels are applied to the image IDs in order to use the images as training data.

clean_images.py contains code to re-size the jpeg images and adjust the colour channels, so all images are consistent.

