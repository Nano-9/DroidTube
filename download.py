# A pedido, fiz esse script bem mais simples!
# Esse é uma versão ligth do E-Tube original
# Essa versão é básica e feita para rodar no Android!
# Versão requisitada do python: 3.10 +
# Coded by: Nano

import sys
import re
import requests
import pytube
from pytube import YouTube
from pytube import Playlist
from time import sleep

class CheckInternetUsuario:

	# checka se o usuário está com conexão a internet
	# classe que chama outra

	def __init__(self,options,link):

		self.options = options
		self.link = link
		self.online = False
		self.connectWeb = requests.Session()
		self.headersWeb = {'User-Agent':'"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.10) Gecko/20160408 Firefox/40.1.10"'}

	def VerificacaoInternet(self):

		match self.options:
			case "-v":
				try:
					self.connectTest = self.connectWeb.get("https://www.google.com.br/",headers=self.headersWeb)
				except KeyboardInterrupt:
					print("\n\033[1;31m[!]\033[m \033[1mSaindo...\033[m\n")
					sys.exit()
				except:
					print("\n\033[1;31m[!]\033[m \033[1mVocê não tem conexão com a internet!\033[m\n")
				else:
					match self.connectTest.status_code:

						case 200:
							self.online = True
							Checar = VerificaLinkUsuario(userurl=self.link,online=self.online,optionPlay=False,optionVideo=True)
							Checar.VerificacaoUrl()
						case _:
							self.online = False
			case "-p":
				try:
					self.conectTest = self.connectWeb.get("https://www.google.com/",headers=self.headersWeb)
				except KeyboardInterrupt:
					print("\n\033[1;31m[!]\033[m \033[1mSaindo...\033[m\n")
				except:
					print("\n\033[1;31m[!]\033[m \033[1mVocê não tem conexão com a internet!\033[m\n")
				else:
					match self.conectTest.status_code:
						case 200:
							self.online = True
							checarPlaylist = VerificaLinkUsuario(userurl=self.link,online=self.online,optionPlay=True,optionVideo=False)
							checarPlaylist.VerificacaoUrl()
						case _:
							self.online = False
class VerificaLinkUsuario:


	# classe que verifica o link do usuário utilizando Regex
	# se válido, autoria o download do vídeo chamando a classe Download

	def __init__(self,userurl,online,optionPlay,optionVideo):

		self.optionPlay = optionPlay
		self.optionVideo = optionVideo
		self.userurl = userurl
		self.online = online

	def VerificacaoUrl(self):

		match self.online:
			case True:
				self.check = re.search(r"^(https://){1}(?:(www\.)?)(youtu\.be/|youtube\.com/)((watch|playlist)?)[a-zA-Z0-9]+\?[a-zA-Z0-9]{1,4}\=[a-zA-Z0-9_\-]{11,34}$",self.userurl)

				if self.check:
					if self.optionVideo:

						DownloadVideo = DownloadYouTube(PlayList=self.optionPlay,Video=self.optionVideo,LinkTube=self.userurl)
						DownloadVideo.BaixarVideo()
					elif self.optionPlay:
						DownloadVideo = DownloadYouTube(PlayList=self.optionPlay,Video=self.optionVideo,LinkTube=self.userurl)
						DownloadVideo.BaixarPlaylist()
				else:
					print("[!] Url Inválida!\n")
			case False:
				print("[!] Você não está conectado na internet!\n")



class DownloadYouTube:

	# classe responsável por fazer o download do vídeo ou playlist do usuário
	# só é executada se caso as outras duas forem

	def __init__(self,PlayList,Video,LinkTube):

		self.PlayList = PlayList
		self.Video = Video
		self.LinkTube = LinkTube

	def BaixarVideo(self):

		self.youtube = YouTube(self.LinkTube)
		self.streams = self.youtube.streams.filter(progressive=True,file_extension="mp4")
		self.nome = self.youtube.title
		print("\033[1;32m[+]\033[m \033[1mBaixando o vídeo...\033[m")
		self.video = self.streams.get_highest_resolution()
		self.video.download(output_path="VÍDEOS")
		print("\033[1;32m[+]\033[m \033[1mVídeo ( {} ) baixado!\033[m\n".format(self.nome))

	def BaixarPlaylist(self):

		playYT = Playlist(self.LinkTube)
		tamanho = []
		for video in playYT:
			tamanho.append(video)
		match len(tamanho):
			case 1:
				print("Playlist contém {} vídeo!".format(len(tamanho)))
			case _:
				print("Playlist contém {} vídeos!".format(len(tamanho)))
		# start download

		for posicao,videos in enumerate(tamanho):
			download = YouTube(videos)
			bestResolution = download.streams.get_highest_resolution()
			print("\033[1;36m[*]\033[m \033[1mBaixando vídeo {}: {}\033[m".format(posicao+1,download.title))
			try:
				bestResolution.download(output_path="PLAYLIST")
			except:
				print("\033[1;31m[!]\033[m \033[1mInformações incompletas sobre o vídeo!\033[m")
				print("\033[1;31m[!]\033[m \033[1mPulando..\033[m")
			else:
				print("\033[1;32m[*]\033[m \033[1mCompleto!\033[m")
