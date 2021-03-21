from token import *
import re
import time

class AnalisadorLexico():
	def __init__(self, nome_arquivo):
		self.nome_arquivo = nome_arquivo
		self.tokens = []

	def abrir_arquivo(self):
		try:
			arquivo = open(self.nome_arquivo, 'tr')
		except FileNotFoundError as expection:
			print('Arquivo não encontrado.')
			exit()
		else:
			return arquivo

	def analisar(self):
		arquivo = self.abrir_arquivo()
		dados = arquivo.read()
		linhas = dados.splitlines()
		arquivo.close()

		ltokens = []
		for linha in linhas:
			if linha.startswith('@'):
				continue
			partes = linha.split()
			for token in partes:
				token_partes = Pontuacao.dividir_pontuacao(token)
				ltokens.extend(token_partes)


		id_atual = 0
		for token in ltokens:
			if Numero.isNumero(token):
				self.tokens.append(Numero(id_atual, token))
			elif Operador.isOperador(token):
				self.tokens.append(Operador(id_atual, token))
			elif Pontuacao.isPontuacao(token):
				self.tokens.append(Pontuacao(id_atual, token))
			id_atual += 1


	def salvar_arquivo(self):
		linhas = []
		for token in self.tokens:
			linhas.append('{},{},{}\n'.format(token.id, type(token).__name__, token.valor))
		arquivo = open('output.txt', 'tw')
		arquivo.writelines(linhas)
		arquivo.close()

def main():
	print('# Analisador Lexico'.upper())
	print('Escreva abaixo o nome do arquivo que deseja analisar.')
	print('O nome padrão para arquivo é output.txt')
	print('Se não desejar mante-lo, aperte ENTER.')
	
	nome_arquivo = input(">> ")
	if nome_arquivo == '':
			nome_arquivo = 'input.txt'
	
	analisador = AnalisadorLexico(nome_arquivo)
	analisador.analisar()
	analisador.salvar_arquivo()
	print('Arquivo analisado e salvo no arquivo output.txt')

if __name__ == '__main__':
	main()
	time.sleep(2)
