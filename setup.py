from io import open
from setuptools import setup

long_description = ''
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='frolic-engine',
    version='1.0.1',
    license='MIT',
    url='https://github.com/nateonguitar/FrolicEngine',
    description='A game engine that lets you write text/ansii based games, targets 60fps.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Nate Brooks',
    author_email='nateonguitar@gmail.com',
    packages=[
        'frolic',
    ],
    install_requires=[
        'pynput',
        'numpy',
        'colorama',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='game games engine text based frolic',
)
