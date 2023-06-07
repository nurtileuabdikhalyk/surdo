# Generated by Django 4.1 on 2023-04-06 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='Сұрақ')),
                ('op1', models.CharField(max_length=500, verbose_name='Нұсқа №1')),
                ('op2', models.CharField(max_length=500, verbose_name='Нұсқа №2')),
                ('op3', models.CharField(max_length=500, verbose_name='Нұсқа №3')),
                ('op4', models.CharField(max_length=500, verbose_name='Нұсқа №4')),
                ('answer', models.CharField(max_length=500, verbose_name='Жауап')),
            ],
            options={
                'verbose_name': 'Тест сұрағы',
                'verbose_name_plural': 'Тест сұрақтары',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='Ұпай')),
                ('percent', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Процент')),
                ('correct', models.IntegerField(verbose_name='Дұрыс жауаптар саны')),
                ('incorrect', models.IntegerField(verbose_name='Қате жауаптар саны')),
                ('total', models.IntegerField(verbose_name='Барлық сұрақтар саны')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.users', verbose_name='Қолданушы')),
            ],
            options={
                'verbose_name': 'Нәтиже',
                'verbose_name_plural': 'Нәтижелер',
            },
        ),
    ]