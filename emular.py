import sys
import urllib.request
import subprocess
import os

url = {
"linux": {
"alpine": "https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/x86_64/alpine-virt-3.21.3-x86_64.iso",
"tinycore": "http://www.tinycorelinux.net/16.x/x86/release/TinyCore-current.iso",
"slitaz": "http://mirror.slitaz.org/iso/rolling/slitaz-rolling.iso"
}
}

def distros():
	print("distros:\n")
	print("alpine linux -> alpine")
	print("slitaz -> slitaz")
	print("tinycorelinux -> tinycore")

def help():
	print("-d [distro] para instalar uma distro linux.")
	print("--help para pedir ajuda.")
	print("--list para listar as distros")
	print("--run-distro [distro] [forma de boot] ex: disk/cdrom para rodar uma distro")

def emule():
	if len(sys.argv) < 3 or sys.argv[2] not in url["linux"]:
		print('falha! digite "python emular.py --help" para obter instruções')
		exit()
	print("instalando " + sys.argv[2] + ".iso..")
	request(url["linux"][sys.argv[2]], sys.argv[2] + ".iso")
	subprocess.run(["qemu-img", "create", "-f", "qcow2", sys.argv[2] + ".qcow2", "5G"])
	print("instalação concluida!")

def run():
	if len(sys.argv) < 4:
		print('falha! digite "python emular.py --help" para obter instruções')
		exit()
	if os.path.isfile("./" + sys.argv[2] + ".iso") and os.path.isfile("./" + sys.argv[2] + ".qcow2"):
		print("seu programa foi linux será aberto em localhost:1")
		if sys.argv[3] == "cdrom":
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
		elif sys.argv[3] == "disk":
			subprocess.run([
                                "qemu-system-x86_64",
                                "-hda", "./" + sys.argv[2] + ".qcow2",
                                "-m", "512",
                                "-nic", "none",
                                "-netdev", "user,id=a",
                                "-device", "e1000,netdev=a",
                                "-vnc", ":1"
				])
		else:
			print('falha! digite "python emular.py --help" para obter instruções')
	else:
		print('falha! digite "python emular.py --help" para obter instruções')
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

