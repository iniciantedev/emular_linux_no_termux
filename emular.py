import sys
import urllib.request
import subprocess
import os

def distros():
	print("distros:\n")
	print("alpine linux -> alpine")

def help():
	print("-d [distro] para emular uma distro linux.")
	print("--help para pedir ajuda.")
	print("--list para listar as distros")
	print("--run-distro para rodar uma distro")

def emule():
	if len(sys.argv) < 3:
		print('falha! digite "python emular.py --help" para obter instruções')
		exit()
	match sys.argv[2]:
		case "alpine":
			print("instalando alpine.iso..")
			request("https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-virt-3.21.3-x86_64.iso", "alpine.iso")
			subprocess.run(["qemu-img", "create", "-f", "qcow2", "alpine.qcow2", "5G"])
			print("instalação concluida!")
		case _:
			print('falha! digite "python emular.py --help" para obter instruções')

def run():
	if os.path.isfile("./" + sys.argv[2] + ".iso") and os.path.isfile("./" + sys.argv[2] + ".qcow2"):
		print("seu programa foi linux será aberto em localhost:1")
		subprocess.run([
			"qemu-system-x86_64",
			"-hda", "./" + sys.argv[2] + ".qcow2",
			"-m", "512",
			"-cdrom", "./" + sys.argv[2] + ".iso",
			"-nic", "none",
			"-netdev", "user,id=a",
			"-device", "e1000,netdev=a",
			"-vnc", ":1"
])
def request(site, arquivo_destino):
    with urllib.request.urlopen(site) as resposta:
        with open(arquivo_destino, "wb") as f:
            bloco = True
            while bloco:
                bloco = resposta.read(1024)
                f.write(bloco)

if len(sys.argv) < 2:
	print('falha! digite "python emular.py --help" para obter instruções')
	sys.exit()

match sys.argv[1]:
	case "--help":
		help()
	case "-d":
		emule()
	case "--list":
		distros()
	case "--run-distro":
		run()
	case _:
		print('falha! digite "python emular.py --help" para obter instruções')

