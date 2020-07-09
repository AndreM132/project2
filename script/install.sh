.~/.bashrc

sudo apt update -y
sudo apt-get install containerd.io
sudo install docker.io -y
sudo apt install docker-compose -y
sudo systemctl start docker
sudo systemctl enable docker
sudo systemctl status docker
sudo usermod -aG docker $USER
