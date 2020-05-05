from django.db import models


class ProductGroup(models.Model):
    label = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('label',)
        verbose_name = 'product_group'

    def __str__(self):
        return self.label


class Product(models.Model):
    product_group = models.ForeignKey(ProductGroup, related_name='products', on_delete=models.CASCADE)
    label = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    accessible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('label',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.label
