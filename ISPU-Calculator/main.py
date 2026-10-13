parameter = ["PM2.5", "PM10", "SO2", "CO", "NO2", "O3"]
konsentrasi = [90, 210, 180, 38, 260, 310]

batas = [
    [15.5, 55.4, 150.4, 250.4],
    [50, 150, 350, 420],
    [52, 180, 400, 800],
    [4000, 8000, 15000, 30000],
    [80, 200, 1130, 2260],
    [120, 235, 400, 800]
]

ispu = []

for i in range(len(parameter)):
    x = konsentrasi[i]

    if x <= batas[i][0]:
        nilai = x / batas[i][0] * 50
    elif x <= batas[i][1]:
        nilai = 50 + (x - batas[i][0]) / (batas[i][1] - batas[i][0]) * 50
    elif x <= batas[i][2]:
        nilai = 100 + (x - batas[i][1]) / (batas[i][2] - batas[i][1]) * 99
    elif x <= batas[i][3]:
        nilai = 199 + (x - batas[i][2]) / (batas[i][3] - batas[i][2]) * 100
    else:
        nilai = 500

    ispu.append(nilai)

maks = ispu[0]
minim = ispu[0]
index_maks = 0
index_min = 0

for i in range(len(ispu)):
    if ispu[i] > maks:
        maks = ispu[i]
        index_maks = i

    if ispu[i] < minim:
        minim = ispu[i]
        index_min = i

if maks <= 50:
    kualitas = "Baik"
elif maks <= 100:
    kualitas = "Sedang"
elif maks <= 199:
    kualitas = "Tidak Sehat"
elif maks <= 299:
    kualitas = "Sangat Tidak Sehat"
else:
    kualitas = "Berbahaya"

for i in range(len(parameter)):
    print(parameter[i], "=", round(ispu[i], 2))

print("ISPU Tertinggi =", round(maks, 2))
print("Kualitas Udara =", kualitas)
print("Pencemar Terbesar =", parameter[index_maks])
print("Pencemar Terkecil =", parameter[index_min])