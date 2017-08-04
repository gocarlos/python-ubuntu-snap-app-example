import os

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

this = os.path.dirname(os.path.realpath(__file__))

def read(name):
    with open(os.path.join(this, name)) as f:
        return f.read()
setup(
    name='my_great_app',
    version='0.0.1',
    description='description',
    long_description=readme,
    author='Carlos Gomes',
    author_email='kmartinho8@gmail.com',
    url='https://github.com/gocarlos/python-ubuntu-snap-app-example',
    packages=['myapp_source'],
    install_requires=read('requirements.txt'),
    include_package_data=True,
    zip_safe=True,
    licence='BSD - 3',
    keywords='example app snap linux ubuntu',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English'
    ],
    test_suite='tests',
    scripts=['bin/my_great_app']
)
