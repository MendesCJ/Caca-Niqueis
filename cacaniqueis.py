#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cacaniqueis.py
# 
#  Copyright 2016 Carlos José Mendes <carlos@localhost>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 021110-1301, USA.

'''
Caça níqueis: O jogador faz sua aposta e caso seja sorteado 3 números i-
guais, o número sorteado será multiplicado por 3 e pelo valor da aposta.
Quanto maior o valor da aposta e quanto maior for o número sorteado, mai
ores serão os premios. Apostar 0 interrompe o jogo, que será salvo  caso
o jogador tenha saldo positivo, podendo o jogador voltar a jogar de onde
havia parado. No final será exibida a classificação dos 10 jogadores que
obtiveram as pontuações mais altas.
'''
# Definição de funções

def limpar():
	'''Esta função limpa a tela de jogo para melhor visualização impri-
	mindo linhas em branco'''
	
	print("\n"*130)
	return()

def estatistica():
	'''Esta função gera o arquivo de estatística salvando nele os resul-
	tados obtidos pelo jogador'''
	
	linha=str(nome)+" "+str(aproveitamento)+" "+str(pontos)+"\n"

	try:
		arquivo=open('estatistica.txt','r')
		if linha not in arquivo.readlines():		
			arquivo.writelines(linha)
			arquivo.close()
	except:
		arquivo=open('estatistica.txt','a')
		arquivo.writelines(linha)
		arquivo.close	
	return()
	
def mostraestatistica():
	'''Esta função recupera o arquivo de estatisticas gravado e  imprime
	em tela os 10 primeiros classificados, em ordem de pontuação'''
	
	arquivo=open('estatistica.txt','r')
	linha=""
	coluna=[]

	for i in arquivo.readlines():
		linha=i.split()
		coluna.append((linha[0],float(linha[1]),float(linha[2])))
	coluna.sort(key=lambda x: x[2],reverse=True)
	arquivo.close()
	limpar()
	print("* * * * * * * * * *   C l a s s i f i c a ç ã o   * * * * * * * * * *")
	print
	cont=1
	for i in coluna:
		if cont<=10:
			nome,aproveitamento,pontos=i[0],i[1],i[2]
			print("%2iº - %s \tAproveitamento: %10.3f %% \tPontuação: %10.3f " %(cont,nome,aproveitamento,pontos))
			cont+=1
		else:
			break
	return()
			
def abrirarquivo(nome):
	'''Esta função tenta abrir um arquivo do jogo existente, senão  cria 
	um arquivo novo com valores iniciais padronizados.'''
	   
	nomearquivo=str(nome)+"niquel.txt"

	try:
		arquivo=open(nomearquivo,'r')
		nome=str(arquivo.readline())
		dinheiro=float(arquivo.readline())
		contador=int(arquivo.readline())
		trinca=int(arquivo.readline())
		aproveitamento=float(arquivo.readline())
		pontos=float(arquivo.readline())
		arquivo.close()

	except:
		arquivo=open(nomearquivo,'w')
		arquivo.writelines(str(nome)+"\n")
		arquivo.writelines('500.00\n')
		arquivo.writelines('0\n')
		arquivo.writelines('0\n')
		arquivo.writelines('0.0\n')
		arquivo.writelines('0.0\n')
		arquivo.close()
		dinheiro=500.00
		contador=0
		trinca=0
		aproveitamento=0.0
		pontos=0.0
	
	return(dinheiro,contador,trinca,aproveitamento,pontos) 		   
		
def mostrajogo(): 
	'''Esta função mostra o status do jogo'''

	limpar()
	print("Mensagem: %s" %mensagem)
	try:
		espeak.synth(mensagem)
	except:
		pass
	
	print
	print                               
	print("* * * * * *   C A Ç A    N Í Q U E I S   * * * * * *")
	print
	print("Jogador"+"."*30+":"+"%14s" %nome)
	print("Dinheiro disponível"+"."*18+": R$ %10.2f" %dinheiro)
	print("Valor da sua aposta"+"."*18+": R$ %10.2f" %aposta)
	print("Quantidade de jogadas efetuadas"+"."*6+": %13i" %contador)
	print("Quantidade de acertos"+"."*16+": %13i" %trinca)
	print("Aproveitamento"+"."*23+":    %10.2f %%" %aproveitamento)
	print("Pontuação"+"."*28+":    %10.2f" %pontos)
	print
	print(" "*11+"* * * Display da maquina * * *")
	print
	print(" "*22+"%s" %str(jogada))
	print
	print("................ Aposte 0 para sair ................")
	
	return()

def detectavenc():
	'''#Esta função detecta se a jogada foi vencedora e retorna a quan-
	tidade de pontos recebida'''
	
	resultado=0

	if jogada[0]==jogada[1] and jogada[1]==jogada[2]:
		resultado=jogada[0]*3
		if resultado==0:
			resultado=30
	
	return(resultado)

def apostar():
	'''Esta função solicita um valor de aposta'''

	try:
		aposta=float(input("Faça sua aposta! "))				
	except:
		aposta=-1.0
	return(aposta)

def gerarjogada():
	'''Esta função gera numeros aleatóreos para o display'''

	from random import randint #Gerar numeros aleatóreos inteiros
	jogada=[randint(0,9), randint(0,9), randint(0,9)]
	return(jogada)
			
def salvajogo():
	'''Esta função salva o jogo atual para que o jogador possa continuar 
	jogando posteriormente'''		

	nomearquivo=str(nome)+"niquel.txt"
	arquivo=open(nomearquivo,"w")
	arquivo.writelines(str(nome)+"\n")
	arquivo.writelines(str(dinheiro)+"\n")
	arquivo.writelines(str(contador)+"\n")
	arquivo.writelines(str(trinca)+"\n")
	arquivo.writelines(str(aproveitamento)+"\n")
	arquivo.writelines(str(pontos)+"\n")
	arquivo.close()

''' Corpo principal do programa '''

try:	
	from espeak import espeak
	espeak.set_voice("pt")
	mensagem="Bem vindo ao jogo de caça níqueis. Digite o seu nome:"
	espeak.synth(mensagem)
except:
	pass
	
from time import sleep

# Declaração de variáveis
nome=""
mensagem="Seja bem vindo "
jogada=[0,0,0]
aposta=0.0
dinheiro=0.0
contador=0
trinca=0
aproveitamento=0.0
pontos=0.0
	
try:
	nome=input("Digite seu primeiro nome: ")
except:
	nome=str(raw_input("Digite seu primeiro nome: "))
	
mensagem="Seja bem vindo "+nome+", faça suas apostas e boa sorte!!"
dinheiro, contador, trinca, aproveitamento, pontos = abrirarquivo(nome)

while dinheiro>0:
	mostrajogo()
	aposta=apostar()
	if aposta<=dinheiro:
		if aposta<0:
			mensagem="Por favor, apenas números maiores ou iguais a 0. Utilize o ponto caso queira separar os centavos"
			aposta=0
		elif aposta==0:
			mensagem="Encerrando o jogo! Seu saldo será salvo e você poderá continuar jogando. Volte sempre!"
			salvajogo()
			mostrajogo()
			sleep(7)
			estatistica()
			mostraestatistica()
			break
		else:
			jogada=gerarjogada()
			contador+=1
			dinheiro-=aposta
			aproveitamento=100*(trinca/float(contador))
			resultado=detectavenc()
			if resultado>1:
				mensagem="Parabéns, você ganhou! O valor da sua aposta será multiplicado pela soma dos números da trinca"
				dinheiro+=aposta*resultado
				trinca+=1
				pontos+=((trinca/float(contador))*100.0)*resultado
			else:
				mensagem="Você não acertou, tente novamente!"	
	else:
		mensagem="Você não pode apostar mais do que tem!"	
		salvajogo()

if aposta!=0:
	mensagem="Fim de jogo! Seu dinheiro acabou!"
	mostrajogo()
	sleep(5)
	estatistica()
	mostraestatistica()
	dinheiro=500.00
	contador=0
	trinca=0
	aproveitamento=0.0
	pontos=0.0	
	salvajogo()	
