# Django Project

### Plataforma de Cursos MOOC (Massive Open Online Course)

Baseado no Curso [Python 3 na Web com Django (Básico e Intermediário)](https://www.udemy.com/course/python-3-na-web-com-django-basico-intermediario/)


__NOTA:__ Recomendado [Python 3.6+](https://www.python.org/downloads/)

## Start

Para testar o projeto siga os passos a seguir:

1. Clone o Projeto
```
git clone https://github.com/H1bertto/DjangoSimpleMooc.git
```

2. Mude para pasta do progete e execute o `start.bat`
```
cd DjangoSimpleMooc
start.bat
```
Ou se seu SO for Windows `win-start.bat`
```
cd DjangoSimpleMooc
win-start.bat
```

3. Migre os dados para o banco de dados
```
python manage.py migrate
```

4. Crie um superuser
```
python manage.py createsuperuser
```

5. Rode a Aplicação
```
python manage.py runserver
```

__NOTA:__ Para que o envio de emails funcione sem ser pelo console edite em `settings.py` os campos <EMAIL> e <PASSWORD> com suas informações e troque as linhas comentadas a seguir:


De:
```
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Para:
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'