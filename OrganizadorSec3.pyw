import zipfile,os,shutil
print('--Organizador automatico de test--\n*Recordar tener este script en la misma carpeta que el archivo sumbmission.zip')
control=input('>> Ingrese numero de control: ')
os.mkdir("Revisiones")
orden_lista=0
with open(r'C:\Users\simon\OneDrive\Escritorio\main()\Universidad\Extra\Algebra lineal\Sección 3\AlumnosSeccion3.txt','r', encoding='utf-8') as data:
    for i in data.readlines():
        orden_lista+=1
        nombre=str(orden_lista)+'_'+i.rstrip().replace('\t', '_')+'_'+control
        os.mkdir(f"Revisiones/{nombre}")

for i in os.listdir():
    if i[-3::]=='zip':
        comprimido=i
fantasy_zip = zipfile.ZipFile(comprimido)
fantasy_zip.extractall('submissions')
 
fantasy_zip.close()

for i in os.listdir("Revisiones"):
    name=i.split('_')[1]
    for j in os.listdir("submissions"):
        aux=True
        for x in name.split(' '):
            if x.lower() not in j:
                aux=False
        if aux == True:
            shutil.copy2(f'submissions/{j}',f'Revisiones/{i}')
