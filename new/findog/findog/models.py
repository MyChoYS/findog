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
    delete = models.BooleanField(default=False)#탈퇴여부
    #탈퇴이유

class mydog(models.Model): #나의개
    member_id = models.ForeignKey(member,on_delete=models.CASCADE)
    dogbreed = models.ForeignKey(dogbreed,on_delete=models.CASCADE)
    dogimage = models.ImageField(blank=True, upload_to="photo_%Y_%m_%d")
    dogname = models.CharField(max_length=50)
    dogage = models.IntegerField()
    dogsex = models.CharField(max_length=50)
    delete = models.BooleanField(default=False)   #삭제여부

class missingdog(models.Model): #유기견리스트
    member_id = models.ForeignKey(member, on_delete=models.CASCADE)
    dogbreed = models.ForeignKey(dogbreed,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    findplace = models.TextField()
    cellphone = models.CharField(max_length=50)
    explanation = models.TextField()
    img = models.ImageField(blank=True, upload_to="photo_%Y_%m_%d")
    findtime = models.CharField(max_length=50)
    delete = models.BooleanField(default=False)#삭제여부


class dogcenter(models.Model) : #동물보호센터 현황
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    cellphone= models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()

#이미지 업로드 테스트용
class UploadModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to="photo_%Y_%m_%d") #폴더 생성만, 이미지명은 따로 찾아야함

class findingdog(models.Model): #실종신고
    member_id = models.ForeignKey(member, on_delete=models.CASCADE)
    dogbreed = models.ForeignKey(dogbreed,on_delete=models.CASCADE)
    lostplace = models.CharField(max_length=100)
    losttime = models.CharField(max_length=100)
    title = models.CharField(max_length=20)
    explanation = models.TextField()
    cellphone =  models.CharField(max_length=20)
    img = models.ImageField(blank=True, upload_to="photo_%Y_%m_%d")
    delete = models.BooleanField(default=False)#삭제여부
