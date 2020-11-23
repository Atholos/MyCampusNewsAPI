from setuptools import find_packages, setup

setup(
    name="app",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
            "aniso8601",
            "click" ,
            "Flask",
            "Flask-RESTful",
            "Flask-SQLAlchemy",
            "itsdangerous",
            "Jinja2",
            "MarkupSafe",
            "pytz",
            "six",
            "SQLAlchemy",
            "Werkzeug",
            "flake8",
            "pytest",
            "pytest-cov",
            "pytest-flask",
            "pytest-xdist",
            "gunicorn",
            "psycopg2",
            "pylint-flask",
            "flask-bcrypt",
            "azure-storage-blob",
    ]

  