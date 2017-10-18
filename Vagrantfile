# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network :forwarded_port, guest: 80, host: 8080
  # config.vm.provision "shell", path: "add_variables.sh", privileged: false
  config.vm.provision "shell", path: "setup.sh"
  config.vm.synced_folder '.', '/vagrant', disabled: true
  config.vm.synced_folder “../“, “/mangarso.com”, id: "vagrant-root",
    owner: "vagrant",
    group: "www-data",
    mount_options: ["dmode=775,fmode=764"]
end