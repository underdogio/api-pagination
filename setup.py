from setuptools import setup, find_packages


setup(
    name='api_pagination',
    version='1.0.0',
    description='Pagination calculator designed for APIs',
    long_description=open('README.rst').read(),
    keywords=[
        'paginate',
        'pagination',
        'calc',
        'calculate',
        'calculator',
        'api'
    ],
    author='Todd Wolfson',
    author_email='todd@twolfson.com',
    url='https://github.com/underdogio/api-pagination',
    download_url='https://github.com/underdogio/api-pagination/archive/master.zip',
    packages=find_packages(),
    license='MIT',
    install_requires=open('requirements.txt').readlines(),
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
