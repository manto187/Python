import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df["total sales"] = df["price"] * df["quantity"]
sales = df["total sales"].to_numpy()
category_sales = df.groupby("category") ["total sales"].sum()
highest = df.loc[df["total sales"].idxmax()]
lowest = df.loc[df["total sales"].idxmin()]

def pause():
    input("\npress enter to continue...")



def graph_menu():
    while True:
        print("\n-----Graph Menu-----")
        print("1. revenue by product")
        print("2. sales distribution (pie)")
        print("3. price histogram")
        print("4. sales box plot")
        print("5. correlation heatmap")
        print("6. category revenue")
        print("7. back")

        ch=input("enter your choice: ")
        if ch=="1":
            revenue_by_product()
        elif ch=="2":
            sales_distribution_pie()
        elif ch=="3":
            price_histogram()
        elif ch=="4":
            sales_box_plot()
        elif ch=="5":
            correlation_heatmap()
        elif ch=="6":
            category_revenue()
        elif ch=="7":
            break
        else: print("invalid choice")
