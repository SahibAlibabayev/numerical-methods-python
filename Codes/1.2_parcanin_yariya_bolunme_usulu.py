import math
def f(x):
    if x <= 0:
        raise ValueError("Loqarifmin arqumenti müsbət olmalıdır!")
    return 5 * x - 8 * math.log(x) - 8

# Başlanğıc verilənlər
default_a = 3.4
default_b = 4.2
default_eps = 0.00001

print("-" * 70)
print("  PARÇANIN ARDICIL YARIYA BÖLÜNMƏSİ ÜSULU (BISECTION METHOD)")
print("-" * 70)
print("Qeyd: Bu üsulun yığılması üçün Boltsano-Veyerştrass teoremi ödənməlidir,")
print("yəni seçilmiş [a, b] aralığının uclarında funksiya müxtəlif işarəli olmalıdır: f(a) * f(b) < 0.")
print("Əgər eyni işarəli aralıq daxil etsəniz, üsul yığılmaya bilər və ya kök tapılmaya bilər.")
print(f"Dəqiqlik (eps) müsbət ədəd olmalıdır (məsələn, {default_eps:.5f}).")
print("-" * 70)
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
    print("  bərabər bölünmə üsulu yığıla bilməz.")
    exit(1)

# Epsilondan asılı olaraq kəsr hissədəki rəqəmlərin sayını hesablayırıq
decimals = max(8, int(-math.log10(eps)) + 2)
k = 0
print("\n" + "-" * 91)
print(f"{'İterasiya':^10} | {'a':^12} | {'b':^12} | {'c':^12} | {'f(c)':^15} | {'|b-a|':^15}")
print("-" * 91)

while True:
    c = (a + b) / 2.0
    k += 1
    val_f = f(c)
    interval_len = abs(b - a)
    
    print(f"{k:^10d} | {a:^12.6f} | {b:^12.6f} | {c:^12.8f} | {val_f:^15.{decimals}f} | {interval_len:^15.{decimals}f}")
    # Kəsilmə şərti
    if abs(val_f) < eps:
        print("=" * 91)
        print("  Nəticə:")
        print(f"    Tapılan kök     : {c:.8f}")
        print(f"    İterasiya sayı  : {k}")
        print(f"    f(kök) qiyməti  : {val_f:.{decimals}f}")
        print("=" * 91)
        break
        
    # İşarə yoxlanışı və aralığın daraldılması
    if f(a) * val_f < 0:
        b = c
    elif f(a) * val_f > 0:
        a = c
    else:
        print("=" * 91)
        print("  Nəticə:")
        print(f"    Tapılan kök     : {c:.8f}")
        print(f"    İterasiya sayı  : {k}")
        print(f"    f(kök) qiyməti  : {val_f:.{decimals}f}")
        print("=" * 91)
        break
