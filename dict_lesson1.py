fruits = {
    "りんご": 120,
    "バナナ": 80,
    "みかん": 100
}

print(fruits)

for name, price in fruits.items():
    print(f"{name} は {price} 円です")


# 値の更新
fruits["バナナ"] = 90

# 新しいフルーツを追加
fruits["ぶどう"] = 150

# フルーツを削除
del fruits["みかん"]

# 確認
for name, price in fruits.items():
    print(f"{name}：{price}円")


stock = {
    "ペン": 12,
    "ノート": 5,
    "消しゴム": 0
}

for item, quantity in stock.items():
    if quantity == 0:
        print(f"{item}は在庫なしです。発注してください")
    else:
        print(f"{item}は在庫{quantity}個です")


cat_status = {
    "みやこまる": 4.6,
    "イヴ": 4.5
}

for name, weight in cat_status.items():
    if weight > 4.5:
        print(f"{name}は太り過ぎです")
    else:
        print(f"{name}は適正体重です")