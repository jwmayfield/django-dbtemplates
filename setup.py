from setuptools import setup, find_packages

setup(
    name='django-dbtemplates',
    version=__import__('dbtemplates').__version__,
    description='Template loader for database stored templates with extensible cache backend',
    long_description=open('docs/overview.txt').read(),
    author='Jannis Leidel',
    author_email='jannis@leidel.info',
    url='http://packages.python.org/django-dbtemplates/',
    packages=find_packages(exclude=['example']),
    zip_safe=False,
    package_data = {
        'dbtemplates': [
            'locale/*/LC_MESSAGES/*',
            'media/dbtemplates/css/*.css',
            'media/dbtemplates/js/*.js',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
