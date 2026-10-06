import csv

# 1. Baca data dari file CSV agar variabel 'data' terisi
data = []
with open("nilai.csv", mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris_bersih = {k.strip(): v.strip() for k, v in baris.items()}
        baris_bersih["nilai"] = int(baris_bersih["nilai"])
        data.append(baris_bersih)

# 2. Kode pengolahan data milikmu
nilai = [d["nilai"] for d in data] 
rata = sum(nilai) / len(nilai) 
print(f"Rata-rata: {rata:.1f}") 

lulus = [d["nama"] for d in data 
         if d["nilai"] >= 75] 
print("Lulus:", lulus) 

top = max(data, key=lambda d: d["nilai"]) 
print("Tertinggi:", top["nama"])