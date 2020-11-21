arrBerat = []
bMin = float()
bMax = float()

def hitungMinMax(arrBerat):
    global bMin, bMax 
    bMin = min(arrBerat)
    bMax = max(arrBerat)
    print('Berat terkecil bayi : ', bMin , ' Kg')
    print('Berat terbesar bayi : ', bMax , ' Kg') 


def rerata(arrBerat):
    total = sum(arrBerat)
    rata2 = total/len(arrBerat)
    print('Rata-rata : ', round(rata2,2) , ' Kg')

print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    berat=float(input(f'Masukkan Berat Balita Ke-{i+1} : '))
    arrBerat.append(berat)

hitungMinMax(arrBerat)
rerata(arrBerat)

