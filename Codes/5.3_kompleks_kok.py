import math
def complex_roots(r, u, n):
    if n <= 0:
        raise ValueError("Kökün dərəcəsi n müsbət tam ədəd olmalıdır!")
    if r == 0 and u == 0:
        return [(0.0, 0.0, 0.0)] * n

    m = 1.0 / n
    s = (r * r + u * u) ** (m / 2.0)  # s = |z|^(1/n)
    
    if r == 0:
        sgn_u = 1 if u > 0 else (-1 if u < 0 else 0)
        t = sgn_u * math.pi / 2.0
    elif r > 0:
        t = math.atan(u / r)
    else:
        t = math.pi + math.atan(u / r)
        if u < 0:
            t -= 2.0 * math.pi
            
    t_start = t * m
    c_step = 2.0 * math.pi * m
    roots = []
    t_current = t_start
    for i in range(n):
        real_part = s * math.cos(t_current)
        imag_part = s * math.sin(t_current)
        roots.append((real_part, imag_part, t_current))
        t_current += c_step   
    return roots

# Başlanğıc verilənlər
default_r = -7.0
default_u = 5.0
default_n = 8
print("-" * 65)
print("  KOMPLEKS ƏDƏDDƏN KÖK ALINMASI ALQORİTMİ")
print("-" * 65)
print("Mötərizədəki qiymətləri seçmək üçün birbaşa Enter düyməsini sıxa bilərsiniz.\n")

try:
    input_r = input(f"Kompleks ədədin həqiqi hissəsi r ({default_r}): ").strip()
    r = float(input_r) if input_r else default_r
    
    input_u = input(f"Kompleks ədədin xəyali hissəsi u ({default_u}): ").strip()
    u = float(input_u) if input_u else default_u

    input_n = input(f"Kökün dərəcəsi n ({default_n}): ").strip()
    n = int(input_n) if input_n else default_n
except ValueError:
    print("\nXəta: İlkin verilənlər səhv daxil edilmişdir!")
    exit(1)

try:
    roots = complex_roots(r, u, n)
except ValueError as e:
    print(f"\nXəta: {e}")
    exit(1)

sign_u = "-" if u < 0 else "+"
print("-" * 60)
print(f"{'İndeks (k)':^10} | {'Faza (rad)':^14} | {'Kök (z_k)':^30}")
print("-" * 60)

for k, (real, imag, phase) in enumerate(roots):
    sign_i = "-" if imag < 0 else "+"
    val_str = f"{real:.6f} {sign_i} {abs(imag):.6f}*i"
    print(f"{k:^10d} | {phase:^14.6f} | {val_str:^30}")

print("=" * 60)
print("  Nəticə:")
print(f"    Daxil edilən ədəd : z = {r} {sign_u} {abs(u)}*i")
print(f"    Kökün dərəcəsi    : n = {n}")
print(f"    Tapılan köklər    : {n} ədəd kompleks kök hesabla mışdır")
print("=" * 60)
