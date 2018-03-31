from django.db import models

# Create your models here.
class Address(models.Model):
    pass

class Person(models.Model):
    name=models.CharField(max_length=100)

class Location(models.Model):
    name=models.CharField(max_length=100)
class Cargo(models.Model):
    name=models.CharField(max_length=100)
class Route(models.Model):
    pass

class BusinessPartner(models.Model):
    name=models.CharField(max_length=100)
    short_name=models.CharField(max_length=10)
    legal_name=models.CharField(max_length=100)
    external_id=models.CharField(max_length=50)
    status=(
    ('CR', 'Created'),
    ('RG', 'Registered'),
    ('LK', 'Locked'),
    ('DL', 'Marked For Deletion'),
    )
    addresses=models.ManyToManyField(Address)
    admin=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='admin')
    contacts=models.ManyToManyField(Person,related_name='contacts')
class Order(models.Model):
    create_date=models.DateTimeField()
    status=(
    ('CR', 'Created'),
    ('RE', 'Released'),
    ('EX', 'In Execution'),
    ('CM', 'Completed'),
    )
    reference_number=models.CharField(max_length=100)
    mode=(
    ('RD', 'Road'),
    ('AR', 'Air'),
    ('OC', 'Ocean'),
    )
    shipping_type=(
    ('LTL', 'Less Than Truck Load'),
    ('FTL', 'Full Truck Load'),
    )
    priority=(
    ('1', 'Very High'),
    ('2', 'High'),
    )
    gross_weight=models.DecimalField(max_digits=10, decimal_places=2)
    gross_weight_uom=(
    ('KG', 'KG'),
    ('TN', 'TON'),
    )
    gross_volume=models.DecimalField(max_digits=10, decimal_places=2)
    gross_volume_uom=(
    ('M3', 'M3'),
    ('L', 'L'),
    )
    comments=models.TextField()
    reference_contract=models.CharField(max_length=50)
    businesspartner=models.ManyToManyField(BusinessPartner,through='Order_BusinessPartner')
    source_location=models.ForeignKey(Location,on_delete=models.CASCADE,related_name='source_location')
    destination_location=models.ForeignKey(Location,on_delete=models.CASCADE,related_name='destination_location')
    cargos=models.ManyToManyField(Cargo)

class Order_BusinessPartner(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    business_partner = models.ForeignKey(BusinessPartner, on_delete=models.CASCADE)
    party_role=(
        ('ORD','Ordering Party'),
        ('SHP','Shipper'),
        ('CON','Consignee'),
        ('3PL','3rd Party Logistics'),
        ('CR','Carrier'),
    )
   