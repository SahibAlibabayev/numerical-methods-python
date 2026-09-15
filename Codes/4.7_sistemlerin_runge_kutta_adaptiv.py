import math

# Sistem tənlikləri: y1' = y2, y2' = -y1
def f1(x, y1, y2):
    return y2

def f2(x, y1, y2):
    return -y1

def rk4_step(x, y1, y2, h):
    # k1 əmsalları
    k1_1 = f1(x, y1, y2)
    k1_2 = f2(x, y1, y2)
    
    # k2 əmsalları
    k2_1 = f1(x + h / 2.0, y1 + (h * k1_1) / 2.0, y2 + (h * k1_2) / 2.0)
    k2_2 = f2(x + h / 2.0, y1 + (h * k1_1) / 2.0, y2 + (h * k1_2) / 2.0)
    
    # k3 əmsalları
    k3_1 = f1(x + h / 2.0, y1 + (h * k2_1) / 2.0, y2 + (h * k2_2) / 2.0)
    k3_2 = f2(x + h / 2.0, y1 + (h * k2_1) / 2.0, y2 + (h * k2_2) / 2.0)
    
    # k4 əmsalları
    k4_1 = f1(x + h, y1 + h * k3_1, y2 + h * k3_2)
    k4_2 = f2(x + h, y1 + h * k3_1, y2 + h * k3_2)
    
    # Yeni qiymətlər
    y1_new = y1 + (h / 6.0) * (k1_1 + 2.0 * k2_1 + 2.0 * k3_1 + k4_1)
    y2_new = y2 + (h / 6.0) * (k1_2 + 2.0 * k2_2 + 2.0 * k3_2 + k4_2)
    return y1_new, y2_new

def get_magnitude(val):
    if val == 0:
        return -999
    return math.floor(math.log10(abs(val))) + 1

# Başlanğıc verilənlər (Kitab nümunəsindəki kimi X4 = 1.0)
default_x0 = 0.0
default_x4 = 1.0
default_y1 = 1.0
default_y2 = 0.0
default_eps1 = 0.001
default_eps2 = -3

print("-" * 75)
print("  ADT SİSTEMİNİN ADTİMİ AVTOMATİK SEÇMƏKLƏ RUNQE-KUTTA HƏLLİ")
print("-" * 75)
print("Qeyd: Adaptiv addımlı 4-cü tərtib Runqe-Kutta üsulu istifadə edilir.")
print("İnteqrallama aralığının sol ucu sağ ucundan kiçik olmalıdır (x0 < x4).")
print("-" * 75)
print("Mötərizədəki qiymətləri seçmək üçün birbaşa Enter düyməsini sıxa bilərsiniz.\n")

try:
    input_x0 = input(f"Başlanğıc nöqtəni daxil edin x0 ({default_x0}): ").strip()
    x0 = float(input_x0) if input_x0 else default_x0
    
    input_y1 = input(f"y1 üçün başlanğıc qiyməti daxil edin y1(0) ({default_y1}): ").strip()
    y1 = float(input_y1) if input_y1 else default_y1

    input_y2 = input(f"y2 üçün başlanğıc qiyməti daxil edin y2(0) ({default_y2}): ").strip()
    y2 = float(input_y2) if input_y2 else default_y2
    
    input_x4 = input(f"Aralığın sağ ucunu daxil edin x4 ({default_x4}): ").strip()
    x4 = float(input_x4) if input_x4 else default_x4
    
    input_eps1 = input(f"Tolerantlıq E1 ({default_eps1}): ").strip()
    eps1 = float(input_eps1) if input_eps1 else default_eps1

    input_eps2 = input(f"Tolerantlıq E2 ({default_eps2}): ").strip()
    eps2 = int(input_eps2) if input_eps2 else default_eps2
except ValueError:
    print("\nXəta: İlkin verilənlər səhv daxil edilmişdir!")
    exit(1)

# Giriş verilənlərinin yoxlanılması
if eps1 <= 0:
    print("\nXəta: Tolerantlıq E1 müsbət ədəd olmalıdır!")
    exit(1)

if x0 >= x4:
    print("\nXəta: İnteqrallama aralığının sol ucu sağ ucundan kiçik olmalıdır (x0 < x4)!")
    exit(1)

x = x0
h = x4 - x
s1 = 0
u = 0

print("-" * 75)
print(f"{'Addım':^8} | {'X':^10} | {'Addım (H)':^12} | {'Y1':^16} | {'Y2':^16}")
print("-" * 75)

step_count = 0
print(f"{step_count:^8d} | {x:^10.4f} | {'-':^12} | {y1:^16.8f} | {y2:^16.8f}")

max_steps = 1000
while step_count < max_steps:
    if x + 2.01 * h > x4:
        u = 1
        h = (x4 - x) / 2.0
        
    # Bir böyük addım (2H) və iki kiçik addım (H)
    y1_large, y2_large = rk4_step(x, y1, y2, 2 * h)
    
    y1_half, y2_half = rk4_step(x, y1, y2, h)
    y1_small, y2_small = rk4_step(x + h, y1_half, y2_half, h)
    
    accepted = True
    
    # y1 üçün nisbi fərq
    mag_l1 = get_magnitude(y1_large)
    mag_s1 = get_magnitude(y1_small)
    e3_1 = max(mag_l1, mag_s1)
    pow1 = max(e3_1, eps2)
    rel1 = abs(y1_small - y1_large) / (10 ** pow1)
    if rel1 > eps1:
        accepted = False
        
    # y2 üçün nisbi fərq
    mag_l2 = get_magnitude(y2_large)
    mag_s2 = get_magnitude(y2_small)
    e3_2 = max(mag_l2, mag_s2)
    pow2 = max(e3_2, eps2)
    rel2 = abs(y2_small - y2_large) / (10 ** pow2)
    if rel2 > eps1:
        accepted = False
        
    if not accepted:
        h = h / 2.0
        u = 0
        continue
        
    x = round(x + 2 * h, 10)
    y1 = y1_small
    y2 = y2_small
    step_count += 1
    
    print(f"{step_count:^8d} | {x:^10.4f} | {h:^12.6f} | {y1:^16.8f} | {y2:^16.8f}")
    
    if u == 1:
        print("=" * 75)
        print("  Nəticə:")
        print(f"    Son nöqtə (x)  : {x:.4f}")
        print(f"    Y1({x:.2f})       : {y1:.8f}")
        print(f"    Y2({x:.2f})       : {y2:.8f}")
        print("=" * 75)
        break
        
    if s1 == 5:
        s1 = 0
        h = 2 * h
    s1 += 1
