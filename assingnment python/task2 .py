# ---------------------------------------------------
# Author: Shreya Upadhyay
# Date: 04-Oct-2025
# Project: Daily Calorie Tracker
# ---------------------------------------------------

# """
# This tool helps you keep track of your daily calorie intake.
# You can log the food you eat, record its calorie value, 
# and check your total calories consumed throughout the day.
# """

# # Welcome message
# print(" Welcome to Daily Calorie Tracker! ")
# print("Track your meals, log calories, and stay on top of your fitness goals.")
# print("Let's get started!")

# Lists to store meal data
meals = []
calories = []

# Ask user how many meals to enter
num_meals = int(input("How many meals do you want to log today? "))

# Collect meal names & calories
for i in range(num_meals):
    meal_name = input("Enter name of meal #{i+1}: ")
    calorie_amount = float(input("Enter calories for {meal_name}: "))
    
    # Store in lists
    meals.append(meal_name)
    calories.append(calorie_amount)

# Display summary
print("--- Daily Meal Log ---")
for i in range(num_meals):
    print("{meals[i]}: {calories[i]} calories")

print(" Data collected successfully!")
