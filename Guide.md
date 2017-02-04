# Setting Up A Cluster Using MPI4Py on Fedora 25

This file consolidates all the steps that were taken to set up a working MPI cluster on Fedora 25 using MPICH and MPI4Py based on steps seen in the [Resources](paradime/Resources.md).

**Step 1: Install the packages required for the setup on all machines.**

>sudo dnf install python-devel mpich-devel mpich-autoload python-mpi4py

*Note: Assuming openssh and nfs-utils are installed. Else, install those packages as well.*

**Step 2: Set up the passwordless SSH Login**

The machines should be able to log in and out of each other without requiring a password. In order for this to work, we perform the following steps - 

1. Create a new user dedicated for running MPI programs. This requires you to have root privileges.

>sudo useradd mpiuser

>passwd mpiuser

>//Enter password as 'password'. These are the standard inputs we will be using on all machines for simplicity's sake.

> //Give this user sudo privileges

>sudo usermod -a -G wheel mpiuser
