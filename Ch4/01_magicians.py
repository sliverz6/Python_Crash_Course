# 리스트 반복문
# magicians = ["alice", "david", "carolina"]
# for magician in magicians:
#     print(magician)


# 반목문 안에서 더 많은 일 하기
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")


# 반복문 블록이 끝나고 한 번만 실행
print("Thank you, everyone. That was a great magic show!")
