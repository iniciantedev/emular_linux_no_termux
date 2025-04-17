#instalando repositorio
#(para maior compatibilidade com termux antigo)
apt install x11-repo

#instalando dependencias
apt install -y \
qemu-system-x86-64-headless \
qemu-utils \
python3 \
openssl

if [ $? != 0 ]; then
echo "sucesso, digite python emular.py --help"
else
echo "failed! exit code: $?!"
fi
