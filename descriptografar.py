import os
import pyaes

## abrir o arquivo a ser criptografado
nome_arquivo = "Doc_importante.txt.ransomwaretroll"
arquivo = open(nome_arquivo, "rb")
data_arquivo = arquivo.read()
arquivo.close()

## chave de criptografia com 16 caracteries
chave = b"descriptografara"
aes = pyaes.AESModeOfOperationCTR(chave)
decrypt_data = aes.decrypt(data_arquivo)

## remover o arquivo criptografado
os.remove(nome_arquivo)

## criar o arquivo descriptografado
novo_arquivo = "Doc_importante.txt"
novo_arquivo = open(f'{novo_arquivo}','wb')
novo_arquivo.write(decrypt_data)
novo_arquivo.close()