__version__ = "0.1"

setup(
    name='Flask-SuperMenu',
    version=__version__,
    url='https://github.com/smontoya/flask-supermenu',
    license='GNU',
    author='Samuel Montoya',
    description='Flask-SuperMenu is a Flask extension that adds support ' \
                'menus and breadcrumbs',
    long_description=open('README.rst').read(),
    packages=['flask_supermenu'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Flask',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 5 - Production/Stable'
    ],
)
