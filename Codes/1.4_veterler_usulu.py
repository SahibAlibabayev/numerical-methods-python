import math
def f(x):
    if x <= 0:
        raise ValueError("Loqarifm funksiyasının arqumenti müsbət olmalıdır!")
    return 5 * x - 8 * math.log(x) - 8

def veterler_usulu(f, a, b, eps, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Funksiyanın aralığın uclarındakı qiymətlərinin işarəsi eyni ola bilməz (f(a)*f(b) < 0 olmalıdır)!")

    decimals = max(8, int(-math.log10(eps)) + 2)
    k = 0
    c_old = a
    history = []
    print("-" * 75)
    print(f"{'İterasiya':^10} | {'a':^12} | {'b':^12} | {'c':^12} | {'f(c)':^15}")
    print("-" * 75)

    while k < max_iter:
        fa = f(a)
        fb = f(b)
        c = a - (fa * (b - a)) / (fb - fa)
        k += 1
        fc = f(c)

        # Hər iterasiyanın nəticəsini qeyd edirik
        history.append((k, a, b, c, fc))
        print(f"{k:^10d} | {a:^12.6f} | {b:^12.6f} | {c:^12.8f} | {fc:^15.{decimals}f}")

        # Dəqiqlik yoxlanması, həm f(c)-nin sıfıra yaxınlığı həm də c-nin dəyişmə addımı yoxlanılır
        if abs(fc) < eps or abs(c - c_old) < eps:
            break
        c_old = c

        # İşarəni yoxlayıb aralığı daraldırıq
        if fa * fc < 0:
            b = c  # Kök [a, c] aralığındadır
        else:
            a = c  # Kök [c, b] aralığındadır
    return c, k, history

#  Başlanğıc verilənlər
default_a = 3.4
default_b = 4.2
default_eps = 0.00001
print("-" * 75)
print("  VƏTƏRLƏR (KƏSƏNLƏR) ÜSULU")
print("-" * 75)
print("Qeyd: Bu üsulun yığılması üçün Boltsano-Veyerştrass teoremi ödənməlidir,")
print("yəni seçilmiş [a, b] aralığının uclarında funksiya müxtəlif işarəli olmalıdır: f(a) * f(b) < 0.")
print("Əgər eyni işarəli aralıq daxil etsəniz, üsul yığılmaya bilər və ya kök tapılmaya bilər.")
print("Dəqiqlik (eps) müsbət ədəd olmalıdır (məsələn, 0.00001).")
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
    print("  vətərlər üsulu yığıla bilməz.")
    exit(1)

try:
    kok, iter_sayi, _ = veterler_usulu(f, a, b, eps)
    decimals_out = max(8, int(-math.log10(eps)) + 2)
    print("=" * 75)
    print(f"  Nəticə:")
    print(f"    Tapılan kök     : {kok:.8f}")
    print(f"    İterasiya sayı  : {iter_sayi}")
    print(f"    f(kök) qiyməti  : {f(kok):.{decimals_out}f}")
    print("=" * 75)

except Exception as ex:
    print(f"Xəta baş verdi: {ex}")
