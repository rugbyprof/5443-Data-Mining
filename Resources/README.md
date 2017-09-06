## Getting Started 

### Mac

`sudo pip install -U numpy scipy matplotlib pandas ipython `

### Ubuntu

`sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas`

### Windows
- Use a virtual machine with ubuntu
- Or use Anaconda

### Source of Free Background Video
- Author: https://github.com/lazyprogrammer/ 
- Video: https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python/


### Vagrant

### Windows
- Download Vagrant
- Download Virtualbox
- https://www.sitepoint.com/getting-started-vagrant-windows/

```sh

Vagrant.configure("2") do |vb|
  vb.vm.box = "ubuntu/xenial64"
  vb.gui = true
  vb.name = "my_vm"
  vb.memory = 1024
  vb.cpus = 2
  vb.vm.provision "shell", path: "https://gist.githubusercontent.com/rugbyprof/89601581a9e167be315abc7b3ea28fa9/raw/15c9798b1fe81e95ac5866b32eb18c274532a4d4/ml_ubuntu_setup.sh"
  
end
