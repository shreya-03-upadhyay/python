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

# --- Formatted Summary Table ---
print("\n--- Daily Calorie Report ---")
print(f"{'Meal Name':<15}{'Calories'}")
print("-" * 30)

for i in range(num_meals):
    print(f"{meals[i]:<15}{calories[i]}")

print("-" * 30)
print(f"{'Total:':<15}{total_calories}")
print(f"{'Average:':<15}{round(average_calories, 2)}")
