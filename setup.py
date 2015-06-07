# -*- coding: utf-8 -*-

__author__ = 'Renato de Pontes Pereira'
__author_email__ = 'renato.ppontes@gmail.com'
__version__ = '0.1.1'
__date__ = '2015 06 07'

try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

from setuptools import setup, find_packages

try:
    f = open('README.rst','rU')
    long_description = f.read()
    f.close()
except:
    long_description = ''

setup(
    name = 'vindinium',
    version = __version__,
    author = __author__,
    author_email = __author_email__,
    license='MIT License',
    description = 'Python client for vindinium.',
    long_description=long_description,
    url = 'https://guithub.com/renatopp/vindinium-python/releases',
    download_url = 'https://guithub.com/renatopp/vindinium-python',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        ('Topic :: Software Development :: Libraries :: Python Modules'),
        ('Topic :: Scientific/Engineering :: Artificial Intelligence'),
    ],
    keywords='vindinium game python',
    packages=find_packages(),
    package_data={'':['README.rst', 'LICENSE']},
    install_requires=['requests>=2.7.0']
)
