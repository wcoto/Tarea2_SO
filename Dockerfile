# Use an official Python runtime as a base image
FROM centos:7

# Update system
RUN yum -y update
# tools for manipulating repositories and extended package management
RUN yum -y install yum-utils
# The Development tools will allow you to build and compile software from source code
RUN yum -y groupinstall development
# 
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm
RUN yum -y install python36u
RUN yum -y install python36u-pip
RUN yum -y install gcc gmp python3-devel
RUN pip3.6 install pycryptodomex

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
#RUN pip install -r requirements.txt

# Define environment variable
# ENV PublicKey MIICWwIBAAKBgQDfpxunGwNeLG+HnvGlmTIXU7mAtw6sZjq//kKyZhmcR8MJc/9nxfdbylB6+COSsf70rFRPoMPlBDPvIBc/kCrEuFpVm86CAPuN08BXvNcUlQmuw++e0KeXtJ33jUw4DdF2xNnLTtnl+u+s0v8xJGZrJF6Ges1j1OMb6B0fR+fxkQIDAQABAoGACsLUTPl683D7RozwcvOknixXTYz5R/SlBOQBrupkVvF5vhqihkpnXwd0cP8/nG1Dr397cMejJ1G5AzthvPtlgFG47zkz/MPT0kLUaAwShciHFXDMkrmP9hCRF6v+cvII/8GsG92tixNoQYmnqbNPtmbJ25ARK6cP7MvsPjGEGWECQQDuRO266fGqBHOVEAcZsu8DW3pOQ8JFdGAjWoxqHO1GqQshBMbghK0E5k/mdXTXJSrMfiGbRGvj0Lunph1m5/JxAkEA8Eu7lCLXCTV5tzgGWu6eCFemThUn4xzhikIyU6B32hLEJcdddPjW37wR1zSrybPYopX3C/66o3+xMzQGmiNBIQJANPbNgYcPWSO0LaZqbaQAzVZAUbVuMdI0rKcsH0pe1B4vgx90tePIMhagHDJvzoNMiDhhcAo9kV6M2C9sybs1gQJAVJslsZPOyNRGRcd5HV000VUjHgz+3U1W8Bo8pAs1B9hhrbeTZVMUPPR4B6Do93zWQvCwak3HIzgbiR7BUFYnYQJAKbodBCCxa6GDjEj3hbMx22WtAMInqwROYm84yTk1LZbGxc3bVfmqaPMW9U7NRH+MwWy04wNsmcUDQmvS6kFITw==

# Run app.py when the container launches
CMD ["python3.6", "-u", "tarea2.py"]
