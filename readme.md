# PASO 1 - Crear virtual enviroment (Primero!)
python3 -m venv venv

# PASO 2 - Activar virtual enviroment
source venv/bin/activate

# PASO 3 - Instalar dependencias
pip install -r requirements.txt

# PASO 4 -Correr el servidor (local)
uvicorn main:app --reload
