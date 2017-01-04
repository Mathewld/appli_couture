# Application de gestion pour la couture

Apprendre Django avec une application pour la couture.

```bash
# lancer virtualenv sous windows
myvenv\Scripts\activate
# ... ou sous linux
source myvenv/bin/activate

# migrer la base de données
python manage.py migrate

# charger de fausses données en base
python manage.py loaddata **/fixtures/*.json

# créer super utilisateur
python manage.py createsuperuser

# lancer l'application
python manage.py runserver
```
