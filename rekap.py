import csv

data = []
with open("nilai.csv", mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris_bersih = {k.strip(): v.strip() for k, v in baris.items()}
        baris_bersih["nilai"] = int(baris_bersih["nilai"])
        data.append(baris_bersih)

rekap = {}
for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")
for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")