from setuptools import setup

_VERSION='0.1.8'

setup(
    name='pyplelogger',
    version=_VERSION,
    description='Simple logger in python mainly used for CLI tool like argparse',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='KeisukeYamashita',
    author_email='19yamashita15@gmail.com',
    license='MIT',
    keywords='logger cli logging',
    packages=[
        "pyplelogger"
    ],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License",
    ],
)
