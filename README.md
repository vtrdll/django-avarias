# django-avarias
Avarias são um grande problema para a área de transporte, pois atrasa a logística tanto fisicamente quanto financeiramente.  

PARA UTILIZAR

Abra seu terminal e rode:

git clone https://github.com/vtrdll/django-avarias.git

cd django-avarias

Crie e ative um ambiente virtual: 

python -m venv venv

venv\Scripts\activate

Instale as dependencias:

pip install -r requirements.txt

Rode as migrações do banco de dados

python manage.py migrate

Inicie o servidor local

python manage.py runserver
