days = ["Sunday", "Monday"]
classes = ["Math", "Science"]

for day in days:                # اللوب الكبيرة: اليوم
    for c in classes:           # اللوب الصغيرة: الحصة
        print(day, "-> Class:", c)

print("-" *2)




















































# 2. تطبيق جدول الضرب باستخدام اللوب المتداخلة
for i in range(1, 4):         
    for j in range(1, 11):     
        print(i, "x", j, "=", i * j)
    print("-" * 15)           