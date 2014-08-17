try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Suhail',
    'author': 'Suhail',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'ssuhail.ahmed93@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['viraliz'],
    'scripts': [],
    
}

setup(**config)
