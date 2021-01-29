# 8-3 티셔츠
def make_shirt(size, message):
    """티셔츠 정보를 출력합니다."""
    print("\n티셔츠의 사이즈는 " + size + "입니다.")
    print("티셔츠에는 '" + message + "' 라는 문구가 적혀 있습니다.")


make_shirt("L", "I Love Seoul")  # 위치형 매개변수
make_shirt(size="S", message="Hotteok Mind")  # 키워드 매개변수


# 8-4 L 사이즈
def make_shirt_2(size="L", message="I love Python"):
    """티셔츠 정보를 출력합니다."""
    print("\n티셔츠의 사이즈는 " + size + "입니다.")
    print("티셔츠에는 '" + message + "' 라는 문구가 적혀 있습니다.")


make_shirt_2()  # 기본값 활용
make_shirt_2(size="M", message="Work Out!")


# 8-5 도시
def describe_city(city, country="한국"):
    """도시의 위치에 대한 설명을 출력합니다."""
    print(city + "은/는 " + country + "에 있습니다.")


describe_city("서울")
describe_city("부산")
describe_city("뉴욕", "미국")