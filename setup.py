from setuptools import setup

VERSION = '0.0.2'
DESCRIPTION = 'USPS Address API 3.0 Python wrapper'

setup(
    name='pyuspsaddress2',
    version=VERSION,
    description=DESCRIPTION,
    url='https://github.com/nexant-uts/pyuspsaddress2',
    author='Resource Innovations',
    author_email='',
    license='MIT',
    packages=['pyuspsaddress2'],
    install_requires=['requests',
                      'djangorestframework',
                      'pytest'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
