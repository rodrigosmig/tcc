~~ DEPENDÊNCIAS
Python 3.X
Pip
Django 1.11
Django Widget-Tweaks
Django Rest Framework
Django CORS Headers
scikit-learn
Numpy
NodeJS
VueJS
BootstrapVue
Moment
Axios

~~ ANTES DE EXECUTAR A PRIMEIRA VEZ
tcc$ sudo pip install -r requirements.txt
tcc/tcc-vue$ npm install

~~ EXECUTAR APENAS NA PRIMEIRA VEZ OU QUANDO O MODEL FOR MODIFICADO
tcc$ python manage.py makemigrations
tcc$ python manage.py migrate
tcc$ python manage.py createsuperuser

~~ EXECUTAR O PROJETO
tcc$ python manage.py runserver
tcc/tcc-vue$ npm run dev
