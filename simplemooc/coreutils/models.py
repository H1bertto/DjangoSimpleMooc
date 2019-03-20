from django.db import models


# Create your models here.
class Course(models.Model):

    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Atalho", )
    descripition = models.TextField("Descrição", blank=True)
    start_date = models.DateField("Data de Início", null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

# Commands
# add in settings
# python manage.py makemigrations coreutils
# python manage.py sqlmigrate coreutils 0001
# python manage.py migrate
# python manage.py shell
