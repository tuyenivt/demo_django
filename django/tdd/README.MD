# Activate virtualenv
pip install virtualenv
virtualenv venv
venv\Scripts\activate

# Install Library
pip install -r requirements.txt

# Test Blog
python manage.py test blog

# Configure Coverage
Update configurations in .coveragerc <<EOF
[run]
include = ./*
branch = True
EOF

# Test Coverage
coverage run manage.py test blog
coverage report
