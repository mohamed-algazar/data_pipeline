from setuptools import setup, find_packages

setup(
    name='data_pipeline_project',  # Name of the overall project, not just one module
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A modular data pipeline project for Maji Ndogo farm data processing.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'pandas',
        'numpy',
        'sqlalchemy',
        'requests'  # optional if you later fetch data dynamically
    ],
    url='https://github.com/mohamed-algazar',
    author='Mo Ali',
    author_email='eng.mohamedelgazar1@gmail.com',
    python_requires='>=3.8',
)
