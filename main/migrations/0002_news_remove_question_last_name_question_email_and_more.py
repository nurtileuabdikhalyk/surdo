# Generated by Django 4.1 on 2023-02-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Тақырыбы')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image_news/', verbose_name='Сурет')),
                ('description', models.TextField(verbose_name='Сипаттама')),
                ('slug', models.SlugField(verbose_name='Слаг')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Келген күні')),
            ],
            options={
                'verbose_name': 'Жаңалық',
                'verbose_name_plural': 'Жаңалықтар',
            },
        ),
        migrations.RemoveField(
            model_name='question',
            name='last_name',
        ),
        migrations.AddField(
            model_name='question',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='Почта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='Есіміңіз'),
        ),
    ]
