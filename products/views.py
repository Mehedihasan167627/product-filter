from django.shortcuts import render,redirect
from django.views import View 
from django.http import JsonResponse
from django.db.models import Q 
from .models import Product,Category,Seller,Brand 

class EmptyView(View):
     def get(self,request):
          return redirect("products:products")

class ProductListView(View):
    def get(self,request):
        brands=Brand.objects.all()
        categories=Category.objects.all()
        sellers=Seller.objects.all()
        products=Product.objects.all().order_by("-id")
        max_price=Product.objects.all().order_by("price").last().price 
        min_price=Product.objects.all().order_by("-price").last().price 
        
        context={
            "brands":brands,
            "categories":categories,
            "sellers":sellers,
            "products":products,
            "range":{"min":min_price,'max':max_price}
        }
        return render(request,'products/product.html',context) 
    

class ProductFilterView(View):
    def get(self,request):
        min_price=request.GET.get("min_price")
        max_price=request.GET.get("max_price")
        brand=request.GET.getlist("brand[]")
        category=request.GET.getlist("category[]")
        product_type=request.GET.getlist("product_type[]")
        sellers=request.GET.getlist("sellers[]")
        warranty=request.GET.getlist("warranty[]")
        sorting=request.GET.get("sorting")
        products=Product.objects.filter(
            price__gte=min_price,price__lte=max_price
        )
        if not brand:
            brand=[obj.id for obj in Brand.objects.all()]
        if not category:
            category=[obj.id for obj in Category.objects.all()]
        if not product_type:
                product_type=["life style","mobile phone accesories"]
        if not sellers:
              sellers=[obj.id for obj in Seller.objects.all()]
        if not warranty:
                warranty=["3days warranty","3months warranty","no warranty"]
        if not category:
            category=[obj.id for obj in Category.objects.all()]
        if not category:
            category=[obj.id for obj in Category.objects.all()]

        products=products.filter(
                brand__id__in=brand,category__id__in=category,seller__id__in=sellers,
                product_type__in=product_type,warranty_period__in=warranty
            )
        
  
        if sorting:
            if sorting=="highest":
                  products=products.order_by("-price")
            elif sorting=="lowest":
                products=products.order_by("price")
            else:
                products=products.order_by("-id")

        data=[]
        for  obj in products:
            data.append({
               "image":obj.image.url,
               "title":obj.title,
               "price":obj.price,
               "discount_price":obj.discount_price,
               "category":obj.category.name,
               'brand':obj.brand.name
            
            })
        if products:count=products.count()
        else: count=0

        return JsonResponse({"data":data,"count":count})
    


