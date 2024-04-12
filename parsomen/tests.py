from datetime import datetime

from db.blok import blok_koleksiyonu
from db.hamur import hamur_koleksiyonu
from db.parsomen import parsomen_koleksiyonu
from db.parsomen_ayar import parsomen_ayar_koleksiyonu

blok_koleksiyonu.insert_many([
    {
        # "_id": 1,
        "icerik": {"tipi": "Text", "data": "Example Data"},
        "sira": 1,
        "yer": 1,
        "uretilmeTarihi": datetime.now(),
        "duzenlenmeTarihi": datetime.now(),
    },
    {
        # "_id": 2,
        "icerik": {"tipi": "Text", "data": "Example Data"},
        "sira": 2,
        "yer": 1,
        "uretilmeTarihi": datetime.now(),
        "duzenlenmeTarihi": datetime.now(),
    }
])

# Örnek bir Hamur ekleme
hamur_koleksiyonu.insert_one({
    # "_id": 1,
    "parsomenNo": 1,
    "bloklar": [1, 2],  # Blok id'leri sıralı gelecek
    "siraNo": 1
})

# Örnek bir Parsomen ekleme
parsomen_koleksiyonu.insert_one({
    # "_id": 1,
    "baslik": "Example Title",
    "hamurlar": [1],  # Hamur id'leri sıralı gelecek
})

# Örnek bir ParsomenAyar ekleme
parsomen_ayar_koleksiyonu.insert_one({
    # "_id": 1,
    "parsomenNo": 1,
    "sonYer": 1,
    "cizimAyarlari": {
        "renk": "#0000FF",
        "buyukluk": 1,
        "font": "Arial"
    },
    "metinAyarlari": {
        "renk": "#0000FF",
        "buyukluk": 1,
        "font": "Arial"
    },
    "sayfaliMi": False,
    "satirliMi": False
})