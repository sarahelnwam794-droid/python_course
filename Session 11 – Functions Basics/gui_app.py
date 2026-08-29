

import tkinter as tk
from tkinter import messagebox


def show_message():
    messagebox.showinfo("رسالة تفاعلية", "أهلاً بيك يا بطل! التطبيق اشتغل في نافذة حقيقية 🎉")

window = tk.Tk()
window.title("برنامجي الأول - واجهة مستخدم")
window.geometry("300x200")

btn = tk.Button(window, text="اضغط هنا يا شطورة", command=show_message, bg="orange", fg="white")
btn.pack(expand=True)

window.mainloop()