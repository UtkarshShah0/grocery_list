import sqlite3

groceries = [
    "apples", 
    "bananas", 
    "clemintines", 
    "dill", 
    "eggs", 
    "flour", 
    "granola", 
    "honey",
    "ice cream",
    "juice",
    "ketchup",
    "lemon",
    "margarine",
    "onion",
    "potatoes",
    "rosmary",
    "salt",
    "thyme",
    "vinegar",
    "pears",
    "watermelon",
    "cucumbers",
    "garlic",
    "carrots",
    "pastries",
    "eggplants",
    "milk",
    "coffee",
    "tea",
    "rice",
    "noodles",
    "lentils",
    "sweet potatoes",
    "strawberries",
    "cranberries",
    "mangoes",
    "peppers",
    "zuccinis",
    "lime",
    "broth",
    "mushrooms",
    "chicken",
    "pork",
    "fish",
    "cream",
    "paprika",
    "turmeric",
    "cinamon",
    "pumpkin",
    "basil",
    "tomatoes",
    "bread",
    "cake",
    "chocolate",
    "gum",
    "pineapple",
    "oranges",
    "lettuce",
    "cheese",
    "cilantro"
    ] 

groceries = sorted(groceries)

connection = sqlite3.connect("grocery_list.db")
cursor = connection.cursor()

cursor.execute("create table groceries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(groceries)):
    cursor.execute("insert into groceries (name) values (?)", [groceries[i]])
    print("added", groceries[i])

connection.commit()
connection.close()