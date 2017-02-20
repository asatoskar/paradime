# Setting Up A Cluster Using MPI4Py on Fedora 25

This file consolidates all the steps that were taken to set up a working MPI cluster on Fedora 25 using MPICH and MPI4Py based on steps seen in the [Resources](https://github.com/m0usedrag0n/paradime/blob/master/Resources.md).

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

Open /etc/hosts in the text editor of your choice. Here, *nano* is used.

>sudo nano /etc/hosts

Enter all the IP addresses that you noted down in Step 1, along with the hostname assigned to each machine in Step 2 as follows.

>IP-address(tab)hostname(tab)hostname.localdomain

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

4. Now start the required daemons on all the machines

>systemctl start sshd

5. Sign into the client machine using the following command

>ssh clientmachinehostname

It should ask for the password of mpiuser@clientmachinehostname, enter 'password'. You should then be signed into mpiuser@clientmachinehostname. Type exit to exit the session.

6. Copy the keys onto other machine

>ssh-copy-id clientmachinehostname

7. Sign into the client machine using the following command

>ssh clientmachinehostname

It should not ask for the password.

**Step 4: Set up NFS with master as the server and remaining slave computers as clients**

1. Create a directory in the home folder of user *mpiuser*

>sudo mkdir /home/mpiuser/cloud

2. Edit the /etc/exports file to 'export' the folder i.e. make it remotely mountable by other machines

>sudo nano /etc/exports

Add the following lines to the file

>/home/mpiuser/cloud (tab) \*(rw,sync,no_root_squash,no_subtree_check)

3. After editing the file, exit nano and run the following command. (It must be run every time changes are made to the /etc/exports file)

>exportfs -a

4. Create the same directory in all the clients/slaves

>sudo mkdir /home/mpiuser/cloud

5. Run nfs daemons on all machines

>sudo systemctl start rpcbind

>*For clients*

>sudo systemctl start nfs

>*For server*

>sudo systemctl start nfs-server

6. Mount the directory remotely on all clients

>sudo mount -t nfs masterhostname:/home/mpiuser/cloud /home/mpiuser/cloud
The first address is the source address on the master computer. The second path is the destination to mount on the slave computer. Instead of hostname, IP address of master may also be used.

**Step 5: Run MPI programs**

1. Copy all executable files to the shared /home/mpiuser/cloud directory on the master.

2. Create a 'machinefile' and add the IP Addresses of all the slaves to it, each on a new line. This machinefile tells the master exactly which computers to run the processes on.

>sudo nano /home/mpiuser/cloud/machinefile

>*Enter the Ip-addresses of all the slaves, one on each line.*

3. To run a Python program using the MPI4Py library, copy the demo program to /home/mpiusers/cloud and then use the following command.

>mpiexec -n *number of processes* -machinefile /path/to/machinefile python /path/to/demo/program.py

For our system,

>mpiexec -n 4 -machinefile /home/mpiuser/cloud/machinefile python /home/mpiuser/cloud/path/to/demo/helloworld.py

This should run the file as needed.
