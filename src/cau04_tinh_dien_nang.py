cong_suat_w=250
so_phut=90
don_gia_kwh=3000
dien_nang_kwh=cong_suat_w*so_phut/60/1000
chi_phi=dien_nang_kwh*don_gia_kwh
print(f"Dien nang tieu thu: {dien_nang_kwh} kwh|Kieu giu lieu:{type(dien_nang_kwh)}")
print(f"Chi phi dien: {chi_phi}VND|Kieu du lieu:{type(chi_phi)}")
#du doan ket qua
#Dien nang tieu thu: 0.375 kwh
#Chi phi dien: 1125 VND
print("---------------------------------------------------------------------------")
so_phut=60
dien_nang_kwh=cong_suat_w*so_phut/60/1000
chi_phi=dien_nang_kwh*don_gia_kwh
print(f"Dien nang tieu thu moi: {dien_nang_kwh} kwh")
print(f"Chi phi moi:{chi_phi} VND")

#So sanh so_phut khi thay bang 60: dien nang tieu thu va chi phi dien o 60 phut nho hon khi o 90 phut