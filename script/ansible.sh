sudo apt-get update
sudo apt-get install python3 -y
mkdir -p ~/.local/bin
echo 'PATH=$PATH:#/.local/bin' >> ~/.bashrc
. ~/.bashrc
pip3 install --user ansible

ansible-playbook -v -i inventory playbook.yaml
