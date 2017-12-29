
from setuptools import setup, find_packages



install_requires = [
    'setuptools',
    'requests',
    'argparse',
    ]

#tests_require = [
    # See tox.iniq
 #   'pytest >=2.8.3',
   # 'coverage',
  #  ]


setup(
    name="readit",
    version="0.1.0",
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
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        (
            
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    include_package_data=True,
    zip_safe=False,
   # setup_requires=setup_requires,
    install_requires=install_requires,
   # tests_require=tests_require,
  #  extras_require=dict(
   #     tests=tests_require,
    #    docs=docs_require,
     #   ),
      # add more sources of randomness here...
 #  },
)
