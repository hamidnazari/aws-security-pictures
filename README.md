[![Build Status](https://travis-ci.org/daniellawrence/aws-security-pictures.svg?branch=master)](https://travis-ci.org/daniellawrence/aws-security-pictures)


# AWS Security Pictures

Generate detailed images of AWS infrastructure for security reviews.

# Dependencies

AWSSP depends on `graphviz` and `awscli`.

On Debian/Ubuntu:

	$ sudo apt-get install graphviz python-pip

On Fedora/CentOS/RedHad:

	$ sudo yum install graphviz python-pip

On Mac:

	$ brew install graphviz
	$ sudo easy_install pip


# How to Install

	$ git clone https://github.com/daniellawrence/aws-security-pictures
	$ python ./setup.py install

or

	$ cd aws-security-pictures
	$ pip install -r requirements.txt


# How to Contribute

	$ pip install -r requirements-dev.txt

Please make sure the following command exits successfully before pushing your
code.

	$ flake8 --ignore=E501
	$ python ./setup.py install


# How to run

It is recommended to utiliase `awssp` command that executes below commands
in one go. More info,

	$ awssp -h

Example:

	$ awssp -p PROFILENAME -l ELBNAME -r RDSID

## generate.py

Generate a picture of an ELB and attached EC2s,

	$ generate.py --elb ELBNAME -o output.dot

Generate a picture of an EC2,

	$ generate.py --ec2 EC2ID -o output.dot

Attach and RDS to a picture of an ELB and attached EC2s, or just an EC2,

	$ generate.py --elb ELBNAME --rds RDSID -o output.dot

or

	$ generate.py --ec2 EC2ID --rds RDSID -o output.dot

The above generate the dot files required. In order to see the output image,

	$ dot -T png output.dot -o output.png

Generate a list of all ELBs and EC2s,

	$ generate.py

Make use of AWS CLI profiles,

	$ generate.py --profile PROFILENAME

	or

	$ generate.py -p PROFILENAME

More handy arugments can be found here,

	$ generate.py -h


# Experiments

Generate all rules within a subnet for review,

	$ experiments/firewall_review.py > x.dot && fdp -Tpng x.dot >x.png && eog x.png

Generate the relationships of all the items with a account,

	$ experiments/relationships.py > x.dot && fdp -Tpng x.dot >x.png && eog x.png


# Examples

ELB pointing to a single instances.

![](https://raw.githubusercontent.com/daniellawrence/aws-security-pictures/master/examples/simple_example.png)
