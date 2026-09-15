import math
def f(x, y):
    return x ** 3 + y

# Başlanğıc verilənlər
default_x0 = 0.0
default_y0 = 1.0
default_b = 1.0
default_n = 10
print("-" * 55)
print("  BİRTƏRTİBLİ ADT-NİN EYLER ÜSULU İLƏ HƏLLİ")
print("-" * 55)
print("Qeyd: Məsələ y' = x^3 + y, y(x0) = y0 başlanğıc şərti ilə həll edilir.")
print("İnteqrallama aralığının sol ucu sağ ucundan kiçik olmalıdır (x0 < B).")
print("Addım sayısı (N) müsbət tam ədəd olmalıdır.")
print("-" * 55)
print("Mötərizədəki qiymətləri seçmək üçün birbaşa Enter düyməsini sıxa bilərsiniz.\n")

try:
    input_x0 = input(f"Başlanğıc nöqtəni daxil edin x0 ({default_x0}): ").strip()
    x0 = float(input_x0) if input_x0 else default_x0
    
    input_y0 = input(f"Başlanğıc qiyməti daxil edin y0 ({default_y0}): ").strip()
    y0 = float(input_y0) if input_y0 else default_y0
    
    input_b = input(f"Aralığın sağ ucunu daxil edin B ({default_b}): ").strip()
    b = float(input_b) if input_b else default_b
    
    input_n = input(f"Addımların sayını daxil edin N ({default_n}): ").strip()
    n = int(input_n) if input_n else default_n
except ValueError:
    print("\nXəta: İlkin verilənlər səhv daxil edilmişdir!")
    exit(1)

# Giriş verilənlərinin yoxlanılması
if n <= 0:
    print("\nXəta: Addım sayı (N) müsbət tam ədəd olmalıdır!")
    exit(1)

if x0 >= b:
    print("\nXəta: İnteqrallama aralığının sol ucu sağ ucundan kiçik olmalıdır (x0 < B)!")
    exit(1)

h = (b - x0) / n
x = x0
y = y0

print("-" * 45)
print(f"{'Addım':^8} | {'X':^12} | {'Y':^18}")
print("-" * 45)
print(f"{0:^8d} | {x:^12.4f} | {y:^18.8f}")

for i in range(1, n + 1):
    # Eyler üsulunun riyazi ifadəsi: y_new = y + h * f(x, y)
    y_new = y + h * f(x, y)
    x_new = round(x0 + i * h, 10)
    
    y = y_new
    x = x_new
    
    print(f"{i:^8d} | {x:^12.4f} | {y:^18.8f}")
print("=" * 45)
print("  Nəticə:")
print(f"    Son nöqtə (x)  : {x:.4f}")
print(f"    Eyler ilə y(x) : {y:.8f}")
print("=" * 45)
