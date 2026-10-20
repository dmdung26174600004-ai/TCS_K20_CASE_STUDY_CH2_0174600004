from datetime import datetime

loai_thiet_bi=input("Nhap loai thiet bi:")
ma_phien=input("Nhap ma phien:")
ma_may=input("Nhap ma may:")
cong_suat_w=float(input("Nhap cong suat (W):"))
so_phut=int(input("Nhap so phut (phut):"))
don_gia=float(input("Nhap don gia (VND/kWh):"))
dien_nang_kwh=cong_suat_w*so_phut/60/1000
chi_phi=dien_nang_kwh*don_gia
tren_60_phut=so_phut>60
ghi_nhan_luc=datetime.now().strftime("%Y-%m-%d%H%S")
print("="*40)
print("--- PHIEU GHI NHAN SU DUNG THIET BI ---")
print("="*40)
print(f"Ten thiet bi: {loai_thiet_bi}")
print(f"Ma phien: {ma_phien}")
print(f"May: {ma_may}")
print(f"Cong suat: {cong_suat_w} W")
print(f"Thoi luong su dung: {so_phut} phut")
print(f"Dien nang: {dien_nang_kwh} kWh")
print(f"Chi phi: {chi_phi} VND")
print(f"Tren 60 phut: {tren_60_phut}")
print(f"Ghi nhan luc: {ghi_nhan_luc}")
print("="*40)

#Kiem thu bang bo du lieu thu nhat:May tinh,LAB026,PC12,250,90,3000
#Kiem thu bang bo du lieu thu hai:May tinh,LAB025,PC01,220,50,2500