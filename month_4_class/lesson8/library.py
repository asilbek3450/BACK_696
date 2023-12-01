class Student:

    def __init__(self, name, age):
        self.ismi = name
        self.yoshi = age
        self.fanlari = []

    def add_subject(self, subject):
        self.fanlari.append(subject)

    def get_subjects(self):
        text = 'Talaba fanlari:\n'
        for f in self.fanlari:
            text += f + '\n'
        return text


class Subject:

    def __init__(self, name, level):
        self.nomi = name
        self.sinfi = level


sub1 = Subject('Matematika', 10)
sub2 = Subject('Fizika', 11)
sub3 = Subject('Informatika', 11)
sub4 = Subject('Ona tili', 10)

student1 = Student('Ali', 15)
student2 = Student('Vali', 16)

student1.add_subject(sub1.nomi)
student1.add_subject(sub3.nomi)
student2.add_subject(sub2.nomi)
student2.add_subject(sub4.nomi)

"""

3. O‘zaro ta’sirlar sinfi:
     - Turli fanlarni ifodalovchi bir nechta ""Subject"" sinf ob'ektlarini yaratish (masalan, ""Matematika"", ""Tarix"", ""Adabiyot"" va boshqalar).
     - “Student” sinfida obyekt yaratish va ob’ektlar ro’yxatiga bir nechta o’quv obyektlarini qo’shish.
     - talabalar haqidagi ma'lumotlarni va uning ob'ektlari ro'yxatini ko'rsatish.
    *** bu degani get_students degan metod yaratiladi, get_subjects degan metod yaratiladi.

4. Qo'shimcha funktsiyalar (ixtiyoriy):
     - Har bir fan bo'yicha o'quvchilarning baholarini ifodalash uchun dars usullarini qo'llash.
    *** bu degani Student sinfida marks degan dict yaratiladi, bunda key=fan, value=baho bo'ladi
    
     - Talabaning barcha fanlar bo‘yicha GPAni hisoblash usulini yaratish.
    *** bu degani hamma fandan olingan o'rtacha baho 
    
     - o‘rtacha ball olgan “yuqori” va “tekis” o‘quvchilarni aniqlash funksiyasini amalga oshirish.
    *** bu degani hamma fanni GPA larini qo'shib nechta fan bo'lsa shunga bo'linadi, 
        agar 3.5 dan katta bo'lsa bu degani "yuqori", 3.5 dan kichik bo'lsa "passiv" degan ma'lumot chiqadi.

"""
