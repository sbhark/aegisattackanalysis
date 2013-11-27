# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.provision :shell, :path => "installation/aegis_dependency_install.sh"
  config.vm.synced_folder ".", "/root"

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "ubuntu_aegis_test"

  # The url from where the 'config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"

  config.vm.network :forwarded_port, guest: 22, host: 2201

  config.vm.provider :virtualbox do |vb| 
    vb.customize ["modifyvm", :id, "--memory", 1024]
  end
end
