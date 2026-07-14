# Desafio-Ransoware-Dio
Demonstração de um ransoware aplicado a todos os arquivos .txt da pasta atual

## Ferramentas
* Python

## Bibliotecas
* os
* glob
* pyaes

## Funcionamento do Script de Criptografia
O script começa iterando todos os arquivos num for na lista de todos os nomes com a extensão especificada a função glob da biblioteca glob, ler os conteúdos de arquivo e guarda, remove os arquivos .txt, em seguida é gerado uma cifra de criptografia com a chave aplicada a função AESModeOfOperationCTR e após isso criptografa cada arquivo com ela, por fim gera um novo nome adicionado no final da extensão .ransowaretroll <br>

<img width="1229" height="560" alt="image" src="https://github.com/user-attachments/assets/b8810e63-92e5-427d-bd50-38b34a1b2519" />
<br> Captura de tela do código do algoritmo encrypter.py <br>

<br>
<br>

<img width="1825" height="466" alt="image" src="https://github.com/user-attachments/assets/153bcb09-7cfe-4656-9a8e-1b4c3ff18437" />
<br> Captura de tela dos arquivos de textos teste legivéis <br>

<br>
<br>

<img width="790" height="134" alt="image" src="https://github.com/user-attachments/assets/3f26829a-8422-4e2b-97a7-0f3581b97912" />
<br> Captura de tela do nome do arquivo após a execução do script de criptografia <br>

<br>
<br>

<img width="1877" height="481" alt="image" src="https://github.com/user-attachments/assets/1eaf6178-9ef4-458d-96b4-0952586d1fdc" />
<br> Captura de tela dos arquivos criptografados <br>

<br>
<br>

## Funcionamento do Script de Criptografia
O script de descriptografia tem o funcionamento semelhante, ele utiliza um for numa lista gerada pela função glob pesquisando por arquivos com a extensão .txt.ransowaretroll, ler o conteúdo de cada arquivo, usa uma chave para gerar uma cifra para descriptografar e depois gera um novo arquivo removendo a extensão .ransoware e com o conteúdo descriptografado e legível

<img width="797" height="561" alt="image" src="https://github.com/user-attachments/assets/299dc4b7-4ae6-42d6-9e09-5bf9bfc85daa" />
Captura de tela do script descrypter.py
