# ---------------------------------------------------
# Author: Shreya Upadhyay
# Date: 04-Oct-2025
# Project: Daily Calorie Tracker
# ---------------------------------------------------

"""
This tool helps you keep track of your daily calorie intake.
You can log the food you eat, record its calorie value, 
and check your total calories consumed throughout the day.
"""

import datetime

# Welcome message
print("🍎 Welcome to Daily Calorie Tracker! 🍎")
print("Track your meals, log calories, and stay on top of your fitness goals.")
print("Let's get started!\n")

# Lists to store meal data
meals = []
calories = []

# Ask user how many meals to enter
num_meals = int(input("How many meals do you want to log today? "))

# Collect meal names & calories
for i in range(num_meals):
    meal_name = input(f"\nEnter name of meal #{i+1}: ")
    calorie_amount = float(input(f"Enter calories for {meal_name}: "))
    
    meals.append(meal_name)
    calories.append(calorie_amount)

# --- Calculations ---
total_calories = sum(calories)
average_calories = total_calories / num_meals

# --- Daily Limit ---
daily_limit = float(input("\nEnter your daily calorie limit: "))

if total_calories > daily_limit:
    status = f"⚠️ Warning! You exceeded your limit by {total_calories - daily_limit} calories."
else:
    status = "✅ Good job! You stayed within your daily calorie limit."

# --- Formatted Summary ---
print("\n--- Daily Calorie Report ---")
print(f"{'Meal Name':<15}{'Calories'}")
print("-" * 30)

for i in range(num_meals):
    print(f"{meals[i]:<15}{calories[i]}")

print("-" * 30)
print(f"{'Total:':<15}{total_calories}")
print(f"{'Average:':<15}{round(average_calories, 2)}")
print(status)

# --- Bonus: Save to File ---
save = input("\nDo you want to save this report to a file? (yes/no): ").strip().lower()

if save == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "daily_report.txt"
    
    with open(filename, "w") as file:
        file.write("🍎 Daily Calorie Tracker Report 🍎\n")
        file.write(f"Date & Time: {timestamp}\n")
        file.write("-" * 40 + "\n")
        file.write(f"{'Meal Name':<15}{'Calories'}\n")
        file.write("-" * 40 + "\n")
        
        for i in range(num_meals):
            file.write(f"{meals[i]:<15}{calories[i]}\n")
        
        file.write("-" * 40 + "\n")
        file.write(f"{'Total:':<15}{total_calories}\n")
        file.write(f"{'Average:':<15}{round(average_calories, 2)}\n")
        file.write(status + "\n")
    
    print(f"\n📂 Report saved successfully as '{filename}'")
else:
    print("\nReport not saved. ✅")

