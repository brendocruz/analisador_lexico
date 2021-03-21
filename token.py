import re

class Token():
	def __init__(self, _id, valor):
		self.id = _id
		self.valor = valor

class Numero():
	def __init__(self, _id, valor):
		Token.__init__(self, _id, valor)

	def isNumero(string):
		numeros = re.compile(r'[0-9]+')
		if numeros.match(string):
			return True
		return False
	isNumero = staticmethod(isNumero)

class Operador():
	def __init__(self, _id, valor):
		Token.__init__(self, _id, valor)

	def isOperador(string):
		operadores = re.compile(r'(\+|\-|\/|\*{1,2})')
		if operadores.match(string):
			return True
		return False
	isOperador = staticmethod(isOperador)

class Pontuacao():
	pontuacoes = (r'\(', r'\)')

	def __init__(self, _id, valor):
		Token.__init__(self, _id, valor)

	def isPontuacao(string):
		pontuacao = re.compile(r'(\(|\))')
		if pontuacao.match(string):
			return True
		return False
	isPontuacao = staticmethod(isPontuacao)

	def dividir_pontuacao(token):
		partes_token = []
		for pontuacao in Pontuacao.pontuacoes:
			padrao = re.compile(pontuacao)
			correspondecia = padrao.search(token)
			if correspondecia is not None:
				if correspondecia.end() != len(token):
					partes_token.append(token[correspondecia.start():correspondecia.end()])
					partes_token.append(token[correspondecia.end():])
				else:
					partes_token.append(token[0:correspondecia.start()])
					partes_token.append(token[correspondecia.start():correspondecia.end()])
				break
		else:
			partes_token.append(token)
		return partes_token
	dividir_pontuacao = staticmethod(dividir_pontuacao)