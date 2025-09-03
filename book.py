class Book:
    # Biến lớp dùng để đánh số thứ tự
    _count=0
    # Phương thức khởi tạo
    def __init__(self,title,author,year,available=True,id=None):
        if id is not None:
            self.id=id
        else:
            Book._count +=1
            self.id=Book._count
        self.title=title
        self.author=author
        self.year=year
        self.available=available # Mặc định là còn sách

    # Phương thức in đẹp
    def __str__(self):
        status="Còn" if self.available else "Đã mượn"
        return f"[{self.id}] {self.title} - {self.author} - {self.year} - {status}"
    
    # Phương thức chuyển thành dict
    def to_dict(self):
        return {
            "id":self.id,
            "title":self.title,
            "author":self.author,
            "year":self.year,
            "available":self.available
        }