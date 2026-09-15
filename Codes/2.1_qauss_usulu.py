import numpy as np

# Başlanğıc verilənlər
default_N = 3
default_A = [
    [-2.0, 3.0, 4.0],
    [1.0, 5.0, 7.0],
    [4.0, 2.0, 1.0]
]
default_b = [21.0, -3.0, -5.0]
print("-" * 75)
print("  XƏTTİ CƏBRİ TƏNLİKLƏR SİSTEMİNİN QAUSS ÜSULU İLƏ HƏLLİ")
print("-" * 75)
print("Qeyd: Düzünə gedişdə əsas elementin seçilməsi (pivoting) istifadə olunur.")
print("Mötərizədəki qiymətləri seçmək üçün birbaşa Enter düyməsini sıxa bilərsiniz.\n")

try:
    input_n = input(f"Tənliklərin sayını daxil edin N ({default_N}): ").strip()
    n = int(input_n) if input_n else default_N
except ValueError:
    print("\nXəta: Zəhmət olmasa tam ədəd daxil edin!")
    exit(1)

if n <= 0:
    print("\nXəta: Tənliklərin sayı müsbət tam ədəd olmalıdır!")
    exit(1)
if n == default_N:
    A = [row[:] for row in default_A]
    b = list(default_b)
else:
    print(f"\n{n}x{n} ölçülü matrisi və sərbəst hədləri daxil edin:")
    A = []
    b = []
    for i in range(n):
        row_str = input(f"  {i+1}-ci tənliyin əmsallarını boşluqla daxil edin ({n} ədəd): ").strip()
        row = [float(x) for x in row_str.split()]
        if len(row) != n:
            print(f"Xəta: Düz {n} ədəd əmsal daxil edilməlidir!")
            exit(1)
        A.append(row)
        b_val = float(input(f"  {i+1}-ci tənliyin sərbəst həddi b({i+1}): ").strip())
        b.append(b_val)

print("\nSistem tənlikləri:")
for i in range(n):
    eq_parts = []
    for j in range(n):
        sign = "+" if A[i][j] >= 0 and j > 0 else ""
        eq_parts.append(f"{sign}{A[i][j]:.2f}*x{j+1}")
    print(f"  {' '.join(eq_parts)} = {b[i]:.2f}")
print("-" * 75)

# Genişləndirilmiş matris [A|b] yaradılır
aug = np.zeros((n, n + 1), dtype=float)
for i in range(n):
    for j in range(n):
        aug[i, j] = A[i][j]
    aug[i, n] = b[i]

# 1. DÜZÜNƏ GEDİŞ
for u in range(n):
    # Əsas elementin (pivot) seçilməsi
    max_row = u
    for k in range(u + 1, n):
        if abs(aug[k, u]) > abs(aug[max_row, u]):
            max_row = k

    # Əgər cari sutunda maksimum element sıfırdırsa, sistem uyuşan deyil və ya sonsuz həlli var
    if abs(aug[max_row, u]) < 1e-12:
        print("\nXəta: Sistem uyuşan deyil və ya yeganə həllə malik deyil (det(A) = 0)!")
        exit(1)

    # Sətirlərin yerinin dəyişdirilməsi
    if max_row != u:
        aug[[u, max_row]] = aug[[max_row, u]]

    # Pivot sətrinin normallaşdırılması (diqonal elementi 1 etmək)
    pivot = aug[u, u]
    aug[u, u:] /= pivot

    # Aşağıdakı sətirlərdən çıxma (sıfırlama)
    for i in range(u + 1, n):
        factor = aug[i, u]
        aug[i, u:] -= factor * aug[u, u:]

# 2. TƏRSİNƏ GEDİŞ 
x = np.zeros(n, dtype=float)
for i in range(n - 1, -1, -1):
    x[i] = aug[i, n]
    for j in range(i + 1, n):
        x[i] -= aug[i, j] * x[j]

print("=" * 75)
print("  Nəticə (Sistemin həlli):")
for i in range(n):
    print(f"    X({i+1}) = {x[i]:.8f}")
print("=" * 75)
