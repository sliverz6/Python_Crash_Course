# 외계인을 저장할 빈 리스트를 만듭니다.
aliens = []

# 녹색 외계인 30명을 만듭니다.
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# 처음 외계인 3명의 정보를 바꿉니다.
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

# 처음 5명을 출력합니다.
for alien in aliens[:5]:
    print(alien)
print("...")

# 외계인이 몇 명 만들어졌는지 출력합니다.
print("Total number of aliens: " + str(len(aliens)))
