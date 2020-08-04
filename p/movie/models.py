from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField('Katigoriyasi', max_length=150)
    description = models.TextField('opisaniyasi')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Katigoriya'
        verbose_name_plural = 'Katigoriyalar'

class Actor(models.Model):
    name = models.CharField('ismi', max_length=100)
    age = models.PositiveSmallIntegerField('Yoshi', default=0)
    description = models.TextField('opisaniyasi')
    image = models.ImageField(upload_to='actors/', height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Akter va Rejisor'
        verbose_name_plural = 'Akterlar va Rejisorlar'

class Genre(models.Model):
    name = models.CharField('Nomi', max_length=100)
    description = models.TextField('opisaniyasi')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Janr'
        verbose_name_plural = 'Janrlar'

class Movie(models.Model):
    title = models.CharField('Nomi', max_length=100)
    tagline = models.CharField('Slogan', max_length=100, default='' )
    description = models.TextField('Opisaniyasi')
    poster = models.ImageField('Poster', upload_to='movies/')
    years = models.PositiveSmallIntegerField('Chiqgan sanasi', default=2020)
    country = models.CharField('Mamlakat', max_length=50)
    directors = models.ManyToManyField(Actor, verbose_name='rejisor', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='Akter', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='janr')
    world_premiere = models.DateField('Dunyo premyerasi', default=date.today)
    budget = models.PositiveIntegerField('Byujet', default=0, help_text='narxini dollarda korsating')
    fees_in_usa = models.PositiveIntegerField('AQSHda yigilgan puli', default=0, help_text='narxini dollarda korsating')
    fees_in_world = models.PositiveIntegerField('Dunyoda yigilgan puli', default=0, help_text='narxini dollarda korsating')
    category = models.ForeignKey(Category, verbose_name='Kategoriya', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField('Chernovik', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('moviesingle', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmlar'

class MovieShots(models.Model):
    title = models.CharField('Sarlavha', max_length=100)
    description = models.TextField('Qisqacha malumot')
    image = models.ImageField(upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Filmdan kadr"
        verbose_name_plural = "Filmdan kadrlar"

class RatingStar(models.Model):
    value = models.SmallIntegerField('Manosi', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Yulduz reytingi'
        verbose_name_plural = 'Yulduzlar reytingi'

class Rating(models.Model):
    name = models.CharField('Nomi', max_length=15)
    ip = models.CharField('Ip adress', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="yulduz")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Film')

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = 'Reyting'
        verbose_name_plural = 'Reytinglar'

class Reviews(models.Model):
    email = models.EmailField('Emaili')
    name = models.CharField('Nomi', max_length=100)
    text = models.TextField('Xabar', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Ota-ona', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='Film', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = 'Sharh'
        verbose_name_plural = 'Sharhlar'

