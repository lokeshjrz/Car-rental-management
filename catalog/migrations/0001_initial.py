# Generated by Django 4.0.6 on 2022-07-09 03:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_venc', models.CharField(choices=[('sedan', 'sedan'), ('station wagon', 'station wagon'), ('hatchback', 'hatchback'), ('minivan', 'minivan'), ('crossover', 'crossover'), ('coupe', 'coupe'), ('cabriolet', 'cabriolet'), ('pickup', 'pickup'), ('minibus', 'minibus'), ('truck', 'truck')], max_length=30, verbose_name='Type of venc')),
                ('brand', models.CharField(choices=[('AC', 'AC'), ('Acura', 'Acura'), ('Adler', 'Adler'), ('Alfa Romeo', 'Alfa Romeo'), ('Alpina', 'Alpina'), ('Alpine', 'Alpine'), ('AM General', 'AM General'), ('AMC', 'AMC'), ('Apal', 'Apal'), ('Ariel', 'Ariel'), ('Aro', 'Aro'), ('Asia', 'Asia'), ('Aston Martin', 'Aston Martin'), ('Auburn', 'Auburn'), ('Audi', 'Audi'), ('Aurus', 'Aurus'), ('Austin', 'Austin'), ('Austin Healey', 'Austin Healey'), ('Autobianchi', 'Autobianchi'), ('BAIC', 'BAIC'), ('Bajaj', 'Bajaj'), ('Baltijas Dzips', 'Baltijas Dzips'), ('Batmobile', 'Batmobile'), ('Bentley', 'Bentley'), ('Bertone', 'Bertone'), ('Bilenkin', 'Bilenkin'), ('Bio auto', 'Bio auto'), ('Bitter', 'Bitter'), ('Blaval', 'Blaval'), ('BMW', 'BMW'), ('Borgward', 'Borgward'), ('Brabus', 'Brabus'), ('Brilliance', 'Brilliance'), ('Bristol', 'Bristol'), ('Bufori', 'Bufori'), ('Bugatti', 'Bugatti'), ('Buick', 'Buick'), ('BYD', 'BYD'), ('Byvin', 'Byvin'), ('Cadillac', 'Cadillac'), ('Callaway', 'Callaway'), ('Carbodies', 'Carbodies'), ('Caterham', 'Caterham'), ('Chana', 'Chana'), ('Changan', 'Changan'), ('ChangFeng', 'ChangFeng'), ('Changhe', 'Changhe'), ('Chery', 'Chery'), ('Chevrolet', 'Chevrolet'), ('Chrysler', 'Chrysler'), ('Ciimo (DongFeng-Honda)', 'Ciimo (DongFeng-Honda)'), ('Citroen', 'Citroen'), ('Cizeta', 'Cizeta'), ('Coggiola', 'Coggiola'), ('Cord', 'Cord'), ('Cupra', 'Cupra'), ('Dacia', 'Dacia'), ('Dadi', 'Dadi'), ('Daewoo', 'Daewoo'), ('Daihatsu', 'Daihatsu'), ('Daimler', 'Daimler'), ('Dallara', 'Dallara'), ('Datsun', 'Datsun'), ('De Tomaso', 'De Tomaso'), ('Deco Rides', 'Deco Rides'), ('Delage', 'Delage'), ('DeLorean', 'DeLorean'), ('Derways', 'Derways'), ('DeSoto', 'DeSoto'), ('DKW', 'DKW'), ('Dodge', 'Dodge'), ('DongFeng', 'DongFeng'), ('Doninvest', 'Doninvest'), ('Donkervoort', 'Donkervoort'), ('DS', 'DS'), ('DW Hower', 'DW Hower'), ('E-Car', 'E-Car'), ('Eagle', 'Eagle'), ('Eagle Cars', 'Eagle Cars'), ('Everus', 'Everus'), ('Excalibur', 'Excalibur'), ('EXEED', 'EXEED'), ('Facel Vega', 'Facel Vega'), ('FAW', 'FAW'), ('Ferrari', 'Ferrari'), ('Fiat', 'Fiat'), ('Fisker', 'Fisker'), ('Flanker', 'Flanker'), ('Ford', 'Ford'), ('Foton', 'Foton'), ('FSO', 'FSO'), ('Fuqi', 'Fuqi'), ('GAC', 'GAC'), ('GAC Aion', 'GAC Aion'), ('Geely', 'Geely'), ('Genesis', 'Genesis'), ('Geo', 'Geo'), ('GMC', 'GMC'), ('Goggomobil', 'Goggomobil'), ('Gonow', 'Gonow'), ('Gordon', 'Gordon'), ('GP', 'GP'), ('Great Wall', 'Great Wall'), ('Hafei', 'Hafei'), ('Haima', 'Haima'), ('Hanomag', 'Hanomag'), ('Haval', 'Haval'), ('Hawtai', 'Hawtai'), ('Heinkel', 'Heinkel'), ('Hennessey', 'Hennessey'), ('Hindustan', 'Hindustan'), ('Hispano-Suiza', 'Hispano-Suiza'), ('Holden', 'Holden'), ('Honda', 'Honda'), ('Hongqi', 'Hongqi'), ('Horch', 'Horch'), ('Hozon', 'Hozon'), ('HSV', 'HSV'), ('HuangHai', 'HuangHai'), ('Hudson', 'Hudson'), ('Hummer', 'Hummer'), ('Hyundai', 'Hyundai'), ('Infiniti', 'Infiniti'), ('Innocenti', 'Innocenti'), ('International', 'International'), ('Invicta', 'Invicta'), ('Iran Khodro', 'Iran Khodro'), ('Isdera', 'Isdera'), ('Isuzu', 'Isuzu'), ('IVECO', 'IVECO'), ('JAC', 'JAC'), ('Jaguar', 'Jaguar'), ('Jeep', 'Jeep'), ('Jensen', 'Jensen'), ('Jinbei', 'Jinbei'), ('JMC', 'JMC'), ('Kia', 'Kia'), ('Koenigsegg', 'Koenigsegg'), ('KTM AG', 'KTM AG'), ('LADA (ВАЗ)', 'LADA (ВАЗ)'), ('Lamborghini', 'Lamborghini'), ('Lancia', 'Lancia'), ('Land Rover', 'Land Rover'), ('Landwind', 'Landwind'), ('Leapmotor', 'Leapmotor'), ('Lexus', 'Lexus'), ('Liebao Motor', 'Liebao Motor'), ('Lifan', 'Lifan'), ('Ligier', 'Ligier'), ('Lincoln', 'Lincoln'), ('LiXiang', 'LiXiang'), ('Logem', 'Logem'), ('Lotus', 'Lotus'), ('LTI', 'LTI'), ('Lucid', 'Lucid'), ('Luxgen', 'Luxgen'), ('Mahindra', 'Mahindra'), ('Marcos', 'Marcos'), ('Marlin', 'Marlin'), ('Marussia', 'Marussia'), ('Maruti', 'Maruti'), ('Maserati', 'Maserati'), ('Matra', 'Matra'), ('Maybach', 'Maybach'), ('Mazda', 'Mazda'), ('McLaren', 'McLaren'), ('Mega', 'Mega'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Mercury', 'Mercury'), ('Messerschmitt', 'Messerschmitt'), ('Metrocab', 'Metrocab'), ('MG', 'MG'), ('Microcar', 'Microcar'), ('Minelli', 'Minelli'), ('MINI', 'MINI'), ('Mitsubishi', 'Mitsubishi'), ('Mitsuoka', 'Mitsuoka'), ('Morgan', 'Morgan'), ('Morris', 'Morris'), ('Nash', 'Nash'), ('Nio', 'Nio'), ('Nissan', 'Nissan'), ('Noble', 'Noble'), ('Oldsmobile', 'Oldsmobile'), ('Opel', 'Opel'), ('Osca', 'Osca'), ('Packard', 'Packard'), ('Pagani', 'Pagani'), ('Panoz', 'Panoz'), ('Perodua', 'Perodua'), ('Peugeot', 'Peugeot'), ('PGO', 'PGO'), ('Piaggio', 'Piaggio'), ('Pierce-Arrow', 'Pierce-Arrow'), ('Plymouth', 'Plymouth'), ('Polestar', 'Polestar'), ('Pontiac', 'Pontiac'), ('Porsche', 'Porsche'), ('Premier', 'Premier'), ('Proton', 'Proton'), ('PUCH', 'PUCH'), ('Puma', 'Puma'), ('Qoros', 'Qoros'), ('Qvale', 'Qvale'), ('RAM', 'RAM'), ('Ravon', 'Ravon'), ('Reliant', 'Reliant'), ('Renaissance', 'Renaissance'), ('Renault', 'Renault'), ('Renault Samsung', 'Renault Samsung'), ('Rezvani', 'Rezvani'), ('Rimac', 'Rimac'), ('Rinspeed', 'Rinspeed'), ('Rivian', 'Rivian'), ('Roewe', 'Roewe'), ('Rolls-Royce', 'Rolls-Royce'), ('Ronart', 'Ronart'), ('Rover', 'Rover'), ('Saab', 'Saab'), ('Saipa', 'Saipa'), ('Saleen', 'Saleen'), ('Santana', 'Santana'), ('Saturn', 'Saturn'), ('Scion', 'Scion'), ('Sears', 'Sears'), ('SEAT', 'SEAT'), ('Shanghai Maple', 'Shanghai Maple'), ('ShuangHuan', 'ShuangHuan'), ('Simca', 'Simca'), ('Skoda', 'Skoda'), ('Skywell', 'Skywell'), ('Smart', 'Smart'), ('Soueast', 'Soueast'), ('Spectre', 'Spectre'), ('Spyker', 'Spyker'), ('SsangYong', 'SsangYong'), ('Steyr', 'Steyr'), ('Studebaker', 'Studebaker'), ('Subaru', 'Subaru'), ('Suzuki', 'Suzuki'), ('Talbot', 'Talbot'), ('TATA', 'TATA'), ('Tatra', 'Tatra'), ('Tazzari', 'Tazzari'), ('Tesla', 'Tesla'), ('Think', 'Think'), ('Tianma', 'Tianma'), ('Tianye', 'Tianye'), ('Tofas', 'Tofas'), ('Toyota', 'Toyota'), ('Trabant', 'Trabant'), ('Tramontana', 'Tramontana'), ('Triumph', 'Triumph'), ('TVR', 'TVR'), ('Ultima', 'Ultima'), ('Vauxhall', 'Vauxhall'), ('Vector', 'Vector'), ('Venturi', 'Venturi'), ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo'), ('Vortex', 'Vortex'), ('Voyah', 'Voyah'), ('VUHL', 'VUHL'), ('W Motors', 'W Motors'), ('Wanderer', 'Wanderer'), ('Wartburg', 'Wartburg'), ('Weltmeister', 'Weltmeister'), ('Westfield', 'Westfield'), ('Wiesmann', 'Wiesmann'), ('Willys', 'Willys'), ('Xin Kai', 'Xin Kai'), ('Xpeng', 'Xpeng'), ('Yulon', 'Yulon'), ('Zastava', 'Zastava'), ('Zeekr', 'Zeekr'), ('Zenos', 'Zenos'), ('Zenvo', 'Zenvo'), ('Zibar', 'Zibar'), ('Zotye', 'Zotye'), ('ZX', 'ZX'), ('Автокам', 'Автокам'), ('ГАЗ', 'ГАЗ'), ('ЗАЗ', 'ЗАЗ'), ('ЗИЛ', 'ЗИЛ'), ('ЗиС', 'ЗиС'), ('ИЖ', 'ИЖ'), ('Канонир', 'Канонир'), ('Комбат', 'Комбат'), ('ЛуАЗ', 'ЛуАЗ'), ('Москвич', 'Москвич'), ('СМЗ', 'СМЗ'), ('Спортивные авто и Реплики', 'Спортивные авто и Реплики'), ('ТагАЗ', 'ТагАЗ'), ('УАЗ', 'УАЗ'), ('Ё-мобиль', 'Ё-мобиль')], max_length=150, verbose_name='Brand')),
                ('model', models.CharField(max_length=150, verbose_name='Model')),
                ('fuel', models.CharField(choices=[('petrol', 'petrol'), ('diesel', 'diesel'), ('hybrid', 'hybrid'), ('electric', 'electric')], max_length=30, verbose_name='Type of fuel')),
                ('engine_volume', models.DecimalField(blank=True, decimal_places=1, max_digits=2)),
                ('transmission', models.CharField(choices=[('manual', 'manual'), ('automatic', 'automatic')], max_length=30, verbose_name='Transmission')),
                ('year', models.IntegerField(verbose_name='Year of car manufacture')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('price_currency', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('BYN', 'BYN'), ('RUB', 'RUB')], max_length=30, verbose_name='Currency')),
                ('mileage', models.IntegerField(verbose_name='Mileage')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo_1', models.ImageField(upload_to='media/photo/%Y/%m/%d/', verbose_name='Photo')),
                ('photo_2', models.ImageField(blank=True, upload_to='media/photo/%Y/%m/%d/', verbose_name='Photo')),
                ('photo_3', models.ImageField(blank=True, upload_to='media/photo/%Y/%m/%d/', verbose_name='Photo')),
                ('photo_4', models.ImageField(blank=True, upload_to='media/photo/%Y/%m/%d/', verbose_name='Photo')),
                ('photo_5', models.ImageField(blank=True, upload_to='media/photo/%Y/%m/%d/', verbose_name='Photo')),
                ('photo_6', models.ImageField(blank=True, upload_to='media/photo/%Y/%m/%d/', verbose_name='Photo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('views', models.IntegerField(default=0, verbose_name='Views')),
                ('seller', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]