import matplotlib.pyplot as plt
from collections import Counter

from matplotlib.lines import lineStyles
from scipy.stats import alpha

######################################################################################


"""
Gerçek Hayat Problemi: Blog Yönetim Sistemi ve İçerik Analizi
Senaryo: Bir blog yönetim sisteminiz var ve bu sistem üzerinden yazarlar içerik yayımlıyor.
Blog içeriği üzerinde çeşitli analizler yaparak yazar performansını ölçmek,
popüler içerikleri belirlemek, cok kullanılan kelimeleri analiz etmek ve kullanıcıların ilgisini çeken konuları keşfetmek istiyorsunuz.

Aşağıda Python ile bir blog yönetim sistemi için geniş kapsamlı bir içerik analizi örneği verilmiştir.
"""

# Örnek blog içerikleri
blog_icerikleri = [
    {
        "blog_id": 1,
        "yazar": "ali123",
        "baslik": "Python Programlama Rehberi",
        "icerik": "Python programlama diliyle ilgili başlangıç seviyesinden ileri düzeye kadar detaylı bilgiler içerir. Öğrenmesi kolay ve güçlü bir dildir.",
        "kategori": "Programlama",
        "goruntulenme": 1500,
        "yorumlar": [
            {"kullanici": "ayse456", "yorum": "Gerçekten harika bir rehber, çok faydalı!"},
            {"kullanici": "mehmet789", "yorum": "Bilgilendirici ama biraz daha örnek olsa iyi olurdu."},
        ],
    }, {
        "blog_id": 2,
        "yazar": "ayse123",
        "baslik": "Web Geliştirme için HTML ve CSS",
        "icerik": "Web geliştirme dünyasına giriş yapmak isteyenler için HTML ve CSS konularında temel bilgiler sunar. İyi bir başlangıç rehberi.",
        "kategori": "Web Geliştirme",
        "goruntulenme": 2000,
        "yorumlar": [
            {"kullanici": "ali123", "yorum": "Çok net ve açıklayıcı bir yazı, teşekkürler!"}
        ],
    },
    {
        "blog_id": 3,
        "yazar": "mehmet123",
        "baslik": "Makine Öğrenimi Nedir?",
        "icerik": "Makine öğrenimi, yapay zeka alanında bir alt daldır. Bu yazı, temel kavramlar ve uygulama alanlarını ele alır.",
        "kategori": "Yapay Zeka",
        "goruntulenme": 800,
        "yorumlar": [
            {"kullanici": "ayse456", "yorum": "Makine öğrenimi konusuna güzel bir giriş olmuş."},
            {"kullanici": "fatma321", "yorum": "Daha fazla teknik detay verilseydi çok daha faydalı olurdu."},
        ],
    },
    {
        "blog_id": 4,
        "yazar": "zeynep123",
        "baslik": "SEO Teknikleriyle Blog Trafiğini Artırma-1",
        "icerik": "SEO, web sitenizin arama motorlarında üst sıralarda yer almasını sağlar. Bu yazı, etkili SEO tekniklerini içerir.",
        "kategori": "Dijital Pazarlama",
        "goruntulenme": 2500,
        "yorumlar": [
            {"kullanici": "mehmet789", "yorum": "Çok işime yaradı, teşekkürler!"},
            {"kullanici": "ali123", "yorum": "SEO'yu iyi anlatmışsınız, pratik teknikler için güzel bir rehber."},
        ],
    }, {
        "blog_id": 5,
        "yazar": "zeynep456",
        "baslik": "SEO Teknikleriyle Blog Trafiğini Artırma-2",
        "icerik": "SEO, web sitenizin arama motorlarında üst sıralarda yer almasını sağlar. Bu yazı, etkili SEO tekniklerini içerir.",
        "kategori": "Dijital Pazarlama",
        "goruntulenme": 2800,
        "yorumlar": [
            {"kullanici": "mehmet789", "yorum": "Çok işime yaradı, teşekkürler!"},
            {"kullanici": "ali123", "yorum": "SEO'yu iyi anlatmışsınız, pratik teknikler için güzel bir rehber."},
            {"kullanici": "ali1234", "yorum": "SEO'yu iyi anlatmışsınız, pratik teknikler için güzel bir rehber."},
        ],
    },

]

"""
    Kodun Özellikleri
    Blog Sayısı ve Kategorilere Dağılım: Blog sayısını ve kategorilere göre dağılımını analiz eder.
    Popülerlik: Görüntülenme sayısına göre en popüler blogları belirler.
    Kelime Analizi: İçeriklerde cok kullanılan kelimeleri analiz ederek ilgi çekici noktaları ortaya çıkarır.
    Yazar Performansı: Yazarların içeriklerini analiz ederek görüntülenme sayılarını ölçer.
    Yorum Analizi: Bloglara yapılan yorum sayısını ve kullanıcıların katkılarını analiz eder.
    Bu örnek, bir blog yönetim sisteminin nasıl analiz edilebileceğini gösterir ve gerçek hayatta uygulanabilir bir çözüm sunar. 
"""
################################################################################################
# 1. Blogların toplam sayısı listeleyerek.
toplam_blog = len(blog_icerikleri)
print(f"Toplam Blog Sayısı: {toplam_blog}")


################################################################################################
# 2. Kategorilere göre blog sayısı listeleyerelim ve Çizgisel görselleştirin.
# Kategorilere göre blog sayısı bulalım.
def kategorilere_gore_blog_sayisi_cizgisel_grafik(blog_icerikleri):
    """
      Blog içeriklerini alsın ve kategorilere göre blog sayısını bulsun ve grafiğibi çizsin

      parametre:
          blog_icerikleri(list): Blog verilerinin bulunduğu liste
    """
    print("\n\rKategorilere Göre Blog Sayısı:")

    # Kategoriye göre blog sayısını tutan dictionary
    kategori_sayilari = {}
    for blog in blog_icerikleri:
        kategori = blog["kategori"]
        # Eğer kategori varsa kategori sayısını değeri 1 artır
        # Yoksa varsayılan değer olan `0` eklesin. (0:Etkisiz eleman)
        kategori_sayilari[kategori] = kategori_sayilari.get(kategori, 0) + 1

    # Pythonda kategori_sayilari.items()
    # bir dictionary yapısınıdaki öğerlere erişmek için kullanılan metottur
    # items(): sözlüğün tüm anahtar-değer çiftleri döndürür
    for kategori, sayi in kategori_sayilari.items():
        print(f"{kategori}: {sayi} adet")

    ### GRAFIK CIZ ########################################################
    # Verileri Hazırlama
    # key: kategorilerin isimlerini versin
    # value: Blog sayıları
    pilot_key_kategoriler = list(kategori_sayilari.keys())
    pilot_value_blog_sayilari = list(kategori_sayilari.values())

    # Çubuk grafik çizimi
    # Grafik alanını genişlik, yüksekliklerini ayalarlıyalım
    # genişlik:8, yükseklik:5
    plt.figure(figsize=(8, 5))  # Grafik boyutunu gösterecek

    # Çubuk grafik
    # plt.bar(X,Y,color='skyblue',edgecolor="black",alpha=0.8)
    # X: pilot_key_kategoriler
    # Y: pilot_value_blog_sayilari(Yani Yükseklik)
    # color: çubuk rengi
    # edgecolor: kenar rengi
    plt.bar(pilot_key_kategoriler, pilot_value_blog_sayilari, color='skyblue', edgecolor="black", alpha=0.8)

    # Çubuk Title (Grafiğin Başlığı)
    plt.title("Kategorilere Göre Blog Sayısı", color="blue", fontsize=18, fontweight='bold')

    # X: pilot_key_kategoriler Renk
    plt.xlabel("Kategoriler", color="red", fontsize=14, fontweight='bold', labelpad=10)

    # Y: pilot_value_blog_sayilari Renk
    plt.ylabel("Blog Sayısı", color="red", fontsize=14, fontweight='bold', labelpad=10)

    # rotation=30: Kategori isimlerini 30 derece eğimle yazdırır.
    # fontsize=10: X ekseni yazılarının boyutunu belirler.
    plt.xticks(rotation=30, fontsize=12, color='darkred')  # X ekseni yazıları

    # Bu kodun görevi, bir grafik üzerindeki çubukların (barların) üzerine etiket eklemektir
    for i, val in enumerate(pilot_value_blog_sayilari):
        plt.text(i, val + 0.2, str(val), ha='center', fontsize=12, color='darkgreen', fontweight='bold')

    # Renkli Grafikler için beyaz arayüz eklemek
    plt.gca().set_facecolor("white")

    # X ve Y  eksen çizgileri
    plt.gca().spines['bottom'].set_linewidth(1.4)
    plt.gca().spines['left'].set_linewidth(1.4)

    # axis: y : ASdece Y ekseni boyunca ızgaları çizer
    # Y eksi için ızgara
    plt.grid(axis='y', linestyle="--", alpha=0.8)

    # Gragik elemanlarını düzenin optimize etmek
    plt.tight_layout()

    # Grafikleri kaydet
    plt.savefig("kategorilere_gore_blog_sayisi_grafik.png", dpi=350)  # Grafiği kaydet

    # Grafiği Ekranda Göster
    plt.show()

# Fonksiyonu çağırmak ve Grafiği çizdirmek
kategorilere_gore_blog_sayisi_cizgisel_grafik(blog_icerikleri)

################################################################################################
# 2. Kategorilere göre blog sayısı listeleyerelim ve Çizgisel görselleştirin.
# Kategorilere göre blog sayısı bulalım.
def kategorilere_gore_blog_sayisi_dairesel_grafik(blog_icerikleri):
    """
      Blog içeriklerini alsın ve kategorilere göre blog sayısını bulsun ve grafiğibi çizsin

      parametre:
          blog_icerikleri(list): Blog verilerinin bulunduğu liste
    """
    print("\n\rKategorilere Göre Blog Sayısı:")

    # Kategoriye göre blog sayısını tutan dictionary
    kategori_sayilari = {}
    for blog in blog_icerikleri:
        kategori = blog["kategori"]
        # Eğer kategori varsa kategori sayısını değeri 1 artır
        # Yoksa varsayılan değer olan `0` eklesin. (0:Etkisiz eleman)
        kategori_sayilari[kategori] = kategori_sayilari.get(kategori, 0) + 1

    # Pythonda kategori_sayilari.items()
    # bir dictionary yapısınıdaki öğerlere erişmek için kullanılan metottur
    # items(): sözlüğün tüm anahtar-değer çiftleri döndürür
    for kategori, sayi in kategori_sayilari.items():
        print(f"{kategori}: {sayi} adet")

    ### GRAFIK CIZ ########################################################
    # Verileri Hazırlama
    # key: kategorilerin isimlerini versin
    # value: Blog sayıları
    pilot_key_kategoriler = list(kategori_sayilari.keys())
    pilot_value_blog_sayilari = list(kategori_sayilari.values())

    plt.figure(figsize=(8,8))

    # Dairesel Grafik
    # Dairesel dilimlerin yüzdelik oranları: autopct='%1.1f%%'
    # Pasta grafiğinin başlangıç açısı: startangle=150,
    # Otomatik renkler: colors=plt.cm.Paired.colors:
    plt.pie(pilot_value_blog_sayilari,labels=pilot_key_kategoriler, ,startangle=140, colors=plt.cm.Paired.colors)

    plt.title("Kategorilere Göre Blog Sayısı Dairesel Grafik", color="blue", fontsize=18, fontweight='bold')

    # Grafikleri kaydet
    plt.savefig("kategorilere_gore_blog_sayisi_grafik.png", dpi=350)  # Grafiği kaydet

    # Grafiği Ekranda Göster
    plt.show()

# Fonksiyonu çağırmak ve Grafiği çizdirmek
kategorilere_gore_blog_sayisi_dairesel_grafik(blog_icerikleri)

################################################################################################
# 3. Yazar başına yazılan blog sayısı listeleyerek görselleştirin.
