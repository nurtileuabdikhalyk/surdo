from django.contrib.auth.models import User
from django.db import models


class Dictionary(models.Model):
    word = models.CharField('Сөз', max_length=150)
    description = models.TextField('Түсіндірме', blank=True, null=True)
    url_youtube = models.CharField('Сілтеме', max_length=255, blank=True, null=True)
    slug = models.SlugField('Слаг')

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Сөздік'
        verbose_name_plural = 'Сөздіктер'


class Question(models.Model):
    first_name = models.CharField('Есіміңіз', max_length=150)
    email = models.EmailField('Почта', )
    message = models.TextField('Хабарлама мәтіні')
    created = models.DateTimeField('Келген күні', auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.email}"

    class Meta:
        verbose_name = 'Сұрақ'
        verbose_name_plural = 'Сұрақтар'


class News(models.Model):
    title = models.CharField('Тақырыбы', max_length=150)
    image = models.ImageField('Сурет', upload_to='image_news/', blank=True, null=True)
    description = models.TextField('Сипаттама')
    slug = models.SlugField('Слаг')
    created = models.DateTimeField('Келген күні', auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Жаңалық'
        verbose_name_plural = 'Жаңалықтар'


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField('Есімі', max_length=150)
    last_name = models.CharField('Тегі', max_length=150, null=True, blank=True)
    phone = models.CharField('Телефон номері', max_length=150, null=True, blank=True)
    status_admin = models.BooleanField('Админ статусы', default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Жүйе қолданушы'
        verbose_name_plural = 'Жүйе қолданушы'


class QuesModel(models.Model):
    question = models.CharField('Сұрақ', max_length=500)
    op1 = models.CharField('Нұсқа №1', max_length=500)
    op2 = models.CharField('Нұсқа №2', max_length=500)
    op3 = models.CharField('Нұсқа №3', max_length=500)
    op4 = models.CharField('Нұсқа №4', max_length=500)
    answer = models.CharField('Жауап', max_length=500)

    class Meta:
        verbose_name = 'Тест сұрағы'
        verbose_name_plural = 'Тест сұрақтары'

    def __str__(self):
        return self.question


class Result(models.Model):
    user = models.ForeignKey(Users, verbose_name='Қолданушы', on_delete=models.CASCADE)
    score = models.IntegerField('Ұпай')
    percent = models.DecimalField('Процент', max_digits=3, decimal_places=1)
    correct = models.IntegerField('Дұрыс жауаптар саны')
    incorrect = models.IntegerField('Қате жауаптар саны')
    total = models.IntegerField('Барлық сұрақтар саны')

    class Meta:
        verbose_name = 'Нәтиже'
        verbose_name_plural = 'Нәтижелер'

    def __str__(self):
        return f"{self.user} {self.score}"
