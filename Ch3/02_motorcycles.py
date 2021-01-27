motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"  # 리스트 요소 수정
print(motorcycles)

motorcycles.append("ducati")  # 리스트 요소 추가
print(motorcycles)

motorcycles.insert(1, "ducati")  # 1번 인덱스에 요소 추가
print(motorcycles)

del motorcycles[0]  # 0번 인덱스 제거
print(motorcycles)

popped_motorcycle = motorcycles.pop()  # 맨 끝에 요소 꺼내기
print(motorcycles)
print(popped_motorcycle)

motorcycles.remove("yamaha")  # 값으로 요소 제거
print(motorcycles)