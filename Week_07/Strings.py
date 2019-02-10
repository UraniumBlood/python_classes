# hello = 'Hello World'
# print(hello[1:6])
#
# hello = "Hello World"
# print(hello[0])

a = "hello"
b = "python"
print(a + b)
#
# print(b*5)

# lis
# s = "I am a LeBron James"
# print(s)
# print(s.lower())
# print(s.capitalize())
# print(s.upper())
# print(s.isalpha())

# #alp = "abcdefg1"
# print("alp.isalpha()", alp.isalpha())
# print("alp.isalnum()", alp.isalnum())
# print("alp.replace", alp.replace("abcdefg", "22222000000s"))
# alp2 = alp.replace("abcdefg", "x")
# print(alp2)
# final = alp2.replace("1", "44444")
# print(final)

# def string_to_uppercase(s):
#      y = s.upper()
#      return y

# output = string_to_uppercase("I am a boy")
# print(output)





# list_hero = ["Captain America", "Dr. Strange", "Spider-Man"]
# for hero in list_hero:
#     print(string_to_uppercase(hero))
#
# def string_to_lower(s):
#     y = s.lower()
#     return y
# list_hero = ["Captain America", "Dr. Strange", "Spider-Man"]
# for hero in list_hero:
#      print(string_to_lower(hero))

# replace = list_hero.replace("a", "1")

def string_to_replace(s):
    y = s.replace("a", "1")
    return y

list_hero = ["Captain America", "Dr. Strange", "Spider-Man"]
for hero in list_hero:
    replace = string_to_replace(hero)
    print(replace)




