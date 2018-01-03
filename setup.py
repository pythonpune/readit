
from setuptools import setup, find_packages



install_requires = [
    'setuptools',
    'requests',
    'argparse',
    
    ]

setup(
    name="readit",
    version="0.1",
    author="Ganesh, Shital, Daivshala",
    author_email="ganeshhubale03@gmail.com",
    description=(
        "It is bookmark manager."),
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
 

