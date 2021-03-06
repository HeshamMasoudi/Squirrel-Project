# Generated by Django 2.2.7 on 2019-12-10 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=13, default='0', help_text='Longitude Location', max_digits=15)),
                ('latitude', models.DecimalField(decimal_places=13, default='0', help_text='Latitude Location', max_digits=15)),
                ('unique_squirrel_id', models.CharField(blank=True, help_text='Squirrel ID', max_length=100)),
                ('hectare', models.CharField(blank=True, help_text='Hectare', max_length=100)),
                ('shift', models.CharField(choices=[('pm', 'PM'), ('am', 'AM'), ('', '')], default='', help_text='Squirrels Shift', max_length=2)),
                ('date', models.DateField(default='2000-01-01', help_text='Date of sighting')),
                ('hectare_squirrel_number', models.IntegerField(default='0', help_text='Number of the sighting session')),
                ('age', models.CharField(blank=True, choices=[('adult', 'Adult'), ('juvenile', 'Juvenile')], help_text='Age of squirrel', max_length=10)),
                ('primary_fur_color', models.CharField(blank=True, choices=[('cinnamon', 'Cinnamon'), ('white', 'White'), ('balck', 'Black')], help_text='Primary fur color', max_length=20)),
                ('location', models.CharField(blank=True, choices=[('above ground', 'Above Ground'), ('ground plane', 'Ground Plane')], help_text='Location of First Sight of the squirrel', max_length=20)),
                ('specific_location', models.CharField(blank=True, help_text='Specific Location', max_length=100)),
                ('running', models.BooleanField(default=False, help_text='Squirrel was seen running.')),
                ('chasing', models.BooleanField(default=False, help_text='Squirrel was seen chasing another squirrel')),
                ('climbing', models.BooleanField(default=False, help_text='Squirrel was seen climbing a tree or other environmental landmark')),
                ('eating', models.BooleanField(default=False, help_text='Squirrel was seen eating')),
                ('foraging', models.BooleanField(default=False, help_text='Squirrel was seen foraging for food')),
                ('other_activities', models.CharField(blank=True, help_text='Other Activities', max_length=100)),
                ('kuks', models.BooleanField(default=False, help_text='Squirrel was heard kukking')),
                ('quaas', models.BooleanField(default=False, help_text='Squirrel was heard quaaing')),
                ('moans', models.BooleanField(default=False, help_text='Squirrel was heard moaning')),
                ('tail_flags', models.BooleanField(default=False, help_text='Squirrel was seen flagging its tail')),
                ('tail_twitches', models.BooleanField(default=False, help_text='Squirrel was seen twitching its tail')),
                ('approaches', models.BooleanField(default=False, help_text='Squirrel was seen approaching human')),
                ('indifferent', models.BooleanField(default=False, help_text='Squirrel was indifferent to human presence')),
                ('runs_from', models.BooleanField(default=False, help_text='Squirrel was seen running from humans')),
            ],
        ),
    ]
