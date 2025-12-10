from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import PositiveSmallIntegerField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator,MaxValueValidator


StatusChoices = (
        ('pro','pro'),
        ('simple','simple'))

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True,blank=True)
    age = PositiveSmallIntegerField(validators=[MinValueValidator(10),MaxValueValidator(80)],
                                    null=True,blank=True)
    profile_image = models.ImageField(upload_to='user_images',null=True,blank=True)
    status = models.CharField(max_length=20,choices=StatusChoices,default='simple')
    data_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name},{self.last_name}'

class Category(models.Model):
    category_name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.category_name

class Genre(models.Model):
    genre_name = models.CharField(max_length=30)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.genre_name

class Country(models.Model):
    country_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.country_name

class Director(models.Model):
    director_photo = models.ImageField(upload_to='director_images')
    full_name = models.CharField(max_length=150)
    bio = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return self.full_name

class Actor(models.Model):
    full_name = models.CharField(max_length=150)
    bio = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return self.full_name

class ActorImage(models.Model):
    actor = models.ForeignKey(Actor,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='actor_images/')

class Movie(models.Model):
    movie_name = models.CharField(max_length=150)
    slogan = models.CharField(max_length=200,verbose_name='Слоган')
    year = models.DateField()
    country = models.ManyToManyField(Country)
    director = models.ManyToManyField(Director)
    genre = models.ManyToManyField(Genre)
    MovieTypeChoices = (
        ('360p','360p'),
        ('480p','480p'),
        ('720p','720p'),
        ('1080p','1080p'),
        ('1080p Ultra','1080p Ultra'))
    movie_type = models.CharField(max_length=30,choices=MovieTypeChoices)
    movie_time = models.PositiveSmallIntegerField()
    actor = models.ManyToManyField(Actor)
    description = models.TextField()
    movie_status = models.CharField(max_length=30)

    def __str__(self):
        return self.movie_name

class MovieVideo(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    video_name = models.CharField(max_length=40)
    video = models.FileField(upload_to='movie_videos')

    def __str__(self):
        return f'{self.movie},{self.video_name}'





