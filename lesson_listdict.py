fruits = ["apple","banana","orange","grape"]
for fruit in fruits:
    print(fruit)

person = {
    "name" : "太郎",
    "age" : 30
}
print(person["name"])
print(person["age"])

prefutures = ["北海道", "青森", "岩手", "宮城", "秋田"]
for pref in prefutures:
    if pref == "北海道":
        print("北海道はでっかいど～")
    else:
        print(pref)

population = {
    "東京":1400,
    "大阪":880,
    "福岡":510
}

for key, value in population.items():
    print(f"{key}の人口は{value}万人です")