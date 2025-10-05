from setuptools import setup, find_packages

setup(
    name='data_ingestion',  # The package name
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A data ingestion module for reading CSVs and querying databases.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',  # important for PyPI later
    install_requires=[
        'pandas',
        'sqlalchemy'
    ],
    url='https://github.com/mohamed-algazar',
    author='Mo Ali',
    author_email='eng.mohamedelgazar1@gmail.com',
    python_requires='>=3.8',
)
