# Generated by Django 4.0.4 on 2022-04-23 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_remove_appartement_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='universite',
            name='ville',
            field=models.CharField(choices=[('tunis', 'tunis'), ('ariana', 'ariana'), ('benArous', 'benArous'), ('manouba', 'manouba'), ('nabeul', 'nabeul'), ('zaghouan', 'zaghouan'), ('bizerte', 'bizerte'), ('béja', 'béja'), ('jendouba', 'jendouba'), ('siliana', 'siliana'), ('sousse', 'sousse'), ('monastir', 'monastir'), ('mahdia', 'mahdia'), ('sfax', 'sfax'), ('kairouan', 'kairouan'), ('kasserine', 'kasserine'), ('sidiBouzid', 'sidiBouzid'), ('gabès', 'gabès'), ('mednine', 'mednine'), ('tataouine', 'tataouine'), ('gafsa', 'gafsa'), ('tozeur', 'tozeur'), ('kebili', 'kebili')], default='tunis', max_length=50),
        ),
        migrations.AlterField(
            model_name='universite',
            name='type',
            field=models.CharField(choices=[('public', 'public'), ('prive', 'prive')], default='public', max_length=50),
        ),
    ]
