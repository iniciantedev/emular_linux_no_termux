#instalando repositorio

install_package() {
if dpkg -l | grep  -q "$1"; then
echo -e "$1: \033[32mOK\033[0m"
else
pkg install -y $1 > /dev/null 2>/dev/null
if [ $? -ne 0 ]; then
echo -e "$1: \033[31mERROR\033[0m"
else
echo -e "$1: \033[32mOK\033[0m"
fi
fi
}

install_package x11-repo

#instalando dependencias
install_package qemu-system-x86-64-headless
install_package qemu-utils
install_package python
install_package openssl

echo "Digite python emular.py --help para mais instruções."
