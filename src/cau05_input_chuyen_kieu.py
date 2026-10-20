ma_may=input("Nhap ma may:")
cong_suat_w=input("Nhap cong suat:")
so_phut=input("Nhap so phut su dung:")
don_gia=input("Nhap don gia dien / KWH:")
print(f"Ma may: {ma_may}|Kieu:{type(ma_may)}")
print(f"Cong suat W: {cong_suat_w} W|Kieu:{type(cong_suat_w)}")
print(f"So phut su dung: {so_phut} phut|Kieu:{type(cong_suat_w)}")
print(f"Don gia dien / KWH: {don_gia} VND|Kieu:{type(don_gia)}")
print("---CHuyen kieu du lieu---")
cong_suat_w=float(cong_suat_w)
so_phut=int(so_phut)
don_gia=float(don_gia)
dien_nang_kwh=cong_suat_w*so_phut/60/1000
chi_phi=dien_nang_kwh*don_gia
print(f"Dien nang sau chuyen kieu: {dien_nang_kwh} KWH")
print(f"Chi phi sau chuyen kieu: {chi_phi} VND")

#Kiem thu voi bo du lieu:
#PC12
#250
#90
#3000