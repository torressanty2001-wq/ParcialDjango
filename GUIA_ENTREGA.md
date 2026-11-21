# Guía de entrega – Modelo Programa (Django)

Usuario del admin local: `admin` / `Admin12345` (cámbiala en PythonAnywhere con `createsuperuser`).

## Parte 2A. GitHub (desde la carpeta del proyecto)
```bash
git remote set-url origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
git add .
git commit -m "Modelo Programa, formulario, plantillas y db.sqlite3"
git branch -M main
git push -u origin main
```
Verifica en GitHub que `db.sqlite3` aparezca en el repositorio.

## Parte 2B. PythonAnywhere (consola Bash)
```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO
mkvirtualenv --python=/usr/bin/python3.13 venv   # usa la versión que ofrezca tu cuenta
pip install -r requirements.txt
python manage.py collectstatic --noinput
```
Si `pip` falla con `requirements.txt` (viene en UTF-16): `pip install Django asgiref sqlparse tzdata`.

Pestaña **Web** → *Add a new web app* → *Manual configuration* (misma versión de Python):
- **Source code / Working directory:** `/home/TU_USUARIO/TU_REPOSITORIO`
- **Virtualenv:** `/home/TU_USUARIO/.virtualenvs/venv`
- **WSGI file** (reemplaza el contenido):
```python
import os, sys
path = "/home/TU_USUARIO/TU_REPOSITORIO"
if path not in sys.path:
    sys.path.append(path)
os.environ["DJANGO_SETTINGS_MODULE"] = "my_project.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
- **Static files:** URL `/static/` → Directory `/home/TU_USUARIO/TU_REPOSITORIO/staticfiles`
- En `settings.py` deja `ALLOWED_HOSTS = ["TU_USUARIO.pythonanywhere.com"]` (haz commit/push y `git pull` en PA).
- Pulsa **Reload** y prueba `/programas/crear/` y `/admin/`.

## Entregables
1. URL del repositorio: https://github.com/TU_USUARIO/TU_REPOSITORIO
2. URL del sitio: https://TU_USUARIO.pythonanywhere.com/programas/crear/
