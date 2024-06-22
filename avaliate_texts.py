import char_lib as clib

def compara_assinatura(a,b):
    #IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) + abs(a[3]-b[3]) + abs(a[4]-b[4]) + abs(a[5]-b[5])
    similaridade = soma/6
    return similaridade

def calcula_assinatura(texto):
  #'''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
  #separandotudo
  lista_de_frases = []
  lista_de_palavras = []
  sentencas = clib.separa_sentencas(texto)
  for sent in sentencas:
    novas_frases = clib.separa_frases(sent)
    lista_de_frases.extend(novas_frases)
  for fr in lista_de_frases:
    novas_palavras = clib.separa_palavras(fr)
    lista_de_palavras.extend(novas_palavras)

  #funçãoparatamanhosmedios
  def tamanho_medio(lista):
    tamanhos=[]
    for t in lista:
      n= len(t)
      tamanhos.append(n)
    tamanhototal = 0
    for f in tamanhos:
      tamanhototal = tamanhototal+f 
    media = tamanhototal/len(lista)
    return media

  #tamanhomediodepalavras    
  wal = float(tamanho_medio(lista_de_palavras))
  #RelaçãoType-Token 
  ttr = float(clib.n_palavras_diferentes(lista_de_palavras)/len(lista_de_palavras))
  #Razão Hapax Legomana
  htr = float(clib.n_palavras_unicas(lista_de_palavras)/len(lista_de_palavras))
  #Tamanho médio de sentenças
  sal = float(tamanho_medio(sentencas))
  #Complexidade de sentença
  sac =  float(len(lista_de_frases)/len(sentencas))
  #Tamanho médio de frase
  pal = float(tamanho_medio(lista_de_frases))

  as_b = [wal, ttr, htr, sal, sac, pal]
  return as_b 


def avalia_textos(textos, ass_cp):
    #'''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_de_assinaturas = []
    for texto in textos:
      as_b =  calcula_assinatura(texto)
      s = compara_assinatura(as_b, ass_cp)
      lista_de_assinaturas.append(s)
    r = lista_de_assinaturas.index(min(lista_de_assinaturas)) + 1 
    return r 

def main():
  ass_cp = clib.le_assinatura()
  textos = clib.le_textos()
  resposta = avalia_textos(textos, ass_cp)
  print("O autor do texto", resposta, "está infectado com COH-PIAH") 

if (__name__) == '__main__':
  main()

main()