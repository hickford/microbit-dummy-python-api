from setuptools import setup

setup(
    name='microbit-dummy',

    # useful: python setup.py sdist bdist_wheel upload
    version='0.0.1',

    description='A dummy Python implementation of the microbit module for MicroPython.',

    url='https://github.com/hickford/microbit-dummy-python-api',

    license='MIT',

    classifiers=[
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],

    py_modules=['microbit'],
)
