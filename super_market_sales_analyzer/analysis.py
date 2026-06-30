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


def revenue_by_product():
    plt.figure(figsize=(10,5))
    plt.bar(df["product"],df["total sales"])
    plt.title("revenue by product")
    plt.xlabel("product")
    plt.ylabel("revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def sales_distribution_pie():
    plt.figure(figsize=(6,6))
    plt.pie(category_sales.values, labels=category_sales.index, autopct="%1.1f")``
    plt.title("sales distribution by category")
    plt.show()

def price_histogram():
    plt.figure(figsize=(8,5))
    plt.hist(df["price"], bins=6)
    plt.title("product price distribution")
    plt.xlabel("price")
    plt.ylabel("frequency")
    plt.show()

def sales_box_plot():
    plt.figure(figsize=(6,5))
    sns.boxplot(y=df["total sales"])
    plt.title("sales distribution")
    plt.show()

def correlation_heatmap():
    plt.figure(figsize=(6,4))
    sns.heatmap(df.select_dtypes(include="number").corr(), annot=True, cmap="Blues")
    plt.title("correlation heatmap")
    plt.show()
    
def category_revenue():
    plt.figure(figsize=(8,5))
    sns.barplot(x=category_sales.index, y=category_sales.values)
    plt.title("revenue by category")
    plt.xlabel("category")
    plt.ylabel("revenue")
    plt.show()

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

while True:
    print("\n--------- SUPERMARKET SALES ANALYZER ---------")
    print("1. view dataset")
    print("2. view statistics")
    print("3. highest and lowest selling products")
    print("4. category wise sales")
    print("5. save reports")
    print("6. view graphs")
    print("7. exit")
    choice=print("enter your choice: ")

    if choice=="1":
        print(df)
        pause()
    elif choice=="2":
        print(f"total revenue: {np.sum(sales)}")
        print(f"average revenue: {np.mean(sales):.2f}")
        print(f"maximum sales: {np.max(sales)}")
        print(f"minimum sales: {np.min(sales)}")
        print(f"median sales: {np.median(sales)}")
        print(f"standard deviation: {np.std(sales):.2f}")
        pause()
    elif choice=="3":
        print("\nhighest selling product:\n", highest)
        print("\nlowest selling product:\n", lowest)
        pause()
    elif choice=="4":
        print(category_sales)
        pause()
    elif choice=="5":
        df.to_csv("sales.csv", index=False)
        print("sales report saved successfully.")
        pause()
    elif choice=="6":
        graph_menu()
    elif choice=="7":
        print("goodbye!")
        break
    else:
        print("invalid choice")
    