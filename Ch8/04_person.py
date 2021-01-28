def build_person(first_name, last_name, age=""):
    """사람에 관한 정보 딕셔너리를 반환합니다."""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("jimi", "hendrix", age=27)
print(musician)
