from setuptools import setup

setup(
    name='deng',
    version='0.1.0',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'deng = main:cli',
        ],
    },
)
