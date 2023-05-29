from django.db import models

class BaseModel(models.Model):
    updated_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True

class Brand(BaseModel):
    name=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

# Earphone child 
class Category(BaseModel):
    name=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
class Seller(BaseModel):
    name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Product(BaseModel):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    price=models.PositiveBigIntegerField()
    discount_price=models.PositiveBigIntegerField(null=True,blank=True) 
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    product_type=models.CharField(max_length=200,choices=(
        ("life style","life style"),
        ("mobile phone accesories","mobile phone accesories")
    ))
    warranty_period=models.CharField(max_length=200,choices=(
        ("3days warranty","3days warranty"),
        ("3months warranty","3months warranty"),
        ("no warranty","no warranty"),
       
    ))
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title 
    
    @property
    def image(self):
        return ProductImage.objects.filter(product__id=self.id).last().image 
        

class ProductImage(BaseModel):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="media/products")

    def __str__(self) -> str:
        return self.product.title 
    
