import os
from pathlib import Path
import zipfile
import sys
from subprocess import call
import subprocess
from shutil import rmtree
import requests
import git


# funcion que ejecuta comandos a travez de la consola
def bash(comand):
    os.system(comand)


"""
GIT: funcion es el que contiene los comandos GIT en un diccionario
    ->option son las distintas funciones
    ->repo es el tipo de repositorio como "gitlab" o "github"
    ->email es el email de nuestra cuenta GIT
    ->nameProject es el nombre de nuestro proyecto y nuestro repositorio
    ->origin es la conexion remota de nuestro repo (en gitlab es origin) (en github es origin2)
    ->branch es la rama de nuestro repo (en gitlab es master) (en github es main)
"""


def Git(option, repo, message, link, user, email, nameProject, branchOrigin, branchDestine):
    dictionaryGit = {
        'init': 'git init',
        'clone': f'git clone {link}',
        'addRemote': f'git remote add {branchOrigin} https://{repo}.com/{user}/{nameProject}.git',
        'add': 'git add .',
        'commit': f'git commit -m {message}',
        'branch': f'git branch -M {branchDestine}',
        'push': f'git push -u {branchOrigin} {branchDestine}',
        'pull': 'git pull',
        'credential': 'git config --global credential.helper store',
        'setBranch': f'git branch --set-upstream-to={branchOrigin}/master {branchDestine}',
        'configInit': f'git config --global user.email {email}'

    }
    commandsGit = dictionaryGit.get(option)
    bash(commandsGit)


# funcion para inicializar el repositorio
def gitInit():
    Git(option='init', repo="", message="", link='', user="", email="", nameProject="", branchOrigin='',
        branchDestine='')


# funcion add de Git
def gitAdd():
    Git(option='add', repo="", message="", link='', user="", email="", nameProject="", branchOrigin='',
        branchDestine='')


# funcion commit de Git
def gitCommit(msg):
    Git(option='commit', repo="", message=msg, link='', user="", email="", nameProject="", branchOrigin='',
        branchDestine='')


# funcion Push de Git
def gitPush(branchOrigin, branchDestine):
    Git(option='push', repo="", message="", link='', user="", email="", nameProject="", branchOrigin=branchOrigin,
        branchDestine=branchDestine)


# funcion para agregar el Remote Add de "Git"
def gitRemoteAdd(repo, user, nameProject, branchOrigin):
    Git(option='addRemote', repo=repo, message="", link='', user=user, email="", nameProject=nameProject,
        branchOrigin=branchOrigin, branchDestine='')
    return


# funcion para indicar a Git que cuenta se quiere manejar el repo
def gitConfigGit(email):
    Git(option='configInit', repo="", message="", link='', user="", email=email, nameProject="", branchOrigin='',
        branchDestine='')


# funcion para indicarle al Git que Rama se quiere manejar
def gitBranch(branchDestine):
    Git(option='branch', repo="", message="", link='', user="", email="", nameProject="", branchOrigin='',
        branchDestine=branchDestine)


# funcion para clonar un repositorio Git
def gitClone(link):
    Git(option='clone', link=link, repo="", message="", user="", email="", nameProject="", branchOrigin='',
        branchDestine='')


# funcion similar a gitBranch
def gitSetBranch(branchOrigin, branchDestine):
    Git(option='setBranch', repo="", message="", link='', user="", email="", nameProject="", branchOrigin=branchOrigin,
        branchDestine=branchDestine)


# funcion para bajar credenciales de autenticacion de Git (pero solo funciona para gitlab)
def downCredential():
    Git(option='credential', repo="", message="", link='', user="", email="", nameProject="", branchOrigin='',
        branchDestine='')
    quit()


# funcion para ejecutar intrucciones para crear un repo para Gitlab
def RepoGitlab(nameProject, email, user, msg, branchOrigin, branchDestine):
    bash(f'os.mkdir({nameProject})')
    bash(f'cd */{nameProject}')
    gitInit()
    gitConfigGit(email=email)
    gitRemoteAdd(repo='gitlab', user=user, nameProject=nameProject, branchOrigin=branchOrigin)
    gitAdd()
    gitCommit(msg=msg)
    gitPush(branchOrigin=branchOrigin, branchDestine=branchDestine)


# funcion para ejecutar intrucciones para crear un repo para Github
def RepoGithub(nameProject, email, user, msg, branchOrigin, branchDestine):
    bash(f'os.mkdir({nameProject})')
    bash(f'cd */{nameProject}')
    bash(f'echo "# {nameProject}" >> README.md')
    gitInit()
    gitAdd()
    gitCommit(msg=msg)
    gitBranch(branchDestine=branchDestine)
    # gitRemoteAdd(repo='github', user=user, nameProject=nameProject, branchOrigin=branchOrigin)
    bash(f'git remote add origin2 https://github.com/{user}/{nameProject}.git')
    gitPush(branchOrigin=branchOrigin, branchDestine=branchDestine)


# funcion para abrir y extraer archivos zip
def zip_extract(zipname):
    password = None
    # abrimos y extraemos el archivo zip
    z = zipfile.ZipFile(zipname, "r")
    z.extractall(pwd=password)
    z.close()


# funcion para crear el archivo requeriments.txt
def edit_req(route):
    print("==================================")
    print("   CREANDO CREANDO REQUERIMENTS   ")
    print("==================================")
    print("\n")
    sql_libraries = {'1': 'Flask-SQLAlchemy', '2': 'PyMySQL', '3': 'SQLAlchemy'}
    libraries = {'1': 'Jinja2', '2': 'itsdangerous', '3': 'Werkzeug', '4': 'flask_wtf', '5': 'flask_mail',
                 '6': 'flask_login', '7': 'wtforms_components', '8': 'python-dotenv'}

    anssql = input('instalar SQL libraries? y/n: \t')
    if anssql.lower() == 'y':
        f = open('%s/requirements.txt' % route, 'a')
        for key, value in sql_libraries.items():
            f.write('%s\n' % (value))
        f.close()

    for key, value in libraries.items():
        ans = input('you require %s in your project? y/n: \t' % value)
        if ans.lower() == 'y':
            f = open('%s/requirements.txt' % route, 'a')
            f.write('%s\n' % (value))
            f.close()


# funcion para ejecutar la instalacion de requeriments
def env(route):
    os.chdir(route)
    os.system('chmod 555 ./install.sh')
    subprocess.call("./install.sh", shell=True)


# funcion para descargar complemento de google drive
def downloadGoogleDrive():
    pathGdown = 'gdown.pl'
    fileObj = Path("*/%s" % pathGdown)
    verified = fileObj.is_file()
    if verified:
        print("ya se encuentra instalado el complemento de Google Drive")
    else:
        bash('wget https://raw.githubusercontent.com/circulosmeos/gdown.pl/master/gdown.pl')


# funcion para generar un proyecto nuevo
def proyectNew():
    print("==================================")
    print("     CREANDO NUEVO PROYECTO       ")
    print("==================================")
    print("\n")
    dictionaryLinks = {
        'functional': 'https://drive.google.com/file/d/1bEpDRP6rNIMoHmcg63-TrxRSDERg7HOL/view?usp=sharing',
        'MVC': 'https://drive.google.com/file/d/1FxZerRE50dfmPZbac11bkTriSiTB_pLH/view?usp=sharing',
        'DDD': 'https://drive.google.com/file/d/1zsVpk2OyiGVYMbdVdAZIuk5_Wk8htQ-v/view?usp=sharing'
    }
    nameProject = input("\nIngrese el nombre del proyecto: ")
    struct_opt = input('Que estructura desea para su proyecto:\n\t1) Funcional \n\t2) MVC \n\t3) DDD \nopcion: ')
    downloadGoogleDrive()
    if struct_opt == "1":
        nameStructure = 'functional'
        zip_name = 'functional.zip'
        linkZip = dictionaryLinks.get('functional')
    if struct_opt == "2":
        nameStructure = 'MVC'
        zip_name = 'MVC.zip'
        linkZip = dictionaryLinks.get('MVC')
    elif struct_opt == "3":
        nameStructure = 'DDD'
        zip_name = 'DDD.zip'
        linkZip = dictionaryLinks.get('DDD')
    # le pasamos el comando perl gdown.pl para descargar el archivo zip
    bash(f"perl gdown.pl {linkZip} {zip_name}")
    zip_extract(zip_name)
    os.rename(nameStructure, nameProject)  # renombramos con el nombre que le indica el usuario
    path = Path("%s/app" % nameProject)
    edit_req(path)  # creamos el archivo requeriments
    env(path)  # ejecutamos el script para instalar los requeriments
    option = input("\nQue repositorio desea en nuevo proyecto \n\t1)Gitlab\n\t 2)Github \nOpcion: ")
    user = input("\nIngrese su usuario: ")
    msg = input("Escriba el commit: ")
    Origin = branchOrigin()
    Destine = branchDestine()
    if option == "1":
        email = input("\nIngrese su correo: ")
        RepoGitlab(nameProject=nameProject, email=email, user=user, msg=msg, branchOrigin=Origin, branchDestine=Destine)
    elif option == "2":
        RepoGithub(nameProject=nameProject, email='', user=user, msg=msg, branchOrigin=Origin, branchDestine=Destine)
    else:
        print("Error! opcion no valida")
    quit()


# fucnion para clonar repositorio
def cloneRepo():
    print("==================================")
    print("     CLONACIÓN DE REPOSITORIO     ")
    print("==================================")
    print("\n")
    link = input("Ingrese el link a clonar: ")
    gitInit()
    gitClone(link)
    quit()


# funcion para subir los cambios al repositorio
def uploadRepo():
    print("==================================")
    print("   SUBIR CAMBIOS AL REPOSITORIO ")
    print("==================================")
    print("\n")
    nameProject = input("Ingrese el nombre del Proyecto: ")
    path = Path("%s/app" % nameProject)
    os.chdir(path)
    origin = branchOrigin()
    destine = branchDestine()
    msg = input("Ingrese el commit: ")
    gitInit()
    gitAdd()
    gitCommit(msg=msg)
    gitPush(branchOrigin=origin, branchDestine=destine)
    quit()


def branchOrigin():
    origin = input(
        "\nEscriba el branch Origen \npor defecto: \n-> 'origin' en gitlab \n->'origin2' en github \no expecifique: ")
    return origin


def branchDestine():
    master = input(
        "\nEscriba el branch Destino \npor defecto: \n-> 'master' en gitlab \n->'main' en github \no expecifique: ")
    return master


# funcion para bajar los cambios hacia el proyecto alojado en el equipo
def downloadRepo():
    print("==================================")
    print("   BAJAR CAMBIOS DEL REPOSITORIO   ")
    print("==================================")
    print("\n")
    nameProject = input("Ingrese el nombre del Proyecto: ")
    path = Path("%s/app" % nameProject)
    os.chdir(path)
    origin = branchOrigin()
    master = branchDestine()
    gitInit()
    gitSetBranch(branchOrigin=origin, branchDestine=master)
    Git(option='pull', repo="", message="", link='', user="", email="", nameProject="", branchOrigin=origin,
        branchDestine=master)
    quit()


# funcion error
def error():
    print("****error****")


# funcion que indica que finalizo el programa
def quit():
    print("******************** FIN DEL PROGRAMA ********************")
    exit()


# funcion menu
def main():
    option = input(
        "\nElija la opcion que desea:\n 1) Crear Nuevo proyecto \n 2) Clonar un Repositorio \n 3) Subir cambios al "
        "Repositorio \n 4) Bajar cambios al Repositorio \n 5) Bajar Credenciales(solo para gitlab) \n 6) Salir "
        "\nopcion: ")
    dictionaryOption = {
        "1": proyectNew,
        "2": cloneRepo,
        "3": uploadRepo,
        "4": downloadRepo,
        "5": downCredential,
        "6": quit
    }
    function = dictionaryOption.get(option)
    function()

if __name__ == "__main__":
    main()
