from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
# Create your models here. 
#Model fields---properties and desc of car which we are selling

'''
car_title
city
state
color
model
year 
condition
price
description
car_photo
car_photo_1
car_photo_2
car_photo_3
car_photo_4
features
body_style
engine
transmission
interior
miles
doors
passengers
vin_no  #vehicle engine no
mileage
fuel_type
no_of_owners 
is_featured
created_date
'''
class Car(models.Model):
    state_choice=(
         ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    
    )
    features_choices = (
        ('Cruise Control', 'Круиз-контроль'),
        ('Audio Interface', 'Мультимедия'),
        ('Airbags', 'Подушки безопасности'),
        ('Air Conditioning', 'Кондиционер'),
        ('Seat Heating', 'Подогрев сидений'),
        ('Alarm System', 'Сигнализация'),
        ('ParkAssist', 'Система помощи парковки'),
        ('Power Steering', 'Усилитель руля'),
        ('Reversing Camera', 'Камера заднего вида'),
        ('Direct Fuel Injection', 'Турбина'),
        ('Auto Start/Stop', 'Функция авто\стоп'),
        ('Wind Deflector', 'Дефлекторы'),
        ('Bluetooth Handset', 'Мультируль'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    year_choice=[]
    for r in range(2000,(datetime.now().year +1)):
         year_choice.append((r,r))

    car_title = models.CharField('Бренд', max_length=255)
    # state=models.CharField(choices=state_choice,max_length=255)
    # city=models.CharField(max_length=255)
    color=models.CharField('Цвет', max_length=255)
    model=models.CharField('Модель',max_length=255)
    year =models.IntegerField(('Год'),choices=year_choice)
    condition=models.CharField('Состояние',max_length=255)
    price=models.IntegerField('Цена')
    description=RichTextField('Описание')
    car_photo=models.ImageField('Фотография', upload_to='photos/%Y/%m/%d/')
    car_photo_1=models.ImageField('Фотография',upload_to='photos/%Y/%m/%d/',blank=True)
    car_photo_2 = models.ImageField('Фотография',upload_to='photos/%Y/%m/%d/',blank=True)
    car_photo_3 =models.ImageField('Фотография',upload_to='photos/%Y/%m/%d/',blank=True)
    car_photo_4 =models.ImageField('Фотография',upload_to='photos/%Y/%m/%d/',blank=True)
    features=MultiSelectField('Комплектация',choices=features_choices)
    body_style=models.CharField('Тип кузова',max_length=255)
    engine=models.CharField('Объем двигателя',max_length=255)
    transmission=models.CharField('Тип коробки передачь', max_length=255)
    interior=models.CharField('Цвет интерьера',max_length=255)
    miles=models.IntegerField('Пробег')
    doors=models.CharField('Количество дверей',choices=door_choices,max_length=10)
    passengers=models.IntegerField('Количество мест')
    vin_no=models.CharField('Vin №',max_length=255)
    #mileage=models.IntegerField()
    fuel_type=models.CharField('Тип топлива',max_length=50)
    no_of_owners=models.CharField('количество владельцев', max_length=255)
    is_featured=models.BooleanField('Рекомендован', default=False)
    created_date=models.DateTimeField('Дата создания', default=datetime.now,blank=True)



    def __str__(self):
        return self.car_title

