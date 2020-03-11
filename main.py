print('Bảng xếp hạng SEA Games\n''1 huy chương vàng = 3 điểm\n''1 huy chương bạc  = 2 điểm\n''1 huy chương đồng = 1 điểm\n')

print('Brunei')
bru_gold = int(input('Vui lòng nhập số lượng huy chương vàng: '))
bru_silver = int(input('Vui lòng nhập số lượng huy chương bạc: '))
bru_bronze = int(input('Vui lòng nhập số lượng huy chương đồng: '))

print('Cambodia')
cam_gold = int(input('Vui lòng nhập số lượng huy chương vàng: '))
cam_silver = int(input('Vui lòng nhập số lượng huy chương bạc: '))
cam_bronze = int(input('Vui lòng nhập số lượng huy chương đồng: '))

print('Indonesia')
ina_gold = int(input('Vui lòng nhập số lượng huy chương vàng: '))
ina_silver = int(input('Vui lòng nhập số lượng huy chương bạc: '))
ina_bronze = int(input('Vui lòng nhập số lượng huy chương đồng: '))

print('Laos')
lao_gold = int(input('Vui lòng nhập số lượng huy chương vàng: '))
lao_silver = int(input('Vui lòng nhập số lượng huy chương bạc: '))
lao_bronze = int(input('Vui lòng nhập số lượng huy chương đồng: '))

print('Malaysia')
mas_gold = int(input('Vui lòng nhập số lượng huy chương vàng: '))
mas_silver = int(input('Vui lòng nhập số lượng huy chương bạc: '))
mas_bronze = int(input('Vui lòng nhập số lượng huy chương đồng: '))

print('Myanmar')
mya_gold = int(input('Vui lòng nhập số lượng huy chương vàng: '))
mya_silver = int(input('Vui lòng nhập số lượng huy chương bạc: '))
mya_bronze = int(input('Vui lòng nhập số lượng huy chương đồng: '))

print('Philippines')
phi_gold = int(input('Vui lòng nhập số lượng huy chương vàng: '))
phi_silver = int(input('Vui lòng nhập số lượng huy chương bạc: '))
phi_bronze = int(input('Vui lòng nhập số lượng huy chương đồng: '))

print('Singapore')
sin_gold = int(input('Vui lòng nhập số lượng huy chương vàng: '))
sin_silver = int(input('Vui lòng nhập số lượng huy chương bạc: '))
sin_bronze = int(input('Vui lòng nhập số lượng huy chương đồng: '))

print('Thailand')
tha_gold = int(input('Vui lòng nhập số lượng huy chương vàng: '))
tha_silver = int(input('Vui lòng nhập số lượng huy chương bạc: '))
tha_bronze = int(input('Vui lòng nhập số lượng huy chương đồng: '))

print('Timor')
tls_gold = int(input('Vui lòng nhập số lượng huy chương vàng: '))
tls_silver = int(input('Vui lòng nhập số lượng huy chương bạc: '))
tls_bronze = int(input('Vui lòng nhập số lượng huy chương đồng: '))

print('Việt Nam')
vie_gold = int(input('Vui lòng nhập số lượng huy chương vàng: '))
vie_silver = int(input('Vui lòng nhập số lượng huy chương bạc: '))
vie_bronze = int(input('Vui lòng nhập số lượng huy chương đồng: '))

#Kết quả
bru = bru_gold*3 + bru_silver*2 + bru_bronze
cam = cam_gold*3 + cam_silver*2 + cam_bronze
ina = ina_gold*3 + ina_silver*2 + ina_bronze
lao = lao_gold*3 + lao_silver*2 + lao_bronze
mas = mas_gold*3 + mas_silver*2 + mas_bronze
mya = mya_gold*3 + mya_silver*2 + mya_bronze
phi = phi_gold*3 + phi_silver*2 + phi_bronze
sin = sin_gold*3 + sin_silver*2 + sin_bronze
tha = tha_gold*3 + tha_silver*2 + tha_bronze
tls = tls_gold*3 + tls_silver*2 + tls_bronze
vie = vie_gold*3 + vie_silver*2 + vie_bronze

#Bảng hiển thị
print('-------------------------------------')
print('Quốc gia      Vàng   Bạc   Đồng   Tổng điểm')
print('Brunei',' '*7,bru_gold,' '*4,bru_silver,' '*3,bru_bronze,' '*4,bru,'\n')
print('Cambodia',' '*5,cam_gold,' '*4,cam_silver,' '*3,cam_bronze,' '*4,cam,'\n')
print('Indonesia',' '*4,ina_gold,' '*4,ina_silver,' '*3,ina_bronze,' '*4,ina,'\n')
print('Laos',' '*9,lao_gold,' '*4,lao_silver,' '*3,lao_bronze,' '*4,lao,'\n')
print('Malaysia',' '*5,mas_gold,' '*4,mas_silver,' '*3,mas_bronze,' '*4,mas,'\n')
print('Myanmar',' '*6,mya_gold,' '*4,mya_silver,' '*3,mya_bronze,' '*4,mya,'\n')
print('Phillippines  ',phi_gold,' '*4,phi_silver,' '*3,phi_bronze,' '*4,phi,'\n')
print('Singapore',' '*4,sin_gold,' '*4,sin_silver,' '*3,sin_bronze,' '*4,sin,'\n')
print('Thailand',' '*5,tha_gold,' '*4,tha_silver,' '*3,tha_bronze,' '*4,tha,'\n')
print('Timor',' '*8,tls_gold,' '*4,tls_silver,' '*3,tls_bronze,' '*4,tls,'\n')
print('Vietnam',' '*6,vie_gold,' '*4,vie_silver,' '*3,vie_bronze,' '*4,vie,'\n')