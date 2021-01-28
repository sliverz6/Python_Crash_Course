# 슬라이싱(slicing)
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

# 슬라이스에 반복문 실행
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
