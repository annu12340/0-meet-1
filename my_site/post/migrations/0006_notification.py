# Generated by Django 3.1.7 on 2021-05-04 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_postideamodel_createdby_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sendfrom_id', models.IntegerField()),
                ('sendfrom_name', models.CharField(max_length=200)),
                ('sendfrom_img', models.CharField(max_length=200)),
                ('sendto_id', models.IntegerField()),
                ('status', models.CharField(default='Pending', max_length=200)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
