# 딕셔너리 안에 리스트 담기

# 주문받은 피자에 관한 정보를 저장합니다.
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
}

# 주문을 요약합니다.
print("You ordered a " + pizza["crust"] + "-crust pizza" +
      "with the following toppings:")

for topping in pizza["toppings"]:
    print("\t" + topping)
