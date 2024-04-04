# def fight_flangs(armType1, armType2):
#     print(armType1, armType2)
#     if armType1 == "Кавалерия" and armType2 == "Кавалерия":
#         return 0
#     elif armType1 == "Кавалерия" and armType2 == "Лучники":
#         return 1
#     elif armType1 == "Кавалерия" and armType2 == "Копейщики":
#         return 2
#     elif armType1 == "Лучники" and armType2 == "Лучники":
#         return 0
#     elif armType1 == "Лучники" and armType2 == "Кавалерия":
#         return 2
#     elif armType1 == "Лучники" and armType2 == "Копейщики":
#         return 1
#     elif armType1 == "Копейщики" and armType2 == "Кавалерия":
#         return 1
#     elif armType1 == "Копейщики" and armType2 == "Лучники":
#         return 2
#     elif armType1 == "Копейщики" and armType2 == "Копейщики":
#         return 0
#     else:
#         return -999

#Кавалерия Лучники Копейщики


# def fight_flangs(armType1, armType2):
#     print(armType1, armType2)
#     if armType1 == "Кавалерия" and armType2 == "Кавалерия":
#         return 0
#     elif armType1 == "Кавалерия" and armType2 == "Лучники":
#         return 1
#     elif armType1 == "Кавалерия" and armType2 == "Копейщики":
#         return 2
#     elif armType1 == "Лучники" and armType2 == "Кавалерия":
#         return 2
#     elif armType1 == "Лучники" and armType2 == "Лучники":
#         return 0
#     elif armType1 == "Лучники" and armType2 == "Копейщики":
#         return 1
#     elif armType1 == "Копейщики" and armType2 == "Кавалерия":
#         return 1
#     elif armType1 == "Копейщики" and armType2 == "Лучники":
#         return 2
#     elif armType1 == "Копейщики" and armType2 == "Копейщики":
#         return 0
#     else:
#         return -999


def fight_flangs(armType1, armType2):
    print(armType1, armType2)
    if armType1 == armType2:
        return 0
    elif (str(armType1), str(armType2)) in [("Кавалерия", "Лучники"), ("Лучники", "Копейщики"), ("Копейщики", "Кавалерия")]:
        return 1
    elif (str(armType1), str(armType2)) in [("Лучники", "Кавалерия"), ("Копейщики", "Лучники"), ("Кавалерия", "Копейщики")]:
        return 2
    else:
        return -999

# print(fight_flangs("Кавалерия", "Лучники"))