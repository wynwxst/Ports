from setuptools import setup

setup(name='ports.py',
      version='0.6.0',
      description='A modern webserver, check github for more information',
      url='http://github.com/n30nyx/ports',
      author='n30nyx/Sakurai07',
      author_email='blzzardst0rm@gmail.com',
      license='MIT',
      packages=['ports'],
    install_requires=[
        "requests","websockets"
        ],
    keywords=['webserver', 'flask alternative','ports'],
    classifiers=["Programming Language :: Python :: 3"],
      zip_safe=False)
