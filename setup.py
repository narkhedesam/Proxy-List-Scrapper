from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='Proxy-List-Scrapper',
    version='0.1.4',
    packages=find_packages(),
    url='',
    license='MIT License',
    author='Sameer Narkhede',
    author_email='narkhedesam@gmail.com',
    description='proxy list scrapper from various websites. they gives the free proxies for temporary use.',
    # other arguments omitted
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
          'requests',
      ],
    include_package_data=True,

)
