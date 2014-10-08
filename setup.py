from setuptools import setup, find_packages

setup(
    name='awssp',
    version='0.0.1',
    description='AWS Security Pictures',
    long_description='Generate detailed images of AWS infrastructure for security reviews.',
    classifiers=['Programming Language :: Python'],
    keywords='AWS securitygroups firewall nacl',
    author='Daniel Lawrence',
    author_email='dannyla@linux.com',
    url='http://github.com/daniellawrence/aws-security-pictures',
    license='The MIT License (MIT)',
    install_requires=['awscli'],
    packages=find_packages('bin'),
    package_dir={'': 'bin'},
    scripts=["bin/awssp"],
    include_package_data=True,
    zip_safe=False,
)
