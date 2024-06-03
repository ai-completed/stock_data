
from setuptools import setup, find_packages

setup(
    name='AutomatedOptionsTrading',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
        'flask',
        'apscheduler'
    ],
    entry_points={
        'console_scripts': [
            'run-server=server:app.run'
        ]
    },
    python_requires='>=3.8',
)
