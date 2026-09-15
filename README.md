# Numerical Methods and Algorithms in Python

### Pythonda Ədədi Üsullar və Onların Alqoritmləri

Bu repozitoriya **"Pythonda Bəzi Ədədi Üsulların Alqoritmləri"** (Azərbaycan Texniki Universiteti, 2026) metodiki vəsaitində təqdim olunan klassik ədədi analiz alqoritmlərinin və hesablama üsullarının rəsmi Python realizasiyalarını ehtiva edir.

Bütün proqramlar təmiz Python 3 sintaksisi ilə yazılmışdır və əlavə xarici asılılıq (kitabxana) tələb etmədən standart riyazi modullarla (`math`) işləyir.

---

## 📚 Mündəricat və Üsullar (Methods Overview)

### I FƏSİL: Qeyri-Xətti Tənliklərin Təqribi Həlli Üsulları

- **[1.2] Parçanın Ardıcıl Yarıya Bölünməsi Üsulu (Bisection Method):**  
  `Codes/1.2_parcanin_yariya_bolunme_usulu.py`  
  _Kökü özündə saxlayan parçanın addım-addım yarıya bölünərək verilmiş $\varepsilon$ dəqiqliyi ilə kökün tapılması._
- **[1.4] Vətərlər (Kəsənlər) Üsulu (Secant / Regula Falsi Method):**  
  `Codes/1.4_veterler_usulu.py`  
  _Əyri üzərində vətərlərin absis oxu ilə kəsişmə nöqtələrinin xətti yaxınlaşması ilə sürətli kök axtarışı._
- **[1.6] Toxunanlar (Nyuton-Rafson) Üsulu (Newton-Raphson Method):**  
  `Codes/1.6_toxunanlar_usulu.py`  
  _Funksiyanın törəməsindən istifadə edərək toxunanların $Ox$ oxunu kəsdiyi nöqtələrlə kvadratik yığılma sürəti._
- **[1.8] Sadə İterasiya Üsulu (Fixed-Point Iteration):**  
  `Codes/1.8_sade_iterasiya_usulu.py`  
  _$f(x)=0$ tənliyinin $x = \varphi(x)$ şəklinə gətirilərək ardıcıl iterasiyalarla həlli._

---

### II FƏSİL: Xətti Cəbri Tənliklər Sistemlərinin Həlli

- **[2.1] Qauss Üsulu (Gauss Elimination with Partial Pivoting):**  
  `Codes/2.1_qauss_usulu.py`  
  _Düzünə gedişdə sıfıra bölünmə və yuvarlaqlaşdırma xətalarını minimuma endirmək üçün baş sütun üzrə ən böyük əsas element seçimi və tərs gediş._
- **[2.4] Xətti Sistemlərin Sadə İterasiya (Yakobi) Üsulu (Jacobi Iteration):**  
  `Codes/2.4_sistemlerin_sade_iterasiya_usulu.py`  
  _Diaqonal üstünlüyə malik matrislər üçün paralel ardıcıl yaxınlaşmalar üsulu._
- **[2.7] Zeydel Üsulu (Gauss-Seidel Method):**  
  `Codes/2.7_zeydel_usulu.py`  
  _Hesablanmış yeni məchul qiymətlərinin dərhal cari iterasiyada istifadə olunması ilə sürətləndirilmiş yığılma._

---

### III FƏSİL: Müəyyən İnteqralın Ədədi Hesablanması (Kvadratura Üsulları)

- **[3.1] Orta Düzbucaqlılar Üsulu (Midpoint Rectangle Rule):**  
  `Codes/3.1_orta_duzbucaglilar_usulu.py`  
  _Elementar parçaların orta nöqtələrindəki qiymətlər əsasında Runqe qaydası ilə adaptiv addımlı inteqrallama._
- **[3.2] Trapeslər Üsulu (Trapezoidal Rule):**  
  `Codes/3.2_trapesler_usulu.py`  
  _Xətti interpolyasiya və Runqe xəta qiymətləndirməsi ilə sahənin təqribi hesablanması._
- **[3.3] Simpson (Parabolalar) Üsulu (Simpson's 1/3 Rule):**  
  `Codes/3.3_simpson_usulu.py`  
  _Parabolik interpolyasiya vasitəsilə 3-cü dərəcəyə qədər çoxhədlilər üçün tam dəqiq inteqral qiymətinin alınması._

---

### IV FƏSİL: Adi Diferensial Tənliklərin Ədədi Həlli (Koşi Məsələsi)

- **[4.2] Birtərtibli ADT-nin Eyler Üsulu ilə Həlli (Euler's Method):**  
  `Codes/4.2_eyler_usulu.py`  
  _Klassik 1-ci tərtib addımlama üsulu ($O(h)$ dəqiqlik)._
- **[4.3] 4-cü Tərtib Runge-Kutta Üsulu (Classical 4th Order Runge-Kutta - RK4):**  
  `Codes/4.3_runge_kutta_usulu.py`  
  _Dörd aralıq meyillilik əmsalı ($k_1, k_2, k_3, k_4$) ilə yüksək dəqiqlikli $O(h^4)$ inteqrallama._
- **[4.6] Diferensial Tənliklər Sisteminin Runge-Kutta Üsulu (RK4 for ODE Systems):**  
  `Codes/4.6_sistemlerin_runge_kutta_usulu.py`  
  _Əlaqəli birtərtibli tənliklər sistemlərinin (məsələn, harmonik ossilyator) vektorlaşdırılmış RK4 həlli._
- **[4.7] Addımı Avtomatik Seçməklə (Adaptiv) Runge-Kutta Üsulu (Adaptive Step-size RK):**  
  `Codes/4.7_sistemlerin_runge_kutta_adaptiv.py`  
  _Yerli xətaya nəzarət edərək addım ölçüsünü ($h$) dinamik tənzimləyən optimallaşdırılmış alqoritm._

---

### V FƏSİL: Kompleks Ədədlər üzərində Əməllər və Kökalma

- **[5.1] Kompleks Ədədin Həqiqi Qüvvətə Yüksəldilməsi (Real Power of Complex Number):**  
  `Codes/5.1_kompleks_quvvet.py`  
  _Qütb forması və faza tənzimləməsi ilə $z^w$ ($w \in \mathbb{R}$) hesablanması._
- **[5.2] Kompleks Ədədin Kompleks Qüvvətə Yüksəldilməsi (Complex Power of Complex Number):**  
  `Codes/5.2_kompleks_kompleks.py`  
  _Çoxqiymətli $z^w = e^{w \cdot \mathrm{Ln}(z)}$ funksiyasının seçilmiş budaq üzrə analitik həlli._
- **[5.3] Kompleks Ədəddən Kökalma Alqoritmi (Roots of Complex Numbers - De Moivre):**  
  `Codes/5.3_kompleks_kok.py`  
  _Muavr düsturundan istifadə edərək $\sqrt[n]{z}$ kompleks köklərinin tam spektrinin tapılması._

---

## 🚀 Quraşdırma və İcra (Getting Started)

### Tələblər:

- **Python 3.8+** (heç bir xarici paket tələb olunmur, standart `math` kitabxanası kifayətdir).

### İcra qaydası:

Repozitoriyanı klonlayın və istədiyiniz alqoritmi terminalda işə salın:

```bash
git clone https://github.com/SahibAlibabayev/numerical-methods-python.git
cd numerical-methods-python

# Nümunə: Vətərlər üsulunu icra etmək
python Codes/1.4_veterler_usulu.py

# Nümunə: Simpson üsulunu icra etmək
python Codes/3.3_simpson_usulu.py

# Nümunə: Runge-Kutta üsulunu icra etmək
python Codes/4.3_runge_kutta_usulu.py
```

Bütün proqramlar interaktiv rejimdə işləyir: istifadəçi öz parametrlərini daxil edə bilər və ya birbaşa **Enter** sıxaraq kitabda göstərilən ilkin test qiymətlərini qəbul edə bilər.

---

## 👨‍💻 Müəlliflər və Elmi İstinad

- **Həsən Vəliyev** — Dosent, Azərbaycan Texniki Universiteti (AzTU)
- **Sahib Əlibabayev** — Bakalavr, Azərbaycan Texniki Universiteti (AzTU)
