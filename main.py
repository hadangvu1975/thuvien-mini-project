from book import Book
from library import Library
#import data

lib=Library()
s1=Book("Giữa hai ngọn sóng","Hà Nguyên Bảo",2025)
s2=Book("Hai ngọn hải đăng","Hà Đăng Vũ",2019)
s3=Book("Muôn kiếp nhân sinh","Nguyên Phong",2020)
s4=Book("Tình yêu muôn thuở","Nguyễn Văn Anh",1820,available=False)

lib.add_book(s1)
lib.add_book(s2)
lib.add_book(s3)
lib.add_book(s4)

# Hàm nhập số nguyên an toàn
def input_int(prompt):
    while True:
        try:
            value=int(input(prompt))
            return value
        except ValueError:
            print("! Vui lòng nhập số nguyên hợp lệ.")
while True:
    print("\n=== Quản lý thư viện ===")
    print("1. Thêm sách")
    print("2. Xem danh sách sách")
    print("3. Sửa sách")
    print("4. Xóa sách")
    print("5. Tìm sách")
    print("6. Sắp xếp sách")
    print("7. Thoát")

    choice=input("Chọn chức năng từ (1-7): ")

    if choice=="1":
        title=input("Tên sách: ")
        author=input("Tác giả: ")
        # year=int(input("Năm xuất bản: "))
        year=input_int("Năm xuất bản: ")
        lib.add_book(Book(title,author,year))
        print("Đã thêm sách.")
    elif choice=="2":
        lib.show_books()
    elif choice=="3":
        try:
            book_id=int(input("Nhập ID sách cần sửa:"))
            lib.edit_book(book_id)
        except ValueError:
            print("ID không hợp lệ.")
    elif choice=="4":
        try:
            book_id=int(input("Nhập ID cần xóa: "))
            lib.remove_book(book_id)
        except ValueError:
            print("ID không hợp lệ.")
    elif choice=="5":
        keyword=input("Nhập từ khóa tìm kiếm (tên hoặc tác giả): ")
        lib.find_books(keyword)
    elif choice=="6":
        print("Sắp xếp theo:")
        print("1. Năm xuất bản")
        print("2. Tên sách")
        print("3. Tác giả")
        opt=input("Chọn từ (1-3): ")
        if opt=="1":
            lib.sort_books("year")
        elif opt=="2":
            lib.sort_books("title")
        elif opt=="3":
            lib.sort_books("author")
        else:
            print("X Lựa chọn không hợp lệ")
    elif choice=="7":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")

