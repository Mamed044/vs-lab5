# 1. Math kitabxanasını (kütüphanesini) daxil edirik, çünki ln və arctan funksiyalarından istifadə edəcəyik.
import math

# 2. Kölünü tapmağa çalışdığımız funksiyanı təyin edirik: ln(x) - arctan(x)
def f(x):
    return math.log(x) - math.atan(x)

# 3. Köl aralığını təyin edirik: [3.0, 4.0]
a = 3.0
b = 4.0

# 4. Dəqiqlik səviyyəsini təyin edirik
e = 0.001

# 5. Kölü tapmaq üçün ikinci dərəcədə bir metod istifadə edəcək funksiyamızı təyin edirik.
def find_root(a, b, e):
    # 6. İlk yoxlama: Başlanğıc nöqtələrində funksiya dəyərlərini yoxlayırıq.
    if f(a) * f(b) >= 0:
        print("Verilmiş aralıqda kök yoxdur.")
        return None

    # 7. Kök tapma prosesi başlayır
    while (b - a) >= e:
        # 8. Orta nöqtəni tapırıq
        c = (a + b) / 2 
        
        # 9. Əgər orta nöqtə köksə, tez çıxıb dəyəri qaytarırıq
        if f(c) == 0:
            return c
        # 10. Kök aralığındakı işarə dəyişiminə görə aralığı yeniləyirik
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    # 11. Dəqiqlikə çatıldığında və ya müəyyən bir iterasiya sayına çatıldığında nəticəni qaytarırıq
    return (a + b) / 2

# 12. Kök tapma funksiyasını çağıraraq kölü tapırıq
root = find_root(a, b, e)

# 13. Əgər kök tapılıbsa, kökü ekrana yazdırırıq
if root is not None:
    print("Köl:", root)
