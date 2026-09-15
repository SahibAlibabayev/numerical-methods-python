import math
def f(x):
    if x <= 0:
        raise ValueError("Loqarifmin arqumenti müsbət olmalıdır!")
    return 5 * x - 8 * math.log(x) - 8

def df(x):
    if x <= 0:
        raise ValueError("Törəmə hesablanarkən arqument müsbət olmalıdır!")
    return 5 - 8 / x

def d2f(x):
    if x <= 0:
        raise ValueError("İkinci tərtib törəmə hesablanarkən arqument müsbət olmalıdır!")
    return 8 / (x ** 2)

# Başlanğıc verilənlər
default_a = 3.4
default_b = 4.2
default_eps = 0.00001
print("-" * 75)
print("  TOXUNANLAR (NYUTON) ÜSULU")
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
    print("  toxunanlar üsulu yığıla bilməz.")
    exit(1)

# Furye şərtinə görə başlanğıc nöqtənin seçilməsi: f(x0) * f''(x0) > 0
if fa * d2f(a) > 0:
    c = a
    print(f"\nFurye şərti A nöqtəsində ödənir. Başlanğıc nöqtə c = a = {a}")
else:
    c = b
    print(f"\nFurye şərti B nöqtəsində ödənir. Başlanğıc nöqtə c = b = {b}")

# Epsilondan asılı olaraq kəsr hissədəki rəqəmlərin sayını hesablayırıq
decimals = max(8, int(-math.log10(eps)) + 2)
k = 0
max_iter = 100
print("-" * 76)
print(f"{'İterasiya':^10} | {'c_old':^12} | {'c_new (x)':^12} | {'f(x)':^15} | {'|x-c|':^15}")
print("-" * 76)

while k < max_iter:
    k += 1
    # Nyuton addımı (Toxunanlar üsulu)
    deriv = df(c)
    if deriv == 0:
        print("Törəmə sıfıra bərabər oldu! Üsul uğursuz oldu.")
        break
        
    x = c - f(c) / deriv
    diff = abs(x - c)
    fx = f(x)
    print(f"{k:^10d} | {c:^12.6f} | {x:^12.8f} | {fx:^15.{decimals}f} | {diff:^15.{decimals}f}")
    
    if diff < eps or abs(fx) < eps:
        print("=" * 76)
        print("  Nəticə:")
        print(f"    Tapılan kök     : {x:.8f}")
        print(f"    İterasiya sayı  : {k}")
        print(f"    f(kök) qiyməti  : {fx:.{decimals}f}")
        print("=" * 76)
        break
    c = x
else:
    print("Maksimum iterasiya sayına çatıldı, lakin təyin olunan dəqiqlik alınmadı.")
