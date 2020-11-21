x= 1
y= 1
i=1
z=0
skor1=[]
skor2=[]
print('Masukan 2 nama klub yang bertanding : ')
klub1=input(']> Klub A : ')
klub2=input(']> Klub B : ')
while x >= 0 and y >= 0 :
    print('Pertandingan',i, ' : ',end='')
    x, y = [int(x) for x in input().split()]
    i += 1
    skor1.append(x)
    skor2.append(y)
skor1.pop()
skor2.pop()
for a in range (len(skor1)):
    if skor1[0+z] < skor2[0+z] : print('Hasil ',1+z,' : ',klub2)
    elif skor1[0+z] == skor2[0+z] : print('Hasil ',1+z,' :  Draw')
    elif skor1[0+z] > skor2[0+z] : print('Hasil ',1+z,' : ',klub1)
    z += 1
print('<===Pertandingan Selesai===>')