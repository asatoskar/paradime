# Setting Up A Cluster Using MPI4Py on Fedora 25

This file consolidates all the steps that were taken to set up a working MPI cluster on Fedora 25 using MPICH and MPI4Py based on steps seen in the [Resources](paradime/Resources.md).

**Step 1: Install the packages required for the setup on all machines.**

>sudo dnf install python-devel mpich-devel mpich-autoload python-mpi4py

*Note: Assuming openssh and nfs-utils are installed. Else, install those packages as well.*

**Step 2: Configure the /etc/hosts file on every machine**

1. Enter the following command on each machine to find the IP-address for your desired interface

>ip-address

Note down these IP addresses as they need to be added in the /etc/hosts file along with the hostname.

2. Change your default hostname.

To change the defalt hostname, open /etc/hostname in the text editor of your choice. Here, *nano* is used.

>sudo nano /etc/hostname

Add the following lines to the file

>yourhostname.localdomain

Where yourhostname will be the name you want to give the machine. Log out and log in again for the change to take effect.

2. Configure /etc/hosts file

Open /etc/hosts in the text editor of your choice. Here, nano is used.

>sudo nano /etc/hosts

Enter all the IP addresses that you noted down in Step 1, along with the hostname assigned to each machine in Step 2 as follows.

>IP-address<tab>hostname<tab>hostname.localdomain

**Step 3: Set up the passwordless SSH Login**

The machines should be able to log in and out of each other without requiring a password. In order for this to work, we perform the following steps - 

1. Create a new user dedicated for running MPI programs. This requires you to have root privileges.

>sudo useradd mpiuser

>passwd mpiuser

>*//Enter password as 'password'. These are the standard inputs we will be using on all machines for simplicity's sake.*

> *//Give this user sudo privileges*

>sudo usermod -a -G wheel mpiuser

2. Change to that user

>su - mpiuser

3. Generate the SSH keys

> ssh-keygeyn -t rsa

> *//For easier setup, just press enter when prompted for a passphrase and file in which to save keys.*

4. Copy the keys onto other machine

>ssh-copy-id clientmachine
