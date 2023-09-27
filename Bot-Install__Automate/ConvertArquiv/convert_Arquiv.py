import os
import win32com.client as win32

def convertArqv_WordTOPdf(arquivo_doc, pasta_saida):
    # Obtenha o nome do arquivo sem extensão
    nome_base = os.path.splitext(os.path.basename(arquivo_doc))[0]

    # Defina o caminho completo para o arquivo PDF de saída na pasta de saída
    arquivo_pdf = os.path.join(pasta_saida, f"{nome_base}.pdf")

    word = win32.Dispatch("Word.Application")
    doc = word.Documents.Open(arquivo_doc)
    doc.SaveAs(arquivo_pdf, FileFormat=17)  # 17 é o código para PDF
    doc.Close()
    word.Quit()


if __name__ == "__main__":
    arquivo_doc = "seuarquivo.docx"  # Substitua pelo nome do seu arquivo DOC
    pasta_saida = "caminho/para/sua/pasta"  # Substitua pelo caminho da pasta de saída

    convertArqv_WordTOPdf(arquivo_doc, pasta_saida)