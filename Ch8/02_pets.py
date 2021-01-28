def describe_pet(pet_name, animal_type="dog"):
    """애완동물에 관한 정보를 출력합니다."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet("harry")  # 위치 매개변수
describe_pet(pet_name="harry", animal_type="hamster")  # 키워드 매개변수
