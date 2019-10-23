from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Name', max_length=150, unique=True)
    description = models.TextField('Description')
    status = models.BooleanField('State', default=True)
    class Meta:
        verbose_category = 'Category'
        verbose_category_plural = 'Categories'
    
    def __str__(self):
        return self.title

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Name', max_length=150, unique=True)
    abbreviation = models.TextField('Abbreviation')
    status = models.BooleanField('State', default=True)
    class Meta:
        verbose_Country = 'Country'
        verbose_Countries_plural = 'Countries'
    
    def __str__(self):
        return self.abbreviation

class Product(Category,Country):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Name', max_length=150, unique=True)
    description = models.TextField('Description')
    photo = models.ImageField('Image', upload_to= 'images/',max_length=200)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantity', max_length=10)
    status = models.BooleanField('State', default=True)
    class Meta:
        verbose_product = 'Product'
        verbose_products_plural = 'Products'
    
    def __str__(self):
        return self.title

class Gender(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Name', max_length=150, unique=True)
    description = models.TextField('Description')
    status = models.BooleanField('State', default=True)
    class Meta:
        verbose_gender = 'Gender'
        verbose_gender_plural = 'Genders'
    
    def __str__(self):
        return self.title

class Client(Gender,Country):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField('First Name', max_length=150)
    lastname = models.CharField('LastName', max_length=150)
    id_gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    phone = models.CharField('Phone', max_length=10)
    email = models.EmailField('E-mail', max_length=200)
    password = models.CharField('First Name', max_length=50)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    photo = models.ImageField('Image', upload_to= 'images/',max_length=200)
    credit_card_number = models.CharField('Phone', max_length=20)
    status = models.BooleanField('State', default=True)
    class Meta:
        verbose_Client = 'Client'
        verbose_Clients_plural = 'Clients'
    
    def __str__(self):
        return self.'{0}{1}{2}'.format(self.lastname, ", ", self.firstname)

class shopping(Product,Client):
    id = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    shopping_date = models.DateField('Shopping date', auto_now=False, auto_now_add=True)
    class Meta:
        abstract = True