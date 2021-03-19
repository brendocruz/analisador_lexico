import re

class Token():
	def __init__(self, _id, valor):
		self.id = _id
		self.valor = valor

class Numero():
	def __init__(self, _id, valor):
		Token.__init__(self, _id, valor)

class Operador():
	def __init__(self, _id, valor):
		Token.__init__(self, _id, valor)

class Pontuacao():
	def __init__(self, _id, valor):
		Token.__init__(self, _id, valor)

def isNumero(string):
	numeros = re.compile(r'[0-9]+')
	if numeros.match(string):
		return True
	return False

def isOperador(string):
	operadores = re.compile(r'(\+|\-|\/|\*{1,2})')
	if operadores.match(string):
		return True
	return False

def isPontuacao(string):
	pontuacao = re.compile(r'(\(|\))')
	if pontuacao.match(string):
		return True
	return False

class AnalisadorLexico():
	def __init__(self):
		self.tokens = []

	def analisar(self):
		arquivo = open('test.txt', 'tr')
		dados = arquivo.read()
		linhas = dados.splitlines()
		arquivo.close()

		ltokens = []
		for linha in linhas:
			if linha.startswith('@'):
				continue
			ltokens.append(linha.split())

		id_atual = 0
		for linha in ltokens:
			for token in linha:
				if isNumero(token):
					self.tokens.append(Numero(id_atual, token))
				elif isOperador(token):
					self.tokens.append(Operador(id_atual, token))
				elif isPontuacao(token):
					self.tokens.append(Pontuacao(id_atual, token))
				id_atual += 1

	def salvar_arquivo(self):
		linhas = []
		for token in self.tokens:
			linhas.append('{},{},{}\n'.format(token.id, type(token).__name__, token.valor))
		arquivo = open('output.txt', 'tw')
		arquivo.writelines(linhas)
		arquivo.close()

if __name__ == '__main__':
	ana = AnalisadorLexico()
	ana.analisar()
	ana.salvar_arquivo()
	pass
