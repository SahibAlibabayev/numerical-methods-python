import math

# Kitabın 2.7 nümunəsindəki 3x3 matris və b vektoru
default_A = [
    [10.0, 3.0, -1.0],
    [2.0, -11.0, 2.0],
    [3.0, 2.0, 12.0]]
default_b = [25.0, -21.0, 60.0]
default_eps = 0.00001
print("-" * 75)
print("  XƏTTİ CƏBRİ TƏNLİKLƏR SİSTEMİNİN ZEYDEL (GAUSS-SEIDEL) ÜSULU İLƏ HƏLLİ")
print("-" * 75)
print("Qeyd: Yığılmanın təmin olunması üçün matris diaqonal üstünlüyünə malik olmalıdır.")
print(f"Dəqiqlik (eps) müsbət ədəd olmalıdır (məsələn, {default_eps:.5f}).")
print("-" * 75)
print("Mötərizədəki qiymətləri seçmək üçün birbaşa Enter düyməsini sıxa bilərsiniz.\n")

try:
    input_eps = input(f"Dəqiqliyi daxil edin eps ({default_eps:.5f}): ").strip()
    eps = float(input_eps) if input_eps else default_eps
except ValueError:
    print("\nXəta: İlkin verilənlər səhv daxil edilmişdir!")
    exit(1)

if eps <= 0:
    print("\nXəta: Dəqiqlik (eps) müsbət ədəd olmalıdır!")
    exit(1)
A = default_A
b = default_b
n = len(b)

# Diaqonal üstünlüyünün yoxlanılması
diagonally_dominant = True
for i in range(n):
    row_sum = sum(abs(A[i][j]) for j in range(n) if j != i)
    if abs(A[i][i]) <= row_sum:
        diagonally_dominant = False

if not diagonally_dominant:
    print("\nXəbərdarlıq: Matris ciddi diaqonal üstünlüyünə malik deyil, alqoritm yığılmaya bilər!")
decimals = max(6, int(-math.log10(eps)) + 1)
x = [0.0] * n  # İlkin yaxınlaşma: x = (0, 0, 0)
max_iter = 50
print("-" * 75)
print(f"{'İterasiya':^10} | {'X0':^14} | {'X1':^14} | {'X2':^14} | {'Maks. Fərq (H)':^16}")
print("-" * 75)

for k in range(1, max_iter + 1):
    h = 0.0
    x_old = list(x)
    
    for i in range(n):
        s = sum(A[i][j] * x[j] for j in range(n) if j != i)
        y = (b[i] - s) / A[i][i]
        
        # Nisbi fərq
        if y != 0:
            diff = abs((y - x_old[i]) / y)
        else:
            diff = abs(y - x_old[i])
            
        if diff > h:
            h = diff
            
        # Gauss-Seidel-də yeni tapılmış dəyər dərhal massivdə yenilənir
        x[i] = y
        
    print(f"{k:^10d} | {x[0]:^14.6f} | {x[1]:^14.6f} | {x[2]:^14.6f} | {h:^16.{decimals}f}")
    
    if h < eps:
        print("=" * 75)
        print("  Nəticə:")
        for i in range(n):
            print(f"    X({i}) = {x[i]:.6f}")
        print(f"    İterasiya sayı = {k}")
        print("=" * 75)
        break
else:
    print("-" * 75)
    print("Maksimum iterasiya sayında yığılma baş vermədi.")
