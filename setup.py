
from setuptools import setup,find_packages

setup (
    name= "Maria_Isabel_Soto",
    version= "0.0.1",
    author= "Maria Isabel Soto",
    author_email= "maria.sotoio@est.iudigital.edu.co",
    description= "",
    py_modules= ["Entregable actividad 1 y 2"],
    install_requires= [
        "kagglehub[pandas-datasets]>=0.3.8",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.2",
        "pandas",
        "numpy",
        "matplotlib",
        "openpyxl",
        "requests"
 ]
 )
