base_money = 1000
apr = 0.05
money_increased = 0

for i in range(11):
    money_increased += base_money + (base_money*apr)
    print(f"After {i} year(s) total money has increased to {money_increased}")
