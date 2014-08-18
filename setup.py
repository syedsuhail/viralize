try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Suhail',
    'author': 'Suhail',
    'author_email': 'ssuhail.ahmed93@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['viralize'],
    'scripts': [],
    
}

setup(**config)
