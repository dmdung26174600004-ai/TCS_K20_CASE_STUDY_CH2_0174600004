from datetime import datetime

thoi_diem=datetime.now()
thoi_diem_text=thoi_diem.strftime("%Y-%m-%d%H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau=datetime(2026,10,14,13,15)
ket_thuc=datetime(2026,10,14,15,5)
thoi_luong=ket_thuc-bat_dau
print(thoi_luong)
print(type(thoi_luong))

#Du doan ket qua phep tru:
#(+)Ket qua thoi_luong: 1:50:00
#Su khac nhau giua datetime,srt,timedelta:
#(+)datetime: bieu dien mot moc thoi gian cu the
#(+)srt: la kieu chuoi ky tu van ban thong thuong,khong dung duoc cho cac phep tinh toan hoc ve thoi gian
#(+)timedelta: bieu dien mot khoang thoi gian hoac hieu so giua hai moc thoi gian