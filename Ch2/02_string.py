# 대소문자 바꾸기
name = "ada lovelace"
print(name.title())
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# 문자열 연결
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

# 들여쓰기, 줄바꿈
# \n: 줄바꿈
# \t: 들여쓰기
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 공백 잘라내기
favorite_language = "  python  "
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
