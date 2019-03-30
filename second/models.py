from django.db import models

# Create your models here.
from django.urls import reverse


class Name(models.Model):
    Name = models.CharField(max_length=222, help_text='Enter your book name ....')

    def __str__(self):
        return self.Name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    lest_name = models.CharField(max_length=30)
    adderss = models.CharField(max_length=330)
    date_birth = models.DateField(auto_now=False)
    death_birth=models.CharField(max_length=25,default='more n',help_text='yeare-menth-day')

    def __str__(self):
        return '%s  %s' % (self.first_name, self.lest_name)
    def revers_author_url(self):
        return reverse('author_details',args=[str(self.id)])


class Book(models.Model):
    title = models.CharField(max_length=121)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    #edition=models.CharField(max_length=55, help_text='1st publish jun-09-2020')
    summary=models.TextField(max_length=1000,help_text='Enter briet deseription of The Book')
    pub_name=models.ManyToManyField(Name,help_text='Select a Book')
    publisher=models.CharField(max_length=111)

    def __str__(self):
        return self.title
    def summarys(self):
        return self.summary[0:150]+'... ... ...'

    def revers_author_url(self):
        return reverse('book_details',args=[str(self.id)])