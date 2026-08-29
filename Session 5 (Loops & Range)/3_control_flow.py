# # 1. استخدام len() لمعرفة طول القائمة أو الكلمة مع range()
# buddies = ["Sara", "abdo", "Ahmad"]
# for index in range(len(buddies)):
#     print(index)










































# # 2. فحص الأعداد الزوجية والفردية باستخدام علامة المودلس (%)
# for index in range(10):
#     if index % 2 == 0:
#         print(index, "is an even number")
#     else:
#         print(index, "is an odd number")








































# # 3. البحث عن عنصر والتوقف الفوري باستخدام break
# colors = ["Red", "Green", "Blue", "Yellow"]
# for color in colors:
#     if color == "Blue":
#         print(color, "is found! Stop searching.")
#         break 
#     else:
#         print("is not the target.")











































# # 4. تخطي عنصر معين باستخدام continue
colors = ["Red", "Green", "Blue", "Yellow", "Orange"]
for color in colors:
    if color == "Blue":
        continue
    print(color, "is a great color")