from django.db import models

# Create your models here.
class Boards(models.Model):
    title=models.CharField(max_length=10)
    content = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    #auto_now_add 해당 데이터가 생성을 할 때 자동으로 시간을 만들어줌.
    updated_at = models.DateTimeField(auto_now=True)
    #auto_now 해당 데이터가 수정을 할 때 자동으로 시간을 만들어줌.

    def __str__(self):
        return f'{self.id} : {self.title}'
    #make 마이크래이션을 해줄 필요가 없다. 왜냐하면 ㅅ

class Subway(models.Model):
    name=models.CharField(max_length=10)
    date=models.DateTimeField(auto_now_add=True)
    sandwitch = models.CharField(max_length=30)
    size = models.IntegerField()
    bread = models.CharField(max_length=30)
    source = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} : {self.date} : {self.sandwitch} : {self.size} : {self.bread} : {self.source}'
