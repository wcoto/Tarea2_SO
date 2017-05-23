# Use an official Python runtime as a base image
FROM centos:7


RUN yum -y update
RUN yum -y install yum-utils
RUN yum -y groupinstall development
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

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV portServer 9999

# Run app.py when the container launches
CMD ["python3.6", "ejemploPython.py"]
