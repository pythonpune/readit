
from setuptools import setup, find_packages

with open("README") as f:
    long_description = f.read()

install_requires = [
    'setuptools',
    'requests',
    'argparse',
    
    ]

setup(
    name="readit",
    entry_points = {
        'console_scripts': [
            'readit = __init__.py:main',
            ],
        },
    version="0.1",
    author="Ganesh, Shital, Daivshala",
    author_email="ganeshhubale03@gmail.com",
    description="It is bookmark manager.",
    long_description = long_description,
    license="MIT",
    keywords="clitool bookmark readit",
    url="https://github.com/ganeshhubale/readit",
    py_modules=[],
    packages=['manager', ],
    namespace_packages=[],
            
    include_package_data=True,
    zip_safe=False,
 
    install_requires=install_requires,
    )
 

