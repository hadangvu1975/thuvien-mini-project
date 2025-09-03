from book import Book
import datetime
import os
from data import save_to_file,load_from_file

# === 1. Viết hàm ghi log chung ===
def ghi_log(action,book):
    '''
    Ghi log vào file library.log
    action: Hành động (Thêm, Sửa, Xóa)
    book: đối tượng sách (có id, title)
    '''
    # Lấy thời gian hiện tại để biết log này xảy ra lúc nào
    thoi_gian=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Tạo chuỗi log gồm thời gian + hành động + thông tin sách
    log_text=f"[{thoi_gian}] {action} - ID:{book.id}, Title:{book.title}\n"
    # Mở file ở chế độ append để không ghi đè dữ liệu cũ
    with open("library.log","a",encoding="utf-8") as f:
        f.write(log_text)

class Library:
    # Danh sách sách trong thư viện
    def __init__(self,filename="books.json"):
        base_dir=os.path.dirname(__file__)
        self.filename=os.path.join(base_dir,filename)
        self.books=load_from_file(self.filename) or []

    def save(self):
        save_to_file(self.filename,self.books)

    # Phương thức thêm sách
    def add_book(self,book):
        '''
        Thêm sách vào thư viện và ghi log 
        '''
        # Thêm sách vào danh sách sách
        self.books.append(book)
        self.save()
        print(f"Đã thêm sách: {book.title}")

        # Sau khi thêm, ta ghi log để lưu vết
        ghi_log("Thêm sách",book)

    # Phương thức in danh sách sách
    def show_books(self):
        if not self.books:
            print("Thư viện trống.")
        else:
            print("=== Danh sách sách ===")
            for b in self.books:
                print(b)

    # Phương thức tìm sách theo tên
    def find_by_title(self,title):
        '''
        Nhận vào tên sách, Trả về danh sách đối tượng sách
        '''
        results=[]
        for book in self.books:
            if title.lower() in book.title.lower():
                results.append(book)
        return results
    
    # Phương thức sửa sách
    def edit_book(self,book_id):
        '''
        Nhận vào book_id, sửa các thông tin nhập mới
        '''
        for book in self.books:
            if book.id==book_id:
                print("Nhập thông tin mới (để trống nếu không thay đổi): ")
                new_title=input("Tên mới: ") or book.title
                new_author=input("Tác giả mới: ") or book.author
                try:
                    new_year=int(input("Năm mới: ") or book.year)
                except ValueError:
                    new_year=book.year
                book.title=new_title
                book.author=new_author
                book.year=new_year
                print("Đã cập nhật sách.")
                # Sau khi sửa, ghi log để lưu vết
                ghi_log("Sửa sách",book)
                return
        print("Không tìm thấy sách.")
    # Phương thức xóa sách   
    def remove_book(self,book_id):
        '''
        Nhận vào id, xóa sách có id trùng với id_book
        '''
        
        for book in self.books:
            if book.id==book_id:
                xac_nhan=input(f"Bạn chắc xóa sách: {book.title}? (y/n) ").strip().lower()
                if xac_nhan=="y":
                    self.books.remove(book)
                    print("Đã xóa sách: {book.title}")
                    # Sau khi xóa, ta ghi log để lưu vết
                    ghi_log("Xóa sách",book)
                    return True
                else:
                    print("Hủy thao tác xóa.")
        print("Không tìm thấy sách để xóa.")
        return False
    
    # Phương thức sắp xếp sách
    def sort_books(self,by="year"):
        if by=="year":
            sorted_books=sorted(self.books,key=lambda b:b.year)
        elif by=="title":
            sorted_books=sorted(self.books,key=lambda b:b.title.lower())
        elif by=="author":
            sorted_books=sorted(self.books,key=lambda b:b.author.lower())
        else:
            print("X Tiêu chí sắp xếp không hợp lệ.")
            return
        print(f"Danh sách sách sắp xếp theo {by}:")
        for book in sorted_books:
            print(book)

    # Phương thức tìm kiếm sách
    def find_books(self,keyword):
        keyword=keyword.lower()
        found=[book for book in self.books
               if keyword in book.title.lower() or 
               keyword in book.author.lower()]
        if not found:
            print("X Không tìm thấy sách.")
        else:
            print("Kết quả tìm kiếm:")
            for book in found:
                print(book)

        
