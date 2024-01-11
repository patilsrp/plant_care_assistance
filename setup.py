from setuptools import setup, find_packages

setup(
    name='login_portal',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'mysql-connector-python',
        # Add any other dependencies here
    ],
)
