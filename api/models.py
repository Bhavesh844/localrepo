from django.db import models

# Create your models here.
class company(models.Model):
    c_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    about=models.TextField(max_length=50)
    type=models.CharField(max_length=50,choices=(('IT','IT'),('Non IT','Non IT'),('Mobiles','Mobiles')))
    added_date=models.DateField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name 

class employee(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    about=models.CharField(max_length=30)
    position=models.CharField(max_length=50,choices=
                              (
                                  ('Manager','manager',),
                                  ('Software developer','sd'),
                                  ('Project Leader','pl')
                              ))
    cp=models.ForeignKey(company,on_delete=models.CASCADE)
    