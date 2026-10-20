#ma_may=input("Nhap ma may:")
#cong_suat_w=input("Nhap cong suat W:")
#so_phut=int(input("Nhap so phut:"))
#dien_nang_kwh=cong_suat_w*so_phut/60/1000

#print(f"May: {ma_may}")
#print(f"Dien nang: {dien_nang:.3f}kWh"

#Cac loi cua tep src/cau07_chuan_doan_loi.py:
#Dong 7:
#(+)Loai loi: SyntaxError
#(+)Thong bao loi: '(' was never closed
#(+)Nguyen nhan: thieu dau ")"
#Dong 5:
#(+)loai loi: TypeError
#(+)Thong bao loi: unsupported operand type(s) for /: 'str' and 'int'
#(+)Nguyen nhan: Bien cong_suat_w nhan gia tri input() duoi dang chuoi (str) nen khong the (*) truc tiep voi so nguyen
#Dong 7:
#(+)loai loi: NameError
#(+)Thong bao loi: name 'dien_nang' is not defined. Did you mean: 'dien_nang_kwh'?
#(+)Nguyen nhan: Python khong tim thay bien 'dien_nang' , python chi tim thay bien dien_nang_kwh
#Sua:
ma_may=input("Nhap ma may:")
cong_suat_w=float(input("Nhap cong suat W:"))
so_phut=int(input("Nhap so phut:"))
dien_nang_kwh=cong_suat_w*so_phut/60/1000

print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh} kWh")

#Mo ta cac loi:
#loi 1: SyntaxError do nhap thieu '(' cuoi cau lenh print dong 7
#loi 2: TypeError do bien cong_suat_w nhan kieu (str) tu input nen khong nhan truc tiep duoc voi so
#loi 3: NameError do lenh print dung sai ten bien 'dien_nang' thay vi 'dien_nang_kwh'