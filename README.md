# Parşömen
Parşömen doküman bazlı bir not tutma platformudur.
Mobil, web, desktop platformlarınd yönetilebilir.

Arayüz bir kitap ile tıpatıptır. Sağ kapakta postitler üstte ayraçlar solda fihrist(arama)
ve ön yüzde kitap kapağınız.

* Parşömenler sonsuz uzunluktadır
* Parşömenler dallanabilir (branch)
* Blok: Metin | Çizim | Resim | Video | Çıkartma | Ayraç | Post-It
* Ayraçlar arasında kolay gezinti
* Çıkartma yapıştırılıp çıkarılabilir sonraya saklanabilir
* Post-It ve çıkartma bloktur. Ancak parşömene dönüştürülebilirler (dal)
* Çıkartmalar parşömen içindedir. Post-it'ler ise yana uzar ve parşömen içi
ayraç işini görebilir.
* Ayarlı sayfalama yapılabilir
* (Gelecekte) Obsiden akıl haritası desteği

Tech stack: MongoDB-Flask-GrapHQL


## Teknik Doküman
Blok collection
Metin | Raster | Video tiplerinde ufak bloklardır. Bir paragraf veya resim veya çizim olabilir. Rasterlar
buluta yüklenip cloudinary id gibi referansla getirilecek. 
Şemada Hamur'un alt kümesidir. Blok <-> Hamur 1-1 

icerik tipi: Raster, Text
icerik data: GUID, full-text-data todo: (veya binData?)
sira: Hamur'daki sıra, order. 
Metinler zaten paragrafli olacağı için sıralı olur. Resimler de textler gibi siralanacaktir.
Tam dogru olmalarina gerek yok maksat indexte dogru yeri bulmak
yer: İmleç no. Her blok'un sayfa üzerinde pixel veya satır anlamında bir sırası var. Tam oraya konumlanacak. 

    # Blok:
    _id: ObjectId
    icerik: {tipi: String, data: String}
    sira: Number
    yer: Number
    
    # hepsinde olmalı (1)
    uretilmeTarihi: timestamp
    duzenlenmeTarihi: timestamp

Hamur collection
Hamur:
Hamurlar bloklardan oluşur ve parşömen ile 1-1 unique ilişkilidir.

    _id: ObjectId
    parsomenId: number
    bloklar: number []  # Blok id'leri sirali gelecek
    sira: number
    # (1)



Parşömen collection
Bir parşömen sonsuz uzunlukta olabilir. Genellikle hamurlardaki sıra noları ile filtrelenir.

Parsomen:

    parsomenNo: number
    _id: ObjectId
    baslik: String (200)
    hamurlar: number []  # Hamur id'leri sirali gelecek
    ayar: ParsomenAyar
    # (1)



ParsomenAyar:

    _id: ObjectId
    parsomenNo: number
    sonYer: number,
    cizimAyarlari: {
        renk: hex | String
        buyukluk: number
        font: String
        ...
    }
    metinAyarlari: {
         renk: hex | String
        buyukluk: number
        font: String
        ...
    }
    sayfaliMi: bool
    satirliMi: bool
    
