s=input("Item: ")
s=s.lower()
fruits=["apple",
        "avocado",
        "banana",
        "cantaloupe",
        "grapefruit",
        "grapes",
        "honeydew melon",
        "kiwifruit",
        "lemon",
        "lime",
        "nectarine",
        "orange",
        "peach",
        "pear",
        "pineapple",
        "plums",
        "strawberries",
        "sweet cherries",
        "tangerine",
        "watermelon",
        ]
calories=[130, 50, 110, 50, 60, 90, 50, 90, 15, 20, 60, 80, 60, 100, 50, 70, 50, 100, 50, 80]

for i in range(len(fruits)):
    if fruits[i]==s:
        print("Calories:",calories[i])
        break