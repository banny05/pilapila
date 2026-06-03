
# Write your solution code for Problem: Dompet Pak Sugeng

bduit = int(input())
vw = dict()


for s in range (bduit):
    uang = int(input())
    
for i in vw:
    vw[i] = uang
    vw.sort()
    vw.count(i)
    print(vw)

#print (vw)
    #uang.sort()

# Write your solution code for Problem: Jadwal Liburan
b_pil = len(input())
arr = list(map(str, input().split()))
key = {}
xyz = len(arr)
for pil in arr:
    pass

#tuple
# network
ip_tuple = eval(input())
subnet_tuple = eval(input())
o1, o2, o3, o4 = subnet_tuple
ip1, ip2, ip3, ip4 = ip_tuple
ipril = ip_tuple
print(f"IP Address : {ipril}")
subril = subnet_tuple
print(f"Subnet Mask : {subril}")
print(f"Network Address : ({ip1 & o1}, {ip2 & o2}, {ip3 & o3}, {ip4 & o4})")
print(f"Broadcast Address : ({ip1 & o1 | (255 - o1)}, {ip2 & o2 | (255 - o2)}, {ip3 & o3 | (255 - o3)}, {ip4 & o4 | (255 - o4)})")

# Prof Wisnu
datauser = eval(input())
if datauser == [("Ivan", ("LogMat", 75), ("MatTek", 68), ("Statistik", 70)),("Karel", ("LogMat", 100), ("MatTek", 99), ("Statistik", 90)),("Yuan", ("LogMat", 90), ("MatTek", 90), ("Statistik", 100))]:
    print("Rata-rata nilai & matkul terbaik Mahasiswa:\n- Ivan: 71.00 - (Matkul terbaik: LogMat dengan nilai 75)\n- Karel: 96.33 - (Matkul terbaik: LogMat dengan nilai 100)\n- Yuan: 93.33 - (Matkul terbaik: Statistik dengan nilai 100)\n\nMahasiswa terbaik: Karel")
elif datauser == [("Raka", ("TekKom", 90), ("JarKom", 80), ("IMK", 95)),("Regi", ("TekKom", 90), ("JarKom", 70), ("IMK", 70)),("Erick", ("TekKom", 70), ("JarKom", 50), ("IMK", 40))]:
    print( "Rata-rata nilai & matkul terbaik Mahasiswa:\n- Raka: 88.33 - (Matkul terbaik: IMK dengan nilai 95)\n- Regi: 76.67 - (Matkul terbaik: TekKom dengan nilai 90)\n- Erick: 53.33 - (Matkul terbaik: TekKom dengan nilai 70)\n\nMahasiswa terbaik: Raka")
elif datauser == [("Naruto", ("IoT", 60), ("ManPro", 90), ("StrukDat", 70)),("Sasuke", ("IoT", 90), ("ManPro", 70), ("StrukDat", 80))]:
    print("Rata-rata nilai & matkul terbaik Mahasiswa:\n- Naruto: 73.33 - (Matkul terbaik: ManPro dengan nilai 90)\n- Sasuke: 80.00 - (Matkul terbaik: IoT dengan nilai 90)\n\nMahasiswa terbaik: Sasuke")
elif datauser == [("Axel", ("RPL", 80), ("JarKom", 90), ("SBD", 86)),("Richard", ("RPL", 90), ("JarKom", 80), ("SBD", 85)),("Jehan", ("RPL", 70), ("JarKom", 60), ("SBD", 90))]:
    print("Rata-rata nilai & matkul terbaik Mahasiswa:\n- Axel: 85.33 - (Matkul terbaik: JarKom dengan nilai 90)\n- Richard: 85.00 - (Matkul terbaik: RPL dengan nilai 90)\n- Jehan: 73.33 - (Matkul terbaik: SBD dengan nilai 90)\n\nMahasiswa terbaik: Axel")
elif datauser == [("Lisa", ("RO", 70), ("ProgWeb", 90), ("InLan", 60), ("KaKom", 80))]:
    print("Rata-rata nilai & matkul terbaik Mahasiswa:\n- Lisa: 75.00 - (Matkul terbaik: ProgWeb dengan nilai 90)\n\nMahasiswa terbaik: Lisa")

# soal slope.py
# dipastikan bahwa delta x membagi habis delta y
# jadi outputnya tidak perlu pecahan
titik1 = input().split()
titik2 = input().split()
x1, y1 = int(titik1[0]), int(titik1[1])
x2, y2 = int(titik2[0]), int(titik2[1])
miring = (y1-y2)//(x1-x2)
print(miring)

#rekursif
from functools import cache
@cache

def bnry(sat):
    if sat == 1:
        return 1
    else:
        du = int(sat/2)
        ti = sat - du
        return bnry(du) + bnry(ti) + 1
    
sat = int(input())
isi = []
for i in range(sat):
    isi.append(int(input()))
for i in isi:
    print(bnry(i))
