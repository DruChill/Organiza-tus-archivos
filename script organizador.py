from PIL import Image
import os
from tkinter import messagebox as MessageBox


rutaActual = os.path.dirname(os.path.abspath(__file__))

def formatRuta(ruta):
    clean = ''
    for caracter in ruta:
        if caracter == '\\':
            clean = clean + '/'
        else:
            clean = clean + caracter

    return clean



downloadsFolder = formatRuta(rutaActual) + '/'
#  se organizaran los archivos donde ejecutes este script

organized_files = downloadsFolder + '/ArchivosOrganizados'
organized_filesImages = downloadsFolder + '/ArchivosOrganizados/ImagenesDescargadas'
organized_filesAudios = downloadsFolder + '/ArchivosOrganizados/AudiosDescargados'
organized_filesVideos = downloadsFolder + '/ArchivosOrganizados/VideosDescargados'
organized_filesPoint = downloadsFolder + '/ArchivosOrganizados/PowerPointDescargados'
organized_filesExe = downloadsFolder + '/ArchivosOrganizados/ProgramasDescargados'
organized_filesRar = downloadsFolder + '/ArchivosOrganizados/RARdescargados'
organized_filesWord = downloadsFolder + '/ArchivosOrganizados/WordDescargados'
organized_filesTxt = downloadsFolder + '/ArchivosOrganizados/ArchivosTxt'
organized_filesPdf = downloadsFolder + '/ArchivosOrganizados/PDFDescargados'

os.mkdir(organized_files)
os.mkdir(organized_filesImages)
os.mkdir(organized_filesAudios)
os.mkdir(organized_filesVideos)
os.mkdir(organized_filesPoint)
os.mkdir(organized_filesExe)
os.mkdir(organized_filesRar)
os.mkdir(organized_filesWord)
os.mkdir(organized_filesTxt)
os.mkdir(organized_filesPdf)


if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png", ".gif", ".HEIC"]:
            os.rename(downloadsFolder + filename, organized_filesImages + '/' + filename)

        if extension in [".mp3", ".flac", ".wap", ".aif"]:
            os.rename(downloadsFolder + filename, organized_filesAudios + '/' + filename)

        if extension in [".mp4", ".mov", ".mpg", ".wmv", ".rm"]:
            os.rename(downloadsFolder + filename, organized_filesVideos + '/' + filename)

        if extension in [".pptx"]:
            os.rename(downloadsFolder + filename, organized_filesPoint + '/' + filename)

        if extension in [".exe"]:
            os.rename(downloadsFolder + filename, organized_filesExe + '/' + filename)

        if extension in [".rar", ".zip", ".cab", ".arj", ".lzh", ".tar", ".gz", ".ace", ".uue", "bz2", ".jar", ".iso", ".z", ".7z"]:
            os.rename(downloadsFolder + filename, organized_filesRar + '/' + filename)

        if extension in [".docx"]:
            os.rename(downloadsFolder + filename, organized_filesWord + '/' + filename)

        if extension in [".txt", ".psd", ".apk", ".vdf", ".rtf"]:
            os.rename(downloadsFolder + filename, organized_filesTxt + '/' + filename)

        if extension in [".pdf"]:
            os.rename(downloadsFolder + filename, organized_filesPdf + '/' + filename)



MessageBox.showwarning("Alerta",
    "Tus archivos estan organizados valio la pena verdad?.")
    #Puedes personalizar tu alerta :D
