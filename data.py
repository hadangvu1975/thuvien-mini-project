import json
from book import Book

# Phương thức lưu file json
def save_to_file(filename,books):
    '''
    Lưu dữ liệu thành file json 
    '''
    data=[book.to_dict() for book in books]
    with open(filename,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)

# Phương thức đọc file json
def load_from_file(filename):
    '''
    Trả về danh sách đối tượng sách
    '''
    try:
        with open(filename,"r",encoding="utf-8") as f:
            data=json.load(f)
            return [Book(**item) for item in data]
            '''
            **item chính là cách viết ngắn gọn, 
            tự động thay thế cho việc gõ từng tham số.
            return [Book(
                id=item["id"],
                title=item["title"],  
                author=item["author"],
                year=item["year"],
                available=item["available"]
            ) for item in data]
            '''
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("File JSON lỗi định dạng, khởi tạo dữ liệu rỗng.")
        return []