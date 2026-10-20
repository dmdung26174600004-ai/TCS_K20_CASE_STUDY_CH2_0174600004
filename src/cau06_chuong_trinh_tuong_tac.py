ma_phien=input("Nhap ma phien:")
ma_may=input("Nhap ma may:")
cong_suat_w=float(input("Nhap cong suat:"))
so_phut=float(input("Nhap so phut su dung:"))
don_gia=float(input("Nhap don gia:"))
dien_nang_kwh=cong_suat_w * so_phut/60/1000
chi_phi=dien_nang_kwh*don_gia
print("-"*50)
print(f"Ma phien: {ma_phien}")
print(f"Ma may: {ma_may}")
print(f"Dien nang su dung: {dien_nang_kwh} KWH")
print(f"Chi phi: {chi_phi} VND")

#Kiem thu vs bo du lieu:
#LAB026
#PC12
#250
#90
#3000
