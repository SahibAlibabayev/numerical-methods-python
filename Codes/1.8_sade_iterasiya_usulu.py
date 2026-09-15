import math
def f(x):
    if x <= 0:
        raise ValueError("Loqarifmin arqumenti müsbət olmalıdır!")
    return 5 * x - 8 * math.log(x) - 8

def g(x):
    return x + (1.0 / 7.0) * f(x)

# Başlanğıc verilənlər
default_a = 0.3
default_b = 0.7
default_eps = 0.00001
print("-" * 75)
print("  SADƏ İTERASİYA ÜSULU")
print("-" * 75)
print("Qeyd: Bu üsulun yığılması üçün Boltsano-Veyerştrass teoremi ödənməlidir,")
print("yəni seçilmiş [a, b] aralığının uclarında funksiya müxtəlif işarəli olmalıdır: f(a) * f(b) < 0.")
print("Əgər eyni işarəli aralıq daxil etsəniz, üsul yığılmaya bilər və ya kök tapılmaya bilər.")
print(f"Dəqiqlik (eps) müsbət ədəd olmalıdır (məsələn, {default_eps:.5f}).")
print("-" * 75)
print("Mötərizədəki qiymətləri seçmək üçün birbaşa Enter düyməsini sıxa bilərsiniz.\n")

try:
    input_a = input(f"Aralığın sol ucunu daxil edin A ({default_a}): ").strip()
    a = float(input_a) if input_a else default_a
    
    input_b = input(f"Aralığın sağ ucunu daxil edin B ({default_b}): ").strip()
    b = float(input_b) if input_b else default_b
    
    input_eps = input(f"Dəqiqliyi daxil edin eps ({default_eps:.5f}): ").strip()
    eps = float(input_eps) if input_eps else default_eps
except ValueError:
    print("\nXəta: İlkin verilənlər səhv daxil edilmişdir!")
    exit(1)

# Giriş verilənlərinin yoxlanması
if eps <= 0:
    print("\nXəta: Dəqiqlik (eps) müsbət ədəd olmalıdır!")
    exit(1)

if a >= b:
    print("\nXəta: Aralığın sol ucu sağ ucundan kiçik olmalıdır (A < B)!")
    exit(1)

try:
    fa = f(a)
    fb = f(b)
except ValueError as e:
    print(f"\nXəta: Funksiya hesablanarkən xəta baş verdi: {e}")
    exit(1)

if fa * fb >= 0:
    print("\nXəbərdarlıq / Problem (Sıra yığılmaya bilər):")
    print(f"  f(a) = {fa:.6f} və f(b) = {fb:.6f} eyni işarəlidir və ya sıfıra bərabərdir (f(a)*f(b) >= 0).")
    print("  Koşi teoremindən çıxan nəticə ödənilmir. Bu aralıqda kökün varlığına zəmanət verilmir,")
    print("  sadə iterasiya üsulu yığıla bilməz.")
    exit(1)

# Epsilondan asılı olaraq kəsr hissədəki rəqəmlərin sayını hesablayırıq
decimals = max(8, int(-math.log10(eps)) + 2)
x = b  # Orijinal BASIC koddakı kimi başlanğıc yaxınlaşma B seçilir
k = 0
max_iter = 100
print("-" * 76)
print(f"{'İterasiya':^10} | {'x_old':^12} | {'x_new (y)':^12} | {'f(y)':^15} | {'Nisbi Fərq':^15}")
print("-" * 76)

while k < max_iter:
    y = g(x)
    k += 1
    
    # Nisbi fərq (BASIC sətir 90-dakı ABS((Y-X)/X) kriteriyası)
    if x == 0:
        rel_diff = abs(y - x)
    else:
        rel_diff = abs((y - x) / x)
        
    fy = f(y)
    print(f"{k:^10d} | {x:^12.6f} | {y:^12.8f} | {fy:^15.{decimals}f} | {rel_diff:^15.{decimals}f}")
    
    if rel_diff < eps:
        print("=" * 76)
        print("  Nəticə:")
        print(f"    Tapılan kök     : {y:.8f}")
        print(f"    İterasiya sayı  : {k}")
        print(f"    f(kök) qiyməti  : {fy:.{decimals}f}")
        print("=" * 76)
        break
    x = y
else:
    print("Maksimum iterasiya sayına çatıldı, lakin təyin olunan dəqiqlik alınmadı.")
