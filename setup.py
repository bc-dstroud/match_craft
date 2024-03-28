from setuptools import setup, find_packages

setup(
    name='match_craft',
    version='0.1.0',
    packages=find_packages(),
    description='A utility package for Spark, ML modeling, and MLflow in Databricks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='David Stroud',
    author_email='david.stroud@bluecrewjobs.com',
    #url='https://github.com/yourusername/your_package_name',
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'mlflow',
        'pyspark',
        'plotly'
    ],
    python_requires='>=3.6',
)
