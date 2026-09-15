import math
def complex_power_complex(a, b, c, d, n):
    if a == 0 and b == 0:
        if c <= 0:
            raise ValueError("0^(c+id) əməliyyatı Re(c) <= 0 olduqda təyin olunmayıb!")
        return 0.0, 0.0
        
    p = 2.0 * n * math.pi
    
    # Faza hesabı (BASIC alqoritmi ilə)
    if a == 0:
        sgn_b = 1 if b > 0 else (-1 if b < 0 else 0)
        p += 0.5 * math.pi * sgn_b
    else:
        p += math.atan(b / a)
        if a < 0:
            if b < 0:
                p -= math.pi
            else:
                p += math.pi
                
    # Logarithm of magnitude: R = ln(|z|) = 0.5 * ln(a^2 + b^2)
    r = 0.5 * math.log(a * a + b * b)
    
    # Qüvvətüstü hesabı
    v = c * p + d * r
    w = math.exp(c * r - d * p)
    x = w * math.cos(v)
    y = w * math.sin(v)
    return x, y

# Başlanğıc verilənlər
default_a = 2.0
default_b = 1.0
default_c = 1.0
default_d = -1.0
default_n = 1
print("-" * 65)
print("  KOMPLEKS ƏDƏDİN KOMPLEKS QÜVVƏTƏ YÜKSƏLDİLMƏSİ ALQORİTMİ")
print("-" * 65)
print("Mötərizədəki qiymətləri seçmək üçün birbaşa Enter düyməsini sıxa bilərsiniz.\n")

try:
    input_a = input(f"Əsas kompleks ədədin həqiqi hissəsi a ({default_a}): ").strip()
    a = float(input_a) if input_a else default_a
    
    input_b = input(f"Əsas kompleks ədədin xəyali hissəsi b ({default_b}): ").strip()
    b = float(input_b) if input_b else default_b

    input_c = input(f"Üst kompleks ədədin həqiqi hissəsi c ({default_c}): ").strip()
    c = float(input_c) if input_c else default_c
    
    input_d = input(f"Üst kompleks ədədin xəyali hissəsi d ({default_d}): ").strip()
    d = float(input_d) if input_d else default_d

    input_n = input(f"Budaq nömrəsi N ({default_n}): ").strip()
    n = int(input_n) if input_n else default_n
except ValueError:
    print("\nXəta: İlkin verilənlər səhv daxil edilmişdir!")
    exit(1)

try:
    x_res, y_res = complex_power_complex(a, b, c, d, n)
except ValueError as e:
    print(f"\nXəta: {e}")
    exit(1)

sign_b = "-" if b < 0 else "+"
sign_d = "-" if d < 0 else "+"
sign_y = "-" if y_res < 0 else "+"
print("=" * 65)
print("  Nəticə:")
print(f"    Əsas (z)       : {a} {sign_b} {abs(b)}*i")
print(f"    Qüvvət üstü (w): {c} {sign_d} {abs(d)}*i")
print(f"    Budaq (N)      : {n}")
print(f"    (z)^w nəticəsi : {x_res:.8f} {sign_y} {abs(y_res):.8f}*i")
print("=" * 65)
