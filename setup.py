"""
Flask Principal
---------------

Identity management for Flask.

Links
`````

* `documentation <http://packages.python.org/Flask-Principal/>`_
* `source <https://github.com/mattupstate/flask-principal>`_
* `development version
  <https://github.com/mattupstate/flask-principal/raw/master#egg=Flask-Principal-dev>`_

"""

from setuptools import setup


setup(
    name='Flask-Principal',
    # used 0.4.1 because 0.4.0 is a version that is tagged from code from the year 2013 (you don't see 0.4.0 in the
    # git log because it seems that tag came from a different branch, not master)
    # There are already more commits in 2015, but no 0.4.1 was ever released, but it would make no sense to number this
    # 0.4.0. So just pretended that a 0.4.1 exists and gave this a +atbay local modifier
    version='0.4.1+atbay',
    url='http://packages.python.org/Flask-Principal/',
    license='MIT',
    author='Ali Afshar',
    author_email='aafshar@gmail.com',
    maintainer='Matt Wright',
    maintainer_email='matt@nobien.net',
    description='Identity management for flask',
    long_description=__doc__,
    py_modules=['flask_principal'],
    zip_safe=False,
    platforms='any',
    install_requires=['Flask', 'blinker'],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
