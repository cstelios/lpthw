try:
    from setuptools import setuptools
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'L.P.t.H.W ex47',
    'author' : 'Stelios Charalambous',
    'url' : 'url to get it at',
    'download_url' : 'Where to download it',
    'author_email' : 'cstelios@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['ex47'],
    'scripts' : [],
    'name' : 'projectname'
}

setuptools.setup(**config)
