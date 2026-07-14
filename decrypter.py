import os
import pyaes
import glob

#Itera em todos os arquivos .txt da pasta
for nome in glob.glob('*.txt.ransowaretroll'):
    with open(f'{nome}', "rb") as f:
        conteudo = f.read()

    #Gera uma chave de criptoggrafia
    key = b"#]>[rNBIoe0R28h@"
    aes = pyaes.AESModeOfOperationCTR(key)
    descriptografArquivo = aes.decrypt(conteudo)

    #Gera um novo arquivo criptografado com o mesmo nome porém além da extensão .txt é acompanhado da extensão do ransoware
    novoArquivo = nome.split('.ransowaretroll')[0]
    novoArquivo = open(f'{novoArquivo}', 'wb')
    novoArquivo.write(descriptografArquivo)
    novoArquivo.close()

    #Remove o arquivo depois de abrir e coletar todo o conteúdo
    os.remove(nome)
