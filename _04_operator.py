################################################################
# Operators

#####################################################################################
#### Operator #######################################################################
#  Aritmetik Operatörler: Temel matematiksel işlemleri gerçekleştirir (toplama, çıkarma, çarpma vb.).
#  Atama Operatörleri: Değişkenlere değer atar ve karmaşık işlemlerle kısayol atamalarını sağlar.
#  Karşılaştırma Operatörleri: İki değeri karşılaştırır ve mantıksal sonuçlar döndürür.
#  Mantıksal Operatörler: Birden fazla koşulun doğru olup olmadığını kontrol eder.
#  Bit Düzeyinde Operatörler: Sayılar üzerinde bit bazında işlem yapar.
#  Üyelik Operatörleri: Bir değerin bir veri yapısının üyesi olup olmadığını kontrol eder.
#  Kimlik Operatörleri: İki nesnenin aynı bellek adresine sahip olup olmadığını kontrol eder.

"""
1-) Aritmetik Operators
    a) Toplama: +
    b) Çıkarma: -
    c) Çarpma: *
    d) Bölme: /
    e) Mod: %
    f) Üs Alma: **
    g) Kalan Sayı Bulma: //


2-) Atama Operators
    a) Eşittir: =
    b) Artı Eşittir: +=
    c) Çıkar Eşittir: -=
    d) Bölme Eşittir: /=
    e) Mod Eşittir: %=
    f) Üs Alma Eşittir: **=
    g) Kalan Sayı Bulma Eşittir: //=

3-) Karşılaştırma Operators
    a) Eşittir: ==
    b) Eşit Değil: !=
    c) Büyük Eşittir: >=
    d) Büyük Değil: <=
    e) Küçük Eşittir: <

4-) Mantıksal Operators
    a) VEYA: or
    b) VE: and
    c) Değil: not

5-) Bit Düzeyinde (Bitwise) Operators  (Bit Düzeyinde: 0 ve 1 olanlardır)
    a) Bitwise AND: &
    b) Bitwise OR: |
    c) Bitwise XOR: ^
    d) Bitwise NOT: ~
    e) Bitwise Left Shift: <<
    f) Bitwise Right Shift: >>
    g) Bitwise Right Shift (unsigned): >>


5-) Atanma ve İfadeler
    a) İfadeleri Birleştirir: +, -, *, /, %, **, //, ==,!=, >, <, >=, <=, or, and, not
    b) Atama İfadesi: =, +=, -=, *=, /=, %=, **=, //=
    c) İfadeleri Öncelik Belirlemek için Parantezler: ()
    d) İfadeleri Birleştirirken İç içe kullanmak için Parantezler: ()
    e) İfadeleri Birleştirirken Boşluklarla veya İfadeler arasında Boşluklar: ()
    f) İfadeleri Birleştirirken İfadeler arasında ��arpanlar: ()
    g) İfadeleri Birleştirirken İfadeler arasında Kullanılan Operatörler: +, -, *, /, %, **, //, ==,!=, >, <, >=, <=, or, and, not

6-) Üyelik Operatör
    a) İçinde İçe Kullanılan İfadeler: in
    b) İçinde İçe Kullanılmamış İfadeler: not in
    c) İçinde İçe Kullanılan İfadeler: is

7-) Kimlik Operators
    a) Kopyalanan İfadeler: =
"""


#####################################################################################
#### Sayısal İşlemler Dört İşlem ####################################################
a=15
b=4
print("Toplama= ",a+b)
print("Çıkarma= ",a-b)
print("Çarpma= ",a*b)
print("Virgüllü Bölme= ",a/b)
print("Tam Sayıya Bölme= ",a//b)
print("Module Bölme= ",a%b)
print("Üslü Sayılar= ",a**b)


#####################################################################################
#### Sayısal İşlemler Mantıksal İşlem ###############################################
print("Eşit mi ",a==b)
print("Eşit Değil mi ",a!=b)
print("Büyük mü ",a>b)
print("Büyük mü, Eşit mi ",a>=b)
print("Küçük mü ",a<b)
print("Küçük mü, Eşit mi  ",a<=b)

#####################################################################################
#### Atama  #####################################################

# Atama
data=10
print(data)

# Topla ve Ata
data+=15
print("Topla ve Ata: ",data)

# Çıkar ve Ata
data-=10
print("Çıkar ve Ata: ",data)

# &=     | Bit düzeyinde VE ve Ata      | x &= 3          |
# |=     | Bit düzeyinde VEYA ve Ata    | x |= 3          |
# ^=     | Bit düzeyinde XOR ve Ata     | x ^= 3          |
# >>=    | Bit kaydırma sağa ve Ata     | x >>= 3         |
# <<=    | Bit kaydırma sola ve Ata     | x <<= 3         |