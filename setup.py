from distutils.core import setup

setup(
    name='Guildr',
    version='1.0.0',
    author='akimbo',
    author_email='akimbo7@protonmail.com',
    packages=['guildr',],
    url='https://github.com/akimbo7/Guildr',
    license='LICENSE',
    python_requires='>=3.7.0',
    description='A simple API Wrapper for Guilded.',
    long_description=open('README.md').read(),
    install_requires=[
        "requests>=2.27.1",
        "bs4>=0.0.1",
        "lxml>=4.8.0"
    ],
)
