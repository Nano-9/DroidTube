import os
import sys
import requests
from pytube import YouTube
from pytube import Playlist
from download import CheckInternetUsuario

os.system("clear")

class GetLinkUser:

	def __init__(self,optionss,linkss):

		self.optionss = optionss
		self.links = linkss

	def ConfigureDownload(self):

		self.validacao = CheckInternetUsuario(options=self.optionss,link=self.links)
		self.resultado = self.validacao.VerificacaoInternet()


if __name__ == "__main__":

	versao = sys.version
	if len(sys.argv) == 3:
		if versao[0:4].replace(".","") >"310":
			if sys.argv[1] == "-v":
				download = GetLinkUser(optionss=sys.argv[1],linkss=sys.argv[2])
				download.ConfigureDownload()
			elif sys.argv[1] == "-p":
				download = GetLinkUser(optionss=sys.argv[1],linkss=sys.argv[2])
				download.ConfigureDownload()
			else:
				print("digite -h para ver as opções!")
		else:
			print("A versão do seu Python não é compatível!\nPois a estrutura usada aqui,\nnão foi implementada na versão do seu python!")
			sys.exit()

	elif len(sys.argv) == 2:
		if sys.argv[1] == "-h":
			print("python3 -v link [ Para baixar um vídeo ]")
			print("python3 -p link [ Para baixar uma playlist ]")
			sys.exit()
		else:
			print("digite -h para ver as opções!")

	else:
		print("digite -h para ver as opções!")
		sys.exit()
