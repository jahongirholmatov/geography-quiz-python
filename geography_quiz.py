import random
quiz_data = [
    {"q": "Which country has the largest area?\na) Russia, b) Canada, c) Argentina, d) China", "a": "a"},
    {"q": "Which country has the smallest area?\na) UK, b) Tajikistan, c) North Korea, d) Vatican", "a": "d"},
    {"q": "What is the capital city of Tajikistan?\na) Tashkent, b) Dushanbe, c) Samarkand, d) Bukhara", "a": "b"},
    {"q": "How many continents are there on Earth?\na) 7, b) 11, c) 6, d) 5", "a": "a"},
    {"q": "Which is the largest ocean in the world?\na) Pacific Ocean, b) Indian Ocean, c) Atlantic Ocean, d) Arctic Ocean", "a": "a"},
    {"q": "What is the name of the longest river in the world?\na) Nile River, b) Mississippi River, c) Amazon River, d) Yenisei River", "a": "a"},
    {"q": "Madagascar is located near which continent?\na) Europe, b) Asia, c) Africa, d) Australia", "a": "c"},
    {"q": "Which ocean is located between Africa and Australia?\na) Pacific Ocean, b) Indian Ocean, c) Atlantic Ocean, d) Arctic Ocean", "a": "b"},
    {"q": "Which is the largest island in the world?\na) Australia, b) Madagascar, c) Greenland, d) Borneo", "a": "c"},
    {"q": "What is the capital city of France?\na) Madrid, b) Rome, c) Lisbon, d) Paris", "a": "d"}
]

random.shuffle(quiz_data)

score = 0 

print("Welcome to the Global Geography Quiz! 🌏")
print("---------------------------------------")

for item in quiz_data:
    print("\n" + item["q"])

    answer = input("Your answer (a, b, c, d): ").lower()
    
    if answer == item["a"]:
        print("Correct! 🎉")
        score += 1
    else:
        print(f"False! The correct answer was: {item['a']}")

print("-" * 30)

print(f"Game Over! Your total score is: {score}/{len(quiz_data)}")
