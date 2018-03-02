import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


install_requires = [
    'setuptools',
    'requests',
    'click',
    'beautifultable',
]

setup(
    name="readit",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'readit = readit.__init__:main',
        ],
    },
    version="v0.1",
    author="Ganesh, Shital, Daivshala",
    author_email="ganeshhubale03@gmail.com",
    description="It is bookmark manager.",
    long_description=read('README.rst'),
    license="GNU General Public License v3.0",
    keywords="clitool bookmark readit",
    url="https://github.com/ganeshhubale/readit",
    py_modules=['readit.__init__'],
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
)
