from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class Pokemon (models.Model):
    TYPE_CHOICES = [ ('w', 'water'), 
                    ('f', 'fire'), 
                    ('w', 'wind'),
                    ('l', 'light'), 
                    ('d', 'darkness'), 
                    ('ln', 'lightning'), 
                    ('r', 'rock'), 
                    ('n', 'nature')]
    
    name = models.CharField(max_length=50, unique=True),
    description = models.TextField, 
    avatar = models.ImageField(upload_to='/pokemons', default='avatar default.jpg'),
    background = models.ImageField(upload_to='/pokemons', default='bg default.png'),
    
    health = models.IntegerField(validators=[MinValueValidator(100)]),
    attack = models.IntegerField(validators=[MinValueValidator(10)]),
    defense = models.IntegerField(validators=[MinValueValidator(5)]),
    speed = models.IntegerField(validators=[MinValueValidator(15)])
    
        
    