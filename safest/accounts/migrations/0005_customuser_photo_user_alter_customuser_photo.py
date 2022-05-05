# Generated by Django 4.0.4 on 2022-05-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_conservatrice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='photo_user',
            field=models.ImageField(blank=True, null=True, upload_to='users/photos'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.TextField(),
        ),
    ]