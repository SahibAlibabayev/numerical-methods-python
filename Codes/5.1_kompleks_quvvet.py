import math
def complex_power_polar(x, y, w):
    if x == 0 and y == 0:
        if w <= 0:
            raise ValueError("0^w əməliyyatı w <= 0 olduqda təyin olunmayıb!")
        return 0.0, 0.0

    # Fazanın tapılması (BASIC alqoritmi ilə)
    if x == 0:
        sgn_y = 1 if y > 0 else (-1 if y < 0 else 0)
        f = 0.5 * math.pi * sgn_y
    else:
        f = math.atan(y / x)
        if x < 0:
            f += math.pi
            if y < 0:
                f -= 2 * math.pi

    # R = (x^2 + y^2)^(w/2)
    r = (x * x + y * y) ** (w / 2.0)
    a = r * math.cos(w * f)
    b = r * math.sin(w * f)
    return a, b

# Başlanğıc verilənlər
default_x = 4.0
default_y = 5.0
default_w = 3.0
print("-" * 65)
print("  KOMPLEKS ƏDƏDİN HƏQİQİ QÜVVƏTƏ YÜKSƏLDİLMƏSİ ALQORİTMİ")
print("-" * 65)
print("Mötərizədəki qiymətləri seçmək üçün birbaşa Enter düyməsini sıxa bilərsiniz.\n")

try:
    input_x = input(f"Kompleks ədədin həqiqi hissəsini daxil edin x ({default_x}): ").strip()
    x = float(input_x) if input_x else default_x
    
    input_y = input(f"Kompleks ədədin xəyali hissəsini daxil edin y ({default_y}): ").strip()
    y = float(input_y) if input_y else default_y
    
    input_w = input(f"Həqiqi qüvvət üstünü daxil edin w ({default_w}): ").strip()
    w = float(input_w) if input_w else default_w
except ValueError:
    print("\nXəta: İlkin verilənlər səhv daxil edilmişdir!")
    exit(1)

try:
    a, b = complex_power_polar(x, y, w)
except ValueError as e:
    print(f"\nXəta: {e}")
    exit(1)

sign_y = "-" if y < 0 else "+"
sign_b = "-" if b < 0 else "+"
print("=" * 65)
print("  Nəticə:")
print(f"    Daxil edilən ədəd : z = {x} {sign_y} {abs(y)}*i")
print(f"    Qüvvət üstü       : w = {w}")
print(f"    (z)^w nəticəsi    : {a:.8f} {sign_b} {abs(b):.8f}*i")
print("=" * 65)
