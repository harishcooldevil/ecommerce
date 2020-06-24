# Generated by Django 3.0.6 on 2020-06-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sports Wear'), ('OW', 'Out Wear')], default='S', max_length=2),
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'Primary'), ('S', 'Secondary'), ('D', 'Danger')], default='P', max_length=1),
        ),
    ]