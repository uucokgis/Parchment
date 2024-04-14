from datetime import datetime

from parsomen.db.collections import BlokCollection, HamurCollection, ParsomenCollection, ParsomenAyarCollection

BlokCollection.collection.insert_many([
    {
        # "_id": 1,
        "parsomenNo": 1,
        "hamurNo": 1,
        "icerik": {"tipi": "Text", "data": "Example Data"},
        "sira": 1,
        "yer": 1,
        "uretilmeTarihi": datetime.now(),
        "duzenlenmeTarihi": datetime.now(),
    },
    {
        "parsomenNo": 1,
        "hamurNo": 1,
        "icerik": {"tipi": "Text", "data": "Example Data"},
        "sira": 2,
        "yer": 1,
        "uretilmeTarihi": datetime.now(),
        "duzenlenmeTarihi": datetime.now(),
    }
])

# Örnek bir Hamur ekleme
HamurCollection.collection.insert_one({
    # "_id": 1,
    "parsomenNo": 1,
    "bloklar": [1, 2],  # Blok id'leri sıralı gelecek
    "siraNo": 1
})

# Örnek bir Parsomen ekleme
ParsomenCollection.collection.insert_one({
    # "_id": 1,
    "baslik": "Example Title",
    "hamurlar": [1],  # Hamur id'leri sıralı gelecek
})

# Örnek bir ParsomenAyar ekleme
ParsomenAyarCollection.collection.insert_one({
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
