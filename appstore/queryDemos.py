from appstore.models import *


customers = Customer.objects.all()

firstCustomer = Customer.objects.first()

lastCustomer = Customer.objects.last()

customerbyName = Customer.objects.get(name = 'Charles Chua')

customerById = Customer.objects.get(id=4)

firstCustomer.order_set.all()

Order = Order.objects.first()
parentName = Order.customer.name

products = Product.objects.fitler(category = "Out Door")

leasttoGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

productsFiltered = Product.objects.filter(tags_name = 'Office Supplies')

class ParentModel(models.Model):
    name = models.CharField(max_legnth=200 , null = True)

class ChildModel(models.Model):
    name = models.CharField(max_length = 200, null=True)
    parent = models.ForeignKey(ParentModel)
    
parent = ParentModel.objects.first()
parent.childmodel_set.all()