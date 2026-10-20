tong_phut=135
cong_suat_w=250
print(f"So gio tron ven:{tong_phut//60}")
print(f"So phut con lai:{tong_phut%60}")
su_dung_lau=tong_phut>60
print(f"Thoi gian su dung lau:{su_dung_lau}")
du_lieu_hop_le=cong_suat_w>0,tong_phut>0
#du doan bieu thuc:
#bieu thuc 1: 100+20*3=160
#bieu thuc 2: (100+20)*3=360
ket_qua_1=100+20*3
ket_qua_2=(100+20)*3
print(f"Ket qua bieu thuc 1: 100+20*3={ket_qua_1}")
print(f"ket qua bieu thuc 2: (100+20)*3={ket_qua_2}")
