from io import open
from setuptools import setup

def read(fname, encoding='utf-8'):
    with open(fname, encoding=encoding) as f:
        return f.read()

setup(
    name='pyDOE2',
    version="1.2.0",
    author='Rickard Sjoegren',
    author_email='r.sjogren89@gmail.com',
    description='Design of experiments for Python',
    url='https://github.com/clicumu/pyDOE2',
    license='BSD License (3-Clause)',
    long_description=read('README.md'),
    packages=['pyDOE2'],
    install_requires=['numpy', 'scipy'],
    keywords=[
        'DOE',
        'design of experiments',
        'experimental design',
        'optimization',
        'statistics',
        'python'
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
        ]
    )

