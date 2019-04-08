from django.db import models


# Create your models here.
class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains=query) or models.Q(description__icontains=query))


class Course(models.Model):

    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Atalho", )
    description = models.TextField("Descrição", blank=True)
    about = models.TextField("Sobre o Curso", blank=True)
    start_date = models.DateField("Data de Início", null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CourseManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # from django.urls import reverse
        # return reverse('courses.view.details', args=[str(self.slug)])
        return '/cursos/%s' % self.slug

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']  # Crescente
        # ordering = ['-name']  # Decrescente

# Commands
# add in settings
# python manage.py makemigrations courses
# python manage.py sqlmigrate courses 0001
# python manage.py migrate
# python manage.py shell
