def build_profile(first, last, **user_info):
    """사용자에 관해 아는 것을 모두 딕셔너리로 만듭니다."""
    profile = {"first_name": first, "last_name": last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile("albert", "einstein",
                             location="princeton",
                             field="physics")

print(user_profile)
