from django.db import models

# Create your models here.
class Base(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Base):

    Category_Status = [(0, "Active"), (1, "InActive")]

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for category')
    description = models.TextField()
    meta_description = models.CharField("Meta Description", max_length=500, help_text='Content description')
    meta_keywpords = models.CharField("Meta Keywords", max_length=500, help_text='Content Keywords')
    category_status = models.IntegerField(choices=Category_Status, default=0)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_date']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed('catalogueapp:catalogue', arg=[self.slug])


class Brand(Base):

    Brand_Status = [(0, "Active"), (1, "InActive")]

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for category')
    description = models.TextField()
    meta_description = models.CharField("Meta Description", max_length=500, help_text='Content description')
    meta_keywpords = models.CharField("Meta Keywords", max_length=500, help_text='Content Keywords')
    brand_status = models.IntegerField(choices=Brand_Status, default=0)

    class Meta:
        db_table = 'brands'
        ordering = ['-created_date']
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed('productcatalog:product_catalog', arg=[self.slug])


class Product(Base):
    Product_Status = [(0, "Active"), (1, "InActive")]

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=500, unique=True, help_text='Unique value')
    description = models.TextField()
    meta_description = models.CharField("Meta Description", max_length=500, help_text='Content description')
    meta_keywpords = models.CharField("Meta Keywords", max_length=500, help_text='Content Keywords')
    sku = models.CharField(max_length=100)
    model = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0.00)
    image_url = models.CharField(max_length=250)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    brands = models.ManyToManyField(Brand)
    product_status = models.IntegerField(choices=Product_Status)

    class Meta:
        db_table = 'products'
        ordering = ['created_date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=['self.slug'])

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None