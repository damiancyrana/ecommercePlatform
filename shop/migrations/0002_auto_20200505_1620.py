# Generated by Django 3.0.6 on 2020-05-05 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productgroup',
            options={'ordering': ('label',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_group',
            new_name='category',
        ),
    ]
