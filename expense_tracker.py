import matplotlib.pyplot as plt
import pandas as pd

def get_expenses():
    expenses = []
    while True:
        try:
            amount = float(input("Enter expense amount (or -1 to finish): "))
            if amount == -1:
                break
            category = input("Enter expense category: ")
            expenses.append({"amount": amount, "category": category})
        except ValueError:
            print("Invalid input. Please enter a number.")
    return expenses

def visualize_expenses(expenses):
    df = pd.DataFrame(expenses)
    category_sums = df.groupby("category")["amount"].sum()

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    category_sums.plot(kind="bar", rot=0)
    plt.title("Expense Distribution by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    expenses = get_expenses()
    if expenses:
        visualize_expenses(expenses)
