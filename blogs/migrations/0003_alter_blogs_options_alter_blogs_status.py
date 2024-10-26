# Generated by Django 5.0.1 on 2024-02-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_category_options_blogs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogs',
            options={'verbose_name_plural': 'blogs'},
        ),
        migrations.AlterField(
            model_name='blogs',
            name='status',
            field=models.IntegerField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft'),
        ),
    ]