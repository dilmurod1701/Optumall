import json
from django.contrib.auth.models import AnonymousUser, User
from rest_framework.authtoken.admin import User
from selenium import webdriver
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from api.models import Users, Products, Profile, Cart


# Test for Model

class OptumallTest(TestCase):
    def setUp(self) -> None:
        Users.objects.create(first_name='John', last_name='Wick', email='johnwick@gmail.com', password='john1234')
        Users.objects.create(first_name='James', last_name='Barry', email='barry01@gmail.com', password='barry1234')
        Users.objects.create(first_name='Romario', last_name='Enderson', email='romario@gmail.com',
                             password='romario1234')
        Users.objects.create(first_name='Diego', last_name='Costa', email='costarico@gmail.com', password='diego1234')
        Users.objects.create(first_name='Alice', last_name='Amber', email='alice@gmail.com', password='alice1234')

        Products.objects.create(title='Iphone13Pro', price=899, photos='',
                                description='Iphone 13 Pro New Ideal Version', availability=True, category='cars',
                                size='M', color='Black')
        Products.objects.create(title='Iphone14Pro', price=1000, photos='',
                                description='Iphone 14 Pro New Ideal Version', availability=True, category='cars',
                                size='M', color='Black')
        Products.objects.create(title='Iphone15Pro', price=1599, photos='',
                                description='Iphone 15 Pro New Ideal Version', availability=True, category='cars',
                                size='M', color='Black')
        Products.objects.create(title='Iphone15ProMax', price=1799, photos='',
                                description='Iphone 15 Pro Max New Ideal Version', availability=True, category='cars',
                                size='M', color='Black')
        Products.objects.create(title='Iphone13ProMax', price=969, photos='',
                                description='Iphone 13 Pro Max New Ideal Version', availability=True, category='cars',
                                size='M', color='Black')

        Profile.objects.create(phone_number=123456, profile_img='', who='customer', telegram_username='@john')
        Profile.objects.create(phone_number=111111, profile_img='', who='deliver', telegram_username='@mrbean')
        Profile.objects.create(phone_number=222222, profile_img='', who='customer', telegram_username='@messi')
        Profile.objects.create(phone_number=555555, profile_img='', who='deliver', telegram_username='@abs')
        Profile.objects.create(phone_number=777777, profile_img='', who='customer', telegram_username='@aaa')

        Cart.objects.create(products='Iphone13Pro')
        Cart.objects.create(products='Iphone15ProMax')
        Cart.objects.create(products='Iphone15Pro')
        Cart.objects.create(products='Iphone13ProMax')
        Cart.objects.create(products='Iphone14Pro')

    def test_models_users(self):
        var1 = Users.objects.get(first_name='John').first_name
        var2 = Users.objects.get(last_name='Wick').last_name
        var3 = Users.objects.get(email='johnwick@gmail.com').email
        var4 = Users.objects.get(password='john1234').password

        var5 = Users.objects.get(first_name='James').first_name
        var6 = Users.objects.get(last_name='Barry').last_name
        var7 = Users.objects.get(email='barry01@gmail.com').email
        var8 = Users.objects.get(password='barry1234').password

        var9 = Users.objects.get(first_name='Romario').first_name
        var10 = Users.objects.get(last_name='Enderson').last_name
        var11 = Users.objects.get(email='romario@gmail.com').email
        var12 = Users.objects.get(password='romario1234').password

        var13 = Users.objects.get(first_name='Diego').first_name
        var14 = Users.objects.get(last_name='Costa').last_name
        var15 = Users.objects.get(email='costarico@gmail.com').email
        var16 = Users.objects.get(password='diego1234').password

        var17 = Users.objects.get(first_name='Alice').first_name
        var18 = Users.objects.get(last_name='Amber').last_name
        var19 = Users.objects.get(email='alice@gmail.com').email
        var20 = Users.objects.get(password='alice1234').password

        self.assertEqual(var1, 'John')
        self.assertEqual(var2, 'Wick')
        self.assertEqual(var3, 'johnwick@gmail.com')
        self.assertEqual(var4, 'john1234')

        self.assertEqual(var5, 'James')
        self.assertEqual(var6, 'Barry')
        self.assertEqual(var7, 'barry01@gmail.com')
        self.assertEqual(var8, 'barry1234')

        self.assertEqual(var9, 'Romario')
        self.assertEqual(var10, 'Enderson')
        self.assertEqual(var11, 'romario@gmail.com')
        self.assertEqual(var12, 'romario1234')

        self.assertEqual(var13, 'Diego')
        self.assertEqual(var14, 'Costa')
        self.assertEqual(var15, 'costarico@gmail.com')
        self.assertEqual(var16, 'diego1234')

        self.assertEqual(var17, 'Alice')
        self.assertEqual(var18, 'Amber')
        self.assertEqual(var19, 'alice@gmail.com')
        self.assertEqual(var20, 'alice1234')

    def test_models_products(self):
        obj1 = Products.objects.get(title='Iphone13Pro').title
        obj2 = Products.objects.get(price=899).price
        obj3 = Products.objects.get(description='Iphone 13 Pro New Ideal Version').description

        obj4 = Products.objects.get(title='Iphone14Pro').title
        obj5 = Products.objects.get(price=1000).price
        obj6 = Products.objects.get(description='Iphone 14 Pro New Ideal Version').description

        obj7 = Products.objects.get(title='Iphone15Pro').title
        obj8 = Products.objects.get(price=1599).price
        obj9 = Products.objects.get(description='Iphone 15 Pro New Ideal Version').description

        obj10 = Products.objects.get(title='Iphone15ProMax').title
        obj11 = Products.objects.get(price=1799).price
        obj12 = Products.objects.get(description='Iphone 15 Pro Max New Ideal Version').description

        obj13 = Products.objects.get(title='Iphone13ProMax').title
        obj14 = Products.objects.get(price=969).price
        obj15 = Products.objects.get(description='Iphone 13 Pro Max New Ideal Version').description

        self.assertEqual(obj1, 'Iphone13Pro')
        self.assertEqual(obj2, 899)
        self.assertEqual(obj3, 'Iphone 13 Pro New Ideal Version')

        self.assertEqual(obj4, 'Iphone14Pro')
        self.assertEqual(obj5, 1000)
        self.assertEqual(obj6, 'Iphone 14 Pro New Ideal Version')

        self.assertEqual(obj7, 'Iphone15Pro')
        self.assertEqual(obj8, 1599)
        self.assertEqual(obj9, 'Iphone 15 Pro New Ideal Version')

        self.assertEqual(obj10, 'Iphone15ProMax')
        self.assertEqual(obj11, 1799)
        self.assertEqual(obj12, 'Iphone 15 Pro Max New Ideal Version')

        self.assertEqual(obj13, 'Iphone13ProMax')
        self.assertEqual(obj14, 969)
        self.assertEqual(obj15, 'Iphone 13 Pro Max New Ideal Version')


class OptumallViewTest(TestCase):

    def test_status_code(self):
        response1 = self.client.get('/api/products')
        self.assertEqual(response1.status_code, 200)

        response2 = self.client.post('/api/products')
        self.assertEqual(response2.status_code, 405)

        response3 = self.client.get('/api/')
        self.assertEqual(response3.status_code, 404)

        response4 = self.client.get('/api/new')
        self.assertEqual(response4.status_code, 403)

    def test_api_new(self):
        user = User.objects.create_superuser(username='tester', email='sarvaromon33@gmail.com',
                                                  password='qwErt1928', is_superuser=True, is_staff=True)
        user.save()
        factory = APIRequestFactory()
        request = factory.post('/notes/', json.dumps({
            "title": "Rolls Royce Ghost",
            "price": 120000,
            "photos": '',
            "description": "Rolls Royce New Ghost version",
            "availability": True,
            "category": 'cars',
            "size": 'M',
            "color": 'Black'
        }), content_type='application/json')

        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/api/new')
