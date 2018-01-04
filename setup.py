
from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

install_requires = [
    'setuptools',
    'requests',
    'argparse',
    
    ]

setup(
    name="readit",
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'readit = manager.__init__.py:main',
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
    namespace_packages=[],
            
    include_package_data=True,
    zip_safe=False,
 
    install_requires=install_requires,
    scripts = [
        'scripts/dbsetup',
        ],
    )
 

