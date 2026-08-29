# تمرين دليل التليفونات المصغر للطلاب
my_contacts = {
    "Ahmed": "0111222333",
    "Sara": "0122333444",
    "Omar": "0155666777"
}

print(f"Original Contacts: {my_contacts}")

# إضافة صديق جديد بطريقة الـ input أو التعديل المباشر
new_name = input("Enter a new friend's name: ")
new_phone = input("Enter their phone number: ")
my_contacts[new_name] = new_phone

# طباعة الدليل بعد التعديل والتحديث
print("\n--- Updated Contacts List ---")
for name, phone in my_contacts.items():
    print(f"Name: {name} | Phone: {phone}")