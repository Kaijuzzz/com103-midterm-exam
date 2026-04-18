name = input("Student name: ")
while True:
    try:
        budget = float(input("Weekly budget: "))
        if budget < 0:
            print("Budget cannot be negative.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a number only.")

categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "Snacks",
    "Entertainment"
]

examples = [
    "Lunch, snacks, coffee",
    "Bus, jeepney, ride-share",
    "Load, data plan, WiFi top-up",
    "Milktea, Cake, Ice Cream",
    "Games, movies, hangout"
]

print("\n==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")
for i in range(len(categories)):
    print(f" {i+1}. {categories[i]:<20} [e.g. {examples[i]}]")
print("==========================================\n")

logged_expenses = []
total_spent = 0

for i in range(1, 5):
    print(f"--- EXPENSE {i} ---")
    cat_choice = int(input("Category (0 to skip): "))
    
    if cat_choice == 0:
        continue
    elif 1 <= cat_choice <= 5:
        desc = input("Description: ")
        amt = float(input("Amount: "))
        
        alert = ""
        if amt > (budget * 0.25):
            alert = "! High Expense Alert!"
            
        logged_expenses.append({
            "category": categories[cat_choice - 1],
            "description": desc,
            "amount": amt,
            "alert": alert
        })
        total_spent += amt

remaining = budget - total_spent
status = "Good at Budgeting." if remaining >= 0 else "Overspent! Reduce spending."

print(f"\n======================================================")
print(f"     {name.upper()} -- WEEKLY EXPENSE LOG")
print(f"======================================================")
print(f"  Weekly Budget  : P{budget:.2f}")

for idx, item in enumerate(logged_expenses, 1):
    print(f"  [{idx}] {item['category']}")
    # Added padding (:35) for description and right-alignment (:>8.2f) for price
    print(f"      {item['description']:35} P{item['amount']:>8.2f}  {item['alert']}")

print(f"------------------------------------------------------")
print(f"  Total Spent    : P{total_spent:>8.2f}")
print(f"  Remaining      : P{remaining:>8.2f}")
print(f"  Status         : {status}")
print(f"======================================================")