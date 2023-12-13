from setuptools import setup

setup(
   name = 'secret_santa',
   version='1.0',
   description='A secret santa bot.',
   author='Jessica Negara',
   author_email='jessica.negara@gmail.com',
   packages = ['secret_santa_lib'],
   install_requires=['twilio'],
   scripts = [ 'scripts/run.py' ],
)

