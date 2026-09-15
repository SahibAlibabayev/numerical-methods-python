import math

# Sistem tənlikləri: y1' = y2, y2' = -y1
def f1(x, y1, y2):
    return y2

def f2(x, y1, y2):
    return -y1

# Başlanğıc verilənlər
default_x0 = 0.0
default_y1 = 1.0
default_y2 = 0.0
default_x1 = 2.0
default_m = 20
print("-" * 65)
print("  DİFERENSİAL TƏNLİKLƏR SİSTEMİNİN RUNQE-KUTTA ÜSULU İLƏ HƏLLİ")
print("-" * 65)
print("Qeyd: 2 tənlikdən ibarət ADT sistemi həll edilir.")
print("İnteqrallama aralığının sol ucu sağ ucundan kiçik olmalıdır (x0 < x1).")
print("Addım sayısı (M) müsbət tam ədəd olmalıdır.")
print("-" * 65)
print("Mötərizədəki qiymətləri seçmək üçün birbaşa Enter düyməsini sıxa bilərsiniz.\n")

try:
    input_x0 = input(f"Başlanğıc nöqtəni daxil edin x0 ({default_x0}): ").strip()
    x0 = float(input_x0) if input_x0 else default_x0
    
    input_y1 = input(f"y1 üçün başlanğıc qiyməti daxil edin y1(0) ({default_y1}): ").strip()
    y1 = float(input_y1) if input_y1 else default_y1

    input_y2 = input(f"y2 üçün başlanğıc qiyməti daxil edin y2(0) ({default_y2}): ").strip()
    y2 = float(input_y2) if input_y2 else default_y2
    
    input_x1 = input(f"Aralığın sağ ucunu daxil edin x1 ({default_x1}): ").strip()
    x1 = float(input_x1) if input_x1 else default_x1
    
    input_m = input(f"Addımların sayını daxil edin M ({default_m}): ").strip()
    m = int(input_m) if input_m else default_m
except ValueError:
    print("\nXəta: İlkin verilənlər səhv daxil edilmişdir!")
    exit(1)

# Giriş verilənlərinin yoxlanılması
if m <= 0:
    print("\nXəta: Addım sayı (M) müsbət tam ədəd olmalıdır!")
    exit(1)
if x0 >= x1:
    print("\nXəta: İnteqrallama aralığının sol ucu sağ ucundan kiçik olmalıdır (x0 < x1)!")
    exit(1)

h = (x1 - x0) / m
x = x0
print("-" * 55)
print(f"{'Addım':^8} | {'X':^10} | {'Y1':^16} | {'Y2':^16}")
print("-" * 55)
print(f"{0:^8d} | {x:^10.4f} | {y1:^16.8f} | {y2:^16.8f}")

for i in range(1, m + 1):
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
    x_new = round(x0 + i * h, 10)

    y1 = y1_new
    y2 = y2_new
    x = x_new
    
    print(f"{i:^8d} | {x:^10.4f} | {y1:^16.8f} | {y2:^16.8f}")
print("=" * 55)
print("  Nəticə:")
print(f"    Son nöqtə (x)  : {x:.4f}")
print(f"    Y1({x:.2f})       : {y1:.8f}")
print(f"    Y2({x:.2f})       : {y2:.8f}")
print("=" * 55)
