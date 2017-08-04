from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [

]

test_requirements = [
'pytest'
]

setup_requires=[
'pytest-runner'
]

setup(
    name='my_great_app',
    version='0.0.1',
    description='description',
    long_description=readme,
    author='Carlos Gomes',
    author_email='kmartinho8@gmail.com',
    url='https://github.com/gocarlos/python-ubuntu-snap-app-example',
    packages=find_packages(exclude=('tests')),
    install_requires=requirements,
    include_package_data=True,
    licence='BSD - 3',
    zip_safe=False,
    keywords='example, app, snap, linux, ubuntu',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requires,
    scripts=['bin/my_great_app']
)
