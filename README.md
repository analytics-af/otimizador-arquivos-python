# Otimizador de Arquivos PDF
##Descrição
Este projeto é um otimizador de arquivos PDF que utiliza o Ghostscript para reduzir o tamanho dos arquivos PDF em um diretório especificado. O script é escrito em Python e usa a biblioteca Tkinter para a interface gráfica.

##Requisitos
Python 3.x
Ghostscript 10.01.1 ou superior

##Como usar
Clone o repositório ou baixe o arquivo main.py.
Instale o Ghostscript e certifique-se de que o caminho do executável esteja correto no script.
Execute o script.
Uma janela de diálogo será aberta. Selecione o diretório que contém os arquivos PDF que você deseja otimizar.

##Funcionalidades
optimize_pdf(input_pdf_path, output_pdf_path)
Esta função otimiza um único arquivo PDF. Ela recebe o caminho do arquivo PDF de entrada e o caminho onde o arquivo PDF otimizado será salvo.

##optimize_pdf_directory(pdf_directory)
Esta função percorre todos os arquivos PDF em um diretório especificado e os otimiza.

##browse_directory()
Esta função abre uma janela de diálogo que permite ao usuário selecionar um diretório para otimizar todos os arquivos PDF contidos nele.

##Configurações
Você pode alterar as configurações de otimização modificando a linha -dPDFSETTINGS=/ebook no comando Ghostscript dentro da função optimize_pdf. As opções disponíveis são:

/screen: para arquivos mais leves
/ebook: para melhor resolução

##Contribuições
Sinta-se à vontade para contribuir com melhorias e correções de bugs.
