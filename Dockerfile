# DockerFile for a Fludity development container

# Use a Trusty base image
FROM ubuntu:xenial

# This DockerFile is looked after by
MAINTAINER Tim Greaves

# Add the Fluidity repository
RUN echo "deb http://ppa.launchpad.net/fluidity-core/ppa/ubuntu xenial main" > /etc/apt/sources.list.d/fluidity-core-ppa-xenial.list

# Import the Launchpad PPA public key
RUN gpg --keyserver keyserver.ubuntu.com --recv 0D45605A33BAC3BE
RUN gpg --export --armor 33BAC3BE | apt-key add -

# Update the system
RUN apt-get update
RUN apt-get -y dist-upgrade

# Install Fluidity development environment
RUN apt-get -y install fluidity-dev

# Add a Fluidity user who will be the default user for this container
RUN adduser --disabled-password --gecos "" fluidity
USER fluidity
WORKDIR /home/fluidity
ENV PETSC_DIR /usr/lib/petscdir/3.6.3

# Set the configure flags
ENV CONFFLAGS --enable-2d-adaptivity
ENV BRANCH -b master
ENV PROJECT FluidityProject

# Get the Fluidity source
RUN git clone $BRANCH https://github.com/$PROJECT/fluidity.git
WORKDIR /home/fluidity/fluidity
RUN git clone https://github.com/FluidityProject/longtests.git
RUN ./configure $CONFFLAGS
RUN make
RUN make fltools
RUN make manual

# Build over, create packages
USER root
RUN apt-get update
RUN apt-get -y install devscripts debhelper
USER fluidity
RUN debuild -uc -us
# Put them in a directory buildbot can find
WORKDIR /home/fluidity
USER root
RUN mkdir /packages
RUN cp *deb /packages
# And define how to install them
WORKDIR /packages
RUN echo "dpkg -i /packages/*deb" > install.sh
RUN chmod 755 install.sh
Status API Training Shop Blog About

# Back to the source directory and user
WORKDIR /home/fluidity/fluidity
USER fluidity
