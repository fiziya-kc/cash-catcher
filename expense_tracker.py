import csv
import os
from datetime import datetime

FILENAME = 'expenses.csv'

# Ensure the CSV file exists with headers
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'category', 'amount', 'description'])

def add_expense():
    print('\n📝 Add a New Expense')
    date = input('📅 Enter date (YYYY-MM-DD) [press Enter for today]: ')
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    category = input('📂 Enter category (e.g., Food, Travel): ')
    # Validate amount input
    while True:
        amount = input('💰 Enter amount (numbers only): ')
        try:
            float(amount)
            break
        except ValueError:
            print('❗ Please enter a valid number for amount.')
    description = input('🖊️ Enter description (optional): ')
    with open(FILENAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])
    print('✅ Expense added!')

def view_expenses():
    print('\n📖 All Expenses:')
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        count = 0
        for row in reader:
            count += 1
            print(f"{count}. 📅 {row[0]} | 📂 {row[1]} | 💰 {row[2]} | 🖊️ {row[3]}")
        if count == 0:
            print('No expenses found yet. Add your first one!')

def summarize_expenses():
    print('\n📊 Expense Summary:')
    total = 0.0
    category_totals = {}
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            try:
                amount = float(row[2])
            except ValueError:
                continue
            total += amount
            category = row[1]
            category_totals[category] = category_totals.get(category, 0) + amount
    print(f"\n💵 Total spent: {total}")
    print('📂 By category:')
    if not category_totals:
        print('No expenses to summarize yet.')
    for cat, amt in category_totals.items():
        print(f"  - {cat}: {amt}")

def main():
    print('''\n==============================\n  💸 Welcome to Expense Tracker! 💸\n==============================\nEasily add, view, and summarize your expenses.\nLet's manage your money together!\n''')
    while True:
        print('\nMain Menu:')
        print('1️⃣  Add Expense')
        print('2️⃣  View Expenses')
        print('3️⃣  Summarize Expenses')
        print('4️⃣  Exit')
        choice = input('👉 Choose an option (1-4): ')
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summarize_expenses()
        elif choice == '4':
            print('👋 Goodbye! Have a great day!')
            break
        else:
            print('❗ Invalid choice, please enter 1, 2, 3, or 4.')

if __name__ == '__main__':
    main() 