from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=90)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.first_name


class Products(models.Model):
    choices = (
        ('oyoq-kiyimlar', 'oyoq-kiyimlar'),
        ('futbolka', 'futbolka'),
        ('cars', 'cars'),
    )
    size_choice = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )
    choose_color = (
        ('Pink', 'Pink'),
        ('Crimson', 'Crimson'),
        ('Brown', 'Brown'),
        ('Salmon', 'Salomon'),
        ('Orange', 'Orange'),
        ('Gold', 'Gold'),
        ('Yellow', 'Yellow'),
        ('Olive', 'Olive'),
        ('Lime', 'Lime'),
        ('Green', 'Green'),
        ('Blue', 'Blue'),
        ('Purple', 'Purple'),
        ('White', 'White'),
        ('Silver', 'Silver'),
        ('Gray', 'Gray'),
        ('Black', 'Black')
    )
    title = models.CharField(max_length=60)
    price = models.BigIntegerField()
    photos = models.ImageField(upload_to='photos')
    description = models.CharField(max_length=200)
    availability = models.BooleanField()
    category = models.CharField(max_length=50, choices=choices)
    size = models.CharField(max_length=40, choices=size_choice)
    color = models.CharField(max_length=40, choices=choose_color)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.title


class Profile(models.Model):
    identity = (
        ('customer', 'customer'),
        ('deliver', 'deliver')
    )
    phone_number = models.BigIntegerField()
    profile_img = models.ImageField(upload_to='profile_images')
    who = models.CharField(max_length=40, choices=identity)
    telegram_username = models.CharField(max_length=90)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.who


class Cart(models.Model):
    from_user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    products = models.CharField(max_length=90)

    class Meta:
        db_table = 'cart'

    def __str__(self):
        return self.from_user
