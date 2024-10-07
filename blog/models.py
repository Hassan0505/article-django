from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_price_locked = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def lock_price(self):
        if self.is_price_locked:
            raise ValueError("Price is already locked")
        self.is_price_locked = True
        self.save()
  

    def unlock_price(self):
        if not self.is_price_locked:
            raise ValueError("Price is already unlocked")
        self.is_price_locked = False
        self.save()

class Payment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    