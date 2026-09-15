import math
def f(x):
    return x ** 3

# Başlanğıc verilənlər
default_a = 0.0
default_b = 3.0
default_n = 10
default_eps = 0.01
print("-" * 70)
print("  ORTA DÜZBUCAQLILAR ÜSULU İLƏ İNTEQRALLAMA")
print("-" * 70)
print("Qeyd: İnteqrallama aralığının sol ucu sağ ucundan kiçik olmalıdır (A < B).")
print("Başlanğıc addım sayı (N) müsbət tam ədəd, dəqiqlik isə müsbət ədəd olmalıdır.")
print("-" * 70)
print("Mötərizədəki qiymətləri seçmək üçün birbaşa Enter düyməsini sıxa bilərsiniz.\n")

try:
    input_a = input(f"Aralığın sol ucunu daxil edin A ({default_a}): ").strip()
    a = float(input_a) if input_a else default_a
    
    input_b = input(f"Aralığın sağ ucunu daxil edin B ({default_b}): ").strip()
    b = float(input_b) if input_b else default_b
    
    input_n = input(f"Başlanğıc addım sayını daxil edin N ({default_n}): ").strip()
    n = int(input_n) if input_n else default_n
    
    input_eps = input(f"Dəqiqliyi daxil edin eps ({default_eps}): ").strip()
    eps = float(input_eps) if input_eps else default_eps
except ValueError:
    print("\nXəta: İlkin verilənlər səhv daxil edilmişdir!")
    exit(1)

if eps <= 0:
    print("\nXəta: Dəqiqlik (eps) müsbət ədəd olmalıdır!")
    exit(1)

if n <= 0:
    print("\nXəta: Addım sayı (N) müsbət tam ədəd olmalıdır!")
    exit(1)

if a >= b:
    print("\nXəta: Aralığın sol ucu sağ ucundan kiçik olmalıdır (A < B)!")
    exit(1)

def integrate_midpoint(a, b, n):
    h = (b - a) / n
    s = 0.0
    for i in range(n):
        # Orta nöqtə x_i
        x_i = a + (i + 0.5) * h
        s += f(x_i)
    return s * h

# Epsilondan asılı olaraq kəsr hissədəki rəqəmlərin sayını hesablayırıq
decimals = max(8, int(-math.log10(eps)) + 2)
print("-" * 67)
print(f"{'İterasiya':^10} | {'N':^8} | {'İnteqral Qiyməti (S)':^22} | {'Xəta (P)':^18}")
print("-" * 67)

k = 1
# Birinci yaxınlaşma
s_old = integrate_midpoint(a, b, n)
print(f"{k:^10d} | {n:^8d} | {s_old:^22.{decimals}f} | {'-':^18}")

max_iter = 20
while k < max_iter:
    k += 1
    n = 2 * n  # Addım sayını 2 dəfə artırırıq
    s_new = integrate_midpoint(a, b, n)
    p = abs(s_new - s_old)
    
    print(f"{k:^10d} | {n:^8d} | {s_new:^22.{decimals}f} | {p:^18.{decimals}f}")
    
    if p < eps:
        print("=" * 67)
        print("  Nəticə:")
        print(f"    İnteqralın təqribi qiyməti : {s_new:.{decimals}f}")
        print(f"    Hesablanmış xəta           : {p:.{decimals}f}")
        print(f"    Son addım sayı (N)         : {n}")
        print("=" * 67)
        break
        
    s_old = s_new
else:
    print("-" * 67)
    print("Maksimum iterasiya sayına çatıldı, lakin təyin olunan dəqiqlik alınmadı.")
