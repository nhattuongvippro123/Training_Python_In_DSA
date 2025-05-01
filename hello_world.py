# print("Hello, Python!")
# name = "Tuong"
# age = 26
# is_student = True
# print(name, age, is_student)
# a = int(input("Nhap so a: "))
# b = int(input("Nhap so b: "))
#
# print("tong", a+b)
# print("A lon hon B?", a>b)
#
# score = int(input("Nhap diem: "))
#
# if score >= 90:
#     print("gioi")
# elif score >= 70:
#     print("Kha")
# else:
#     print("Trung binh hoac yeu")
# from enum import CONTINUOUS
# from operator import truediv
# from random import choices
# from collections.abc import Hashable
# from multiprocessing.reduction import duplicate

# for i in range(1,6):
#     print(i)
#
# n = int(input("nhap n:"))
# while n <5:
#     print(n)
#     n+=1

# fruits = ["apple", "banana", "cherry"]
# fruits.pop(1)
# fruits.append("abc")
# print(fruits)

# person = {"name": "Tường", "age": 25}
# person["age"] = 26
# print(person["name"], "-", person["age"])

# print("=== MÁY TÍNH CƠ BẢN ===")
#
# while True:
#     print("\nChọn phép tính:")
#     print("1. Cộng")
#     print("2. Trừ")
#     print("3. Nhân")
#     print("4. Chia")
#     print("0. Thoát")
#
#     choice = input("Nhập lựa chọn (0-4): ")
#
#     if choice == "0":
#         print("Đã thoát chương trình. Tạm biệt!")
#         break  # Thoát vòng lặp
#
#     if choice not in ["1", "2", "3", "4"]:
#         print("⚠️ Lựa chọn không hợp lệ! Vui lòng chọn từ 0 đến 4.")
#         continue  # Quay lại đầu vòng lặp để chọn lại
#
#     try:
#         a = float(input("Nhập số thứ nhất: "))
#         b = float(input("Nhập số thứ hai: "))
#     except ValueError:
#         print("⚠️ Vui lòng nhập số hợp lệ!")
#         continue
#
#     if choice == "1":
#         print("Kết quả:", a + b)
#     elif choice == "2":
#         print("Kết quả:", a - b)
#     elif choice == "3":
#         print("Kết quả:", a * b)
#     elif choice == "4":
#         if b != 0:
#             print("Kết quả:", a / b)
#         else:
#             print("⚠️ Không thể chia cho 0!")


#set
# a = {5, 1, 2, 3 , 7}
# b = {2, 3, 4, 5 ,6 , 8}
#
# print(a | b)   # union: {1, 2, 3, 4}
# print(a & b)   # intersection: {2, 3}
# print(b - a)   # difference: {1}


# def say_hello(name):
#     print(f"Xin chào, {name}!")
#
# say_hello(input("Nhap ten:"))

# def cong(a, b):
#     return a + b
#
# kq = cong(2, 3)
# print(kq)  # 👉 5


# add = lambda x, y: x + y
# print(add(3, 4))  # 👉 7

# def tong(*args):
#     return sum(args)
#
# print(tong(1, 2, 3))   # 👉 6

# def demo(*args):
#     print(args)
#
# demo(10, 20, 30)  # 👉 (10, 20, 30)

# def thong_tin(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# thong_tin(ten="An", tuoi=22, dia_chi="Đà Nẵng")
# # 👉 ten: An
# # 👉 tuoi: 22
# # 👉 dia_chi: Đà Nẵng

# def demo(*args, **kwargs):
#     print("Args:", args)
#     print("Kwargs:", kwargs)
#
# demo(1, 2, name="An", job="Dev")

# class Thanh:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         print(f"Xin chào, mình là {self.name}, {self.age} tuổi.")
# p1 = Thanh("Thanh",22)
# p1.greet()

# class TinhTong:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def tinh(self):
#         print(self.a + self.b)
# bai1 = TinhTong(10,11)
# bai1.tinh()

# class Car:
#     def __init__(self, brand,color, year):
#         self.brand = brand
#         self.color = color
#         self.year = year
#
#     def show_info(self):
#         print(f"{self.brand} | {self.color} | {self.year}")
#
# car1 = Car("BMW", "red", 2021)
# car1.show_info()
# car2 = Car("Lamboghini", "yellow", 1999)
# car2.show_info()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         print(f"Xin chào, mình là {self.name}, {self.age} tuổi.")
#
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id
#
#     def show_id(self):
#         print(f"{self.name} | {self.age} | {self.student_id}")
#
# sv = Student("John", 25, "SV001")
# sv.greet()
# sv.show_id()

# class Contact:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#     def show(self):
#         print(f"{self.name}: {self.phone}")
#
#
# class PhoneBook:
#     def __init__(self):
#         self.contacts = []
#
#     def add_contact(self, contact):
#         self.contacts.append(contact)
#
#     def search_contact(self, name):
#         for contact in self.contacts:
#             if contact.name.lower() == name.lower():
#                 contact.show()
#                 return
#         print("❌ Không tìm thấy.")
#
#     def delete_contact(self, name):
#         for contact in self.contacts:
#             if contact.name.lower() == name.lower():
#                 self.contacts.remove(contact)
#                 print(f"🗑️ Đã xóa liên hệ: {name}")
#                 return
#         print("❌ Không tìm thấy để xóa.")
#
#     def show_all(self):
#         if not self.contacts:
#             print("📭 Danh bạ trống.")
#         else:
#             print("\n📒 Danh bạ:")
#             for contact in self.contacts:
#                 contact.show()
#
#
# # ===== Giao diện người dùng =====
# phonebook = PhoneBook()
#
# while True:
#     print("\n===== MENU QUẢN LÝ DANH BẠ =====")
#     print("1. Thêm liên hệ mới")
#     print("2. Tìm liên hệ theo tên")
#     print("3. Hiển thị tất cả liên hệ")
#     print("4. Xóa liên hệ")
#     print("0. Thoát")
#
#     choice = input("👉 Nhập lựa chọn (0-4): ")
#
#     if choice == "1":
#         name = input("Nhập tên: ")
#         phone = input("Nhập số điện thoại: ")
#         contact = Contact(name, phone)
#         phonebook.add_contact(contact)
#         print("✅ Đã thêm liên hệ.")
#
#     elif choice == "2":
#         name = input("Nhập tên cần tìm: ")
#         phonebook.search_contact(name)
#
#     elif choice == "3":
#         phonebook.show_all()
#
#     elif choice == "4":
#         name = input("Nhập tên cần xóa: ")
#         phonebook.delete_contact(name)
#
#     elif choice == "0":
#         print("👋 Tạm biệt!")
#         break
#
#     else:
#         print("⚠️ Lựa chọn không hợp lệ. Hãy nhập từ 0 đến 4.")



# class Contact:
#     def __init__(self,name,phone):
#         self.name = name
#         self.phone = phone
#     def show(self):
#         print(f"{self.name} : {self.phone}")
#
# class Phonebook:
#     def __init__(self):
#         self.contacts = []
#     def add_contract(self,contact):
#         self.contacts.append(contact)
#     def show_contact_name(self, name):
#         for contact in self.contacts:
#             if contact.name.lower() == name.lower():
#                 contact.show()
#                 return
#             else:
#                 print("Contact not found")
#     def show_contact(self):
#         if not self.contacts:
#             print("Trong")
#         else:
#             for contact in self.contacts:
#                 contact.show()
#     def delete_contact(self, name):
#         for contact in self.contacts:
#             if contact.name.lower() == name.lower():
#                 self.contacts.remove(contact)
# phonebook = Phonebook()
# while True:
#     print("Nhap dieu can lam:")
#     print("1. THem lien he:")
#     print("2. Show lien he theo ten:")
#     print("3. Show tat ca lien he:")
#     print("4. xoa lien he:")
#     print("5. thoat chuong trinh:")
#
#     choice = input("nhap dieu can lam:")
#
#     if choice == "1":
#         name = input("Nhap ten:")
#         phone = input("Nhap so dien thoai")
#         contact = Contact(name,phone)
#         phonebook.add_contract(contact)
#         print("Lien he da duoc them")
#         print("====================================")
#     elif choice == "2":
#         name = input("Nhap ten:")
#         phonebook.show_contact_name(name)
#         print("Lien he da duoc loc ra")
#         print("====================================")
#     elif choice == "3":
#         phonebook.show_contact()
#         print("tat ca lien he da duoc show")
#         print("====================================")
#     elif choice == "4":
#         name = input("Nhap lien he can xoa:")
#         phonebook.delete_contact(name)
#         print("da xoa lien he")
#         print("====================================")
#     elif choice == "5":
#         break
#     else:
#         print("Nhap cho dung ko tao danh")

#ket thuc luyen class

#OOP
# import json
# import os
#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return f"{self.name} nói: ..."
#
#     # def to_data(self):
#     #     return f"{self.__class__.__name__}:{self.name}"
#
#     def to_dict(self):
#         return {
#             "type": self.__class__.__name__,
#             "name": self.name
#         }
#
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} nói: Meo meo!"
#
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} nói: Gâu gâu!"
#
# class Zoo:
#     def __init__(self):
#         self.animals = []
#         self.load_from_file()
#
#     def add_animal(self, animal):
#         self.animals.append(animal)
#         self.save_to_file()
#
#     def show_animals(self):
#         if not self.animals:
#             print("🐾 Sở thú đang trống.")
#         else:
#             print("🐾 Danh sách các con vật trong sở thú:")
#             for animal in self.animals:
#                 print(animal.speak())
#
#     def count_animals_by_type(self, animal_type):
#         count = sum(isinstance(a, animal_type) for a in self.animals)
#         print(f"Số lượng {animal_type.__name__}: {count}")
#
#     def remove_animal_by_name(self, name):
#         for a in self.animals:
#             if a.name.lower() == name.lower():
#                 self.animals.remove(a)
#                 self.save_to_file()
#                 print(f"🗑️ Đã xóa {a.name} khỏi sở thú.")
#                 return
#         print("❌ Không tìm thấy con vật nào với tên đó.")
#
#     def rename_animal(self, old_name, new_name):
#         for a in self.animals:
#             if a.name.lower() == old_name.lower():
#                 a.name = new_name
#                 self.save_to_file()
#                 print(f"✏️ Đã đổi tên thành {new_name}.")
#                 return
#         print("❌ Không tìm thấy con vật nào với tên đó.")
#
#     def show_by_type(self):
#         cats = [a for a in self.animals if isinstance(a, Cat)]
#         dogs = [a for a in self.animals if isinstance(a, Dog)]
#
#         print("\n🐱 Danh sách Mèo:")
#         if cats:
#             for c in cats:
#                 print(c.speak())
#         else:
#             print("Không có mèo.")
#
#         print("\n🐶 Danh sách Chó:")
#         if dogs:
#             for d in dogs:
#                 print(d.speak())
#         else:
#             print("Không có chó.")
#
#     def save_to_file(self):
#         data = [animal.to_dict() for animal in self.animals]
#         with open("zoo_data.json", "w", encoding="utf-8") as f:
#             json.dump(data, f, ensure_ascii=False, indent=2)
#
#     def load_from_file(self):
#         if not os.path.exists("zoo_data.json"):
#             return
#         with open("zoo_data.json", "r", encoding="utf-8") as f:
#             data = json.load(f)
#             for item in data:
#                 type_str = item["type"]
#                 name = item["name"]
#                 if type_str == "Cat":
#                     self.animals.append(Cat(name))
#                 elif type_str == "Dog":
#                     self.animals.append(Dog(name))
#
# # ============ MENU ==============
# def show_menu():
#     print("\n===== MENU QUẢN LÝ SỞ THÚ =====")
#     print("1. 🐱 Thêm mèo")
#     print("2. 🐶 Thêm chó")
#     print("3. 📋 Hiển thị tất cả động vật")
#     print("4. 🔢 Đếm số lượng mèo")
#     print("5. 🔢 Đếm số lượng chó")
#     print("6. 🗑️ Xóa động vật theo tên")
#     print("7. ✏️ Đổi tên động vật")
#     print("8. 📂 Thống kê theo loại")
#     print("0. 🚪 Thoát")
#
# # ========== MAIN ==========
# zoo = Zoo()
#
# while True:
#     show_menu()
#     choice = input("👉 Nhập lựa chọn (0-8): ")
#
#     if choice == "1":
#         name = input("Nhập tên mèo: ")
#         zoo.add_animal(Cat(name))
#         print("✅ Đã thêm mèo vào sở thú.")
#
#     elif choice == "2":
#         name = input("Nhập tên chó: ")
#         zoo.add_animal(Dog(name))
#         print("✅ Đã thêm chó vào sở thú.")
#
#     elif choice == "3":
#         zoo.show_animals()
#
#     elif choice == "4":
#         zoo.count_animals_by_type(Cat)
#
#     elif choice == "5":
#         zoo.count_animals_by_type(Dog)
#
#     elif choice == "6":
#         name = input("Nhập tên con vật cần xóa: ")
#         zoo.remove_animal_by_name(name)
#
#     elif choice == "7":
#         old_name = input("Nhập tên hiện tại của con vật: ")
#         new_name = input("Nhập tên mới: ")
#         zoo.rename_animal(old_name, new_name)
#
#     elif choice == "8":
#         zoo.show_by_type()
#
#     elif choice == "0":
#         print("👋 Tạm biệt!")
#         break
#
#     else:
#         print("⚠️ Lựa chọn không hợp lệ. Vui lòng chọn từ 0 đến 8.")

# Danh sach quan ly sinh vien bang linked list
# class Node:
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#         self.next = None # con tro den sinh vien tiep theo
#
# class LinkedList:
#     def __init__(self):
#         self.head = None #node dau tien ban dau rong
#
#     def add_student(self, name, student_id):
#         """Them sinh vien vao dau danh sach"""
#         new_node = Node(name, student_id)
#         new_node.next = self.head
#         self.head = new_node
#
#     def print_student(self):
#         """In danh sach sinh vien"""
#         current = self.head
#         while current:
#             print(f"ID: {current.student_id}, Name: {current.name}")
#             current = current.next
#
# students_list = LinkedList()
#
# students_list.add_student("alice","SV001")
# students_list.add_student("Bob","SV002")
# students_list.add_student("Charlie","SV003")
# students_list.add_student("Tuong", "SV004")
#
# students_list.print_student()

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None  # Chỉ có con trỏ đến nút tiếp theo
#
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None  # Node đầu tiên
#
#     def append(self, data):
#         """Thêm node mới vào cuối danh sách"""
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
#
#     def print_list(self):
#         """Duyệt danh sách và in các phần tử"""
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")
#
# # ✅ Kiểm thử Singly Linked List
# singly_list = SinglyLinkedList()
# singly_list.append(1)
# singly_list.append(3)
# singly_list.append(2)
# singly_list.print_list()

# arr = [10, 30, 20, 60, 40, 50, 5]
# print (len(arr))
# arr.append(60)
# print (arr)
# arr.insert(2,25)
# print (arr)
# arr.remove(30)
# print (arr)
# arr.pop(4)
# print (arr)
#
# for x in arr:
#     print(f"Phan tu {x}")
#
# arr.sort()
# print (arr)
# duplicate = set([x for x in arr if arr.count(x) >1])
# print (duplicate)
# arr = list(set(arr))
# print (arr)
# arr.reverse()
# print(arr)

# hash_table = {"Tuong":26, "Thanh":24}
# print (hash_table["Tuong"])
# hash_table["nhaTTuong"] = 27
# print (hash_table)
# del hash_table["Thanh"]
# print(hash_table)
# if "Thanh" in hash_table:
#     print ("Thanh co trong hash table!")
# print("Thanh khong co trong danh sach table")
#
# for key,value in hash_table.items():
#     print(f"{key} -> {value}")
# keys = hash_table.keys()
# print(keys)
# for key in hash_table.keys():
#     print (key)
#
# values = hash_table.values()
# print(values)
#
# for values in hash_table.values():
#     print(values)

# import re
# text = "Python is great. _0 @,#Python is easy to learn. Learn Python!"
#
# #Clean text
# text = text.lower() #Khong phan biet hoa hay thuong
# text =  re.sub(r"[^\w\s]",'',text) #lay tat ca ky tu dac biet va tha the bang '' trong doan text
# print(text)
#
# # tach tung tu ra
# words = text.split()
# print(words)
#
# #Dem so lan tu xuat hien trong doan text
# word_count ={}
# for word in words: #duyet tung tu trong text vua tach
#     if word in word_count: # neu da co thi tang  len 1
#         word_count[word] +=1
#     else: # chua co thi cho la 1 (lan dau xuat hien)
#         word_count[word] = 1
# print(word_count)
#
# #Sap xep theo tan suat giam dan
# #Sau khi sort bang key,value cua dict word_count vua tao, (item:item[1] vi du 'python'[0],3[1],se chon[1] la 3,
# # mac dinh la tu nho -> lon, nen phai reverse=true de lon->nho, sau khi sort xong thi co dang tuple nen phai
# # chuyen ve dang dict)
# sorted_word_count = dict(sorted(word_count.items(), key=lambda item:item[1], reverse=True))
# print(sorted_word_count)

# import re
# text = "The stars shine brightly. The stars glow. The stars illuminate the sky. Stars are everywhere. Stars never fade. Stars, stars, stars!"
#
# text = text.lower()
# text = re.sub(r'[^\w\s]','',text)
#
# words = text.split()
#
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] +=1
#     else:
#         word_count[word] = 1
#
# sorted_word_count = dict(sorted(word_count.items(),key= lambda item:item[1], reverse=True))
# print(sorted_word_count)

#Viết hàm kiểm tra xem trong một danh sách số nguyên nums có tồn tại phần tử trùng nhau hay không.

# Input: [1, 2, 3, 4]
# Output: False
#
# Input: [1, 2, 3, 1]
# Output: True

# def contains_duplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         else:
#             seen.add(num)
#     return False
#
# print(contains_duplicate([1,2,3,4]))
# print(contains_duplicate([1,2,3,1]))

#Cho một danh sách số nguyên, trong đó **mỗi phần tử xuất hiện đúng 2 lần,
# ngoại trừ **một phần tử duy nhất xuất hiện 1 lần. Tìm phần tử đó.

# Input: [2, 3, 5, 4, 5, 3, 4]
# Output: 2

# from collections import Counter
#
# def find_single_number(nums):
#     freq= Counter(nums)
#     for num,count in freq.items():
#         if count == 1:
#             return num
# print(find_single_number([2, 3, 5, 4, 5, 3, 4]))

# 🎯 Đề bài:
# Cho một chuỗi s, tìm ký tự đầu tiên không lặp lại,
# và trả về chỉ số (index) của nó. Nếu không có, trả về -1.

# Input: "leetcode"
# Output: 0  # vì 'l' chỉ xuất hiện 1 lần và đứng đầu
#
# Input: "loveleetcode"
# Output: 2  # 'v' chỉ xuất hiện 1 lần
#
# Input: "aabbcc"
# Output: -1  # Không có ký tự nào chỉ xuất hiện 1 lần

# from collections import Counter
# def find_word_only1(s):
#     count= Counter(s)
#     for i, char in enumerate(s):
#         if count[char] == 1:
#             return i
#     return -1
# print (find_word_only1("leetcode"))
# print (find_word_only1("loveleetcode"))
# print (find_word_only1("aabbcc"))

#On tap
# Đếm tần suất từ trong chuỗi
# Bài tập: Viết hàm count_characters(s) nhận vào chuỗi s,
# trả về dict chứa tần suất từng ký tự.
# Input: "hello"
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# from collections import Counter
#
# def count(s):
#     freq = dict(Counter(s))
#     return freq
# print(count("hello"))

#  2. Kiểm tra mảng có phần tử trùng không
# 🔹 Bài tập: Viết hàm has_duplicate(nums) kiểm tra xem
# trong nums có phần tử nào xuất hiện nhiều hơn 1 lần không.
# Input: [1, 2, 3, 4]   → False
# Input: [1, 2, 2, 3]   → True

# def has_duplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         else:
#             seen.add(num)
#     return False
# print(has_duplicate([1, 2, 3, 4]))
# print(has_duplicate([1, 2, 2, 3]))

#  3. Tìm phần tử xuất hiện duy nhất trong mảng
# (Mỗi phần tử khác xuất hiện đúng 2 lần)
#
# 🔹 Bài tập: Viết hàm find_unique(nums) trả về phần tử xuất hiện đúng 1 lần, còn lại xuất hiện 2 lần.

# Input: [2, 3, 5, 3, 2]
# Output: 5

# from collections import Counter
#
# def find_unique(nums):
#     freq= Counter(nums)
#     for num,count in freq.items():
#         if count == 1:
#             return num
# print(find_unique([2, 3, 5, 3, 2]))

# ✅ 4. Tìm ký tự đầu tiên không lặp lại trong chuỗi
# 🔹 Bài tập: Viết hàm first_unique_char(s) trả về chỉ số ký tự đầu tiên trong s chỉ xuất hiện 1 lần.
#
# 🧪 Ví dụ:
# Input: "leetcode"
# Output: 0
# Input: "aabb"
# Output: -1

# from collections import Counter
# def first_unique_char(s):
#     count = Counter(s)
#     for i,char in enumerate(s):
#         if count[char]==1:
#             return i
#     return -1
# print(first_unique_char("leetcode"))
# print(first_unique_char("aabb"))

#  Bài 1 – Biến thể: Đếm từ thay vì ký tự
# 🧩 Đề:
# Viết hàm count_words(s) đếm tần suất từng từ trong chuỗi (tách theo dấu cách).
#
# 🔹 Ví dụ:
#
# Input: "hello world hello"
# Output: {'hello': 2, 'world': 1}
#
# from collections import Counter
# def count_words(s):
#     words = s.split(" ")
#     word = dict(Counter(words))
#     return word
# print(count_words("hello world hello"))

# 🔄 Bài 2 – Biến thể: Kiểm tra phần tử trùng trong chuỗi từ
# 🧩 Đề:
# Viết hàm has_duplicate_words(s) kiểm tra xem chuỗi có từ nào trùng không.
# 🔹 Ví dụ:
# Input: "apple banana orange"
# Output: False
#
# Input: "apple banana apple"
# Output: True


# def has_duplicate_words(s):
#     seen = set()
#     words = s.split()
#     for word in words:
#         if word in seen:
#             return True
#         else:
#             seen.add(word)
#     return False
# print(has_duplicate_words("apple banana orange"))
# print(has_duplicate_words("apple banana apple"))


#  Bài 3 – Biến thể: Tìm số xuất hiện đúng 1 lần, còn lại xuất hiện 3 lần
# 🧩 Đề:
# Trong mảng, mỗi phần tử xuất hiện đúng 3 lần,
# trừ một phần tử xuất hiện 1 lần. Tìm phần tử đó.
#
# 🔹 Ví dụ:Input: [2, 2, 3, 2]
# Output: 3

# from collections import Counter
# def find_only(nums):
#     count = Counter(nums)
#     for num,count in count.items():
#         if count ==1:
#             return num
# print(find_only([2, 2, 3, 2]))

# 🔄 Bài 4 – Biến thể: Trả về ký tự không lặp lại đầu tiên (nếu không có, trả về ký tự đầu tiên lặp lại)
# 🧩 Đề:
# Viết hàm first_unique_or_repeat(s):
#
# Nếu có ký tự không lặp → trả về ký tự đầu tiên như cũ.
#
# Nếu tất cả đều lặp, trả về ký tự đầu tiên lặp lại.
#
# 🔹 Ví dụ:

# Input: "leetcode" → Output: 'l' (không lặp)
# Input: "aabbcc"   → Output: 'a' (tất cả lặp, trả ký tự lặp đầu tiên)

# from collections import Counter
#
# def find_first_word(s):
#     words = Counter(s)
#     for char in s:
#         if words[char] ==1:
#             return char
#     seen = set()
#     for char in s:
#         if char in seen:
#             return char
#         else:
#             seen.add(char)
# print(find_first_word("leetcode"))
# print(find_first_word("aabbcc"))


# debai
# Viết hàm is_anagram(s, t) trả về
# True nếu s và t là anagram của nhau (chứa cùng ký tự, tần suất giống nhau).

# from collections import Counter
#
# def is_anagram(s, t):
#     return Counter(s) == Counter(t)
#
# print(is_anagram("listen","silent"))
# print(is_anagram("hello", "world"))

# Viết hàm count_pairs(nums, k) trả về số cặp (i, j) sao cho nums[i] + nums[j] == k.

# from collections import Counter
#
# def count_pairs(nums, k):
#     count = Counter(nums)  # Dùng Counter để đếm số lần xuất hiện
#     pairs = 0
#
#     for num in nums:
#         if k - num in count:
#             pairs += count[k - num]
#
#     return pairs // 2  # Chia 2 để tránh đếm trùng
#
# print(count_pairs([1, 2, 3, 4], 5))  # Output: 2

# 2 pointer  mang da sap xep +  hashmap với mảng chưa sắp xếp

# class Solution:
#     def two_sum_sorted(self, numbers, target):
#         left = 0
#         right = len(numbers)-1
#
#         while left < right:
#             total = numbers[left] + numbers[right]
#
#             if total == target:
#                 return [left + 1, right + 1]
#             elif total < target:
#                 left += 1
#             else:
#                 right -=1
#
#     def two_sum_unsorted(self, numbers, target):
#         hashmap ={}
#         for i, num in enumerate(numbers):
#             x = target - num
#             if x in hashmap:
#                 return [hashmap[x] + 1, i + 1]
#             hashmap[num] = i
#
#
# Sol = Solution()
# print(Sol.two_sum_sorted([2, 7, 11, 15], 9))
# print(Sol.two_sum_unsorted([2, 7, 11, 15], 9))

# Bài 1: Two Sum Less Than K
# Cho một mảng nums và một số k, tìm tổng lớn nhất của 2 số trong nums mà nhỏ hơn k.
# Nếu không có cặp số nào thoả mãn, trả về -1.

# Input: nums = [34,23,1,24,75,33,54,8], k = 60
# Output: 58
# Giải thích: 34 + 24 = 58 là tổng lớn nhất < 60

import time
class Solution1:
    def max_total_less_than_k(self, nums, k):
        hash_map_key={}
        max_sum = -1

        for num in nums:
            for key in hash_map_key:
                total = num + key
                if total < k:
                    max_sum = max(max_sum, total)
            hash_map_key[num] = True
        return max_sum

    # sap xep xong roi 2 point
    def twopoint_solution(self, nums, k):
        nums.sort()
        left  = 0
        right = len(nums)-1
        max_ban_dau = -1
        while left < right:
            total = nums[left] + nums[right]
            if total < k:
                 max_ban_dau = max(max_ban_dau,total)
                 left += 1
            else:
                right -=1
        return max_ban_dau

import random
nums = random.sample(range(1, 100000), 10000)
k = 10000

Sol1 = Solution1()

start = time.time()
result_hashmap = Sol1.max_total_less_than_k(nums, k)
end = time.time()
print(f"HashMap result: {result_hashmap}, Time: {end - start:.5f} seconds")

start = time.time()
result_twopoint = Sol1.twopoint_solution(nums, k)
end = time.time()
print(f"Two Pointers result: {result_twopoint}, Time: {end - start:.5f} seconds")



