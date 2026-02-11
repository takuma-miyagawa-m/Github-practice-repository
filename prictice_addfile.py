a = input("名前を入力してください: ")
print("\n" + "=" * 40)

for i in range(30):
    status = "未成年" if i < 18 else "成人"
    print(f"{i}歳の{a}さん → {status}")

print("=" * 40 + "\n")