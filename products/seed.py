from .models import*
import random 

product_names=[
    "Motorola MOTO SP105 Sport Wireless In-Ear Headphones",
    "Yison Celebrat FLY-1 In-Ear Wired Earphone",
    "KZ HD9 HiFi In-Ear Sports Earphone",
    "UiiSii C1 Type-C Heavy Bass Earphone",
    "UiiSii CX Type-C Heavy Bass Earphone",
    "JOYROOM JR-EC01 Type-C Wired Earphone",
    "Realme Buds 2 Neo Wired Earphones (RMA2016)",
    "Rapoo EP28 Wired In Ear Phone",
    "Edifier H180 Hi-Fi Stereo In-ear Earphone",
    "Xiaomi Mi HSEJ03JY 3.5mm Earphone Basic",
    "Motorola EarBuds 3 In Ear Earphone"
]

def productSeed(limit=10):
    if limit>20:
        limit=20
    category=Category.objects.all()
    brand=Brand.objects.all()
    seller=Seller.objects.all()
    product_type=["life style","mobile phone accesories"]
    warranty_period=["3days warranty","3months warranty","no warranty"]

    for i in range(limit):
        Product.objects.create(
            category=random.choice(category),
            title=product_names[i],
            price=random.randint(100,999),
            brand=random.choice(brand),
            product_type=random.choice(product_type),
            warranty_period=random.choice(warranty_period),
            seller=random.choice(seller)
        )    
