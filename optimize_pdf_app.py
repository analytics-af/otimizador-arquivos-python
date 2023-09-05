import os
import subprocess
import tkinter as tk
from tkinter import filedialog


def optimize_pdf(input_pdf_path, output_pdf_path):
    gs_command = [
        "C:\\Program Files\\gs\\gs10.01.1\\bin\\gswin64c.exe",
        '-sDEVICE=pdfwrite',
        '-dCompatibilityLevel=1.5',
        '-dPDFSETTINGS=/ebook', #TROCAR PARA /screen PARA FICAR MAIS LEVE OU /ebook PARA RESOLUCAO MELHOR
        '-dNOPAUSE',
        '-dBATCH',
        f'-sOutputFile={output_pdf_path}',
        input_pdf_path,
    ]
    subprocess.run(gs_command, check=True)


def optimize_pdf_directory(pdf_directory):
    for pdf_file in os.listdir(pdf_directory):
        if pdf_file.endswith('.pdf'):
            input_pdf_path = os.path.join(pdf_directory, pdf_file)
            temp_output_pdf_path = os.path.join(pdf_directory, 'temp_optimized_' + pdf_file)

            optimize_pdf(input_pdf_path, temp_output_pdf_path)

            os.replace(temp_output_pdf_path, input_pdf_path)
            print(f"Arquivo otimizado substituiu o arquivo original: {input_pdf_path}")


def browse_directory():
    directory = filedialog.askdirectory()
    optimize_pdf_directory(directory)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    browse_directory()
