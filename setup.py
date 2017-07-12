from setuptools import setup

setup(name='Distutils',
      version='1.0',
      description='This is sample python project setup',
      author='Bharath Kumar',
      author_email='mail.bharath92@gmail.com',
      url='',
      packages=['distutils', 'distutils.command'],
      install_requires=[
          'python-jenkins'
      ]
      )
