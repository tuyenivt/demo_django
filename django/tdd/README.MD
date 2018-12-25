# Activate virtualenv
pip install virtualenv
virtualenv venv
venv\Scripts\activate

# Install Library
pip install -r requirements.txt

# Test Blog
python manage.py test blog
