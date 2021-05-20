from django.db import models

# Create your models here.
class dogbreed(models.Model): #견종
    dogbreed = models.CharField(max_length=100,primary_key=True)

class member(models.Model): #회원관리
    id = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    home = models.TextField()
    cellphone = models.CharField(max_length=50)

class mydog(models.Model):
    member_id = models.ForeignKey(member,on_delete=models.CASCADE)
    dogbreed = models.ForeignKey(dogbreed,on_delete=models.CASCADE)
    dogimage = models.ImageField(blank=True, upload_to="photo_%Y_%m_%d")
    dogname = models.CharField(max_length=50)
    dogage = models.IntegerField()
    dogsex = models.CharField(max_length=50)

class missingdog(models.Model): #유기견리스트
    member_id = models.ForeignKey(member, on_delete=models.CASCADE)
    dogbreed = models.ForeignKey(dogbreed,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    findplace = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
    cellphone = models.IntegerField()
    explanation = models.TextField()
    img = models.ImageField(blank=True, upload_to="photo_%Y_%m_%d")
    findtime = models.DateTimeField()

class dogcenter(models.Model) : #동물보호센터 현황
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    cellphone= models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()