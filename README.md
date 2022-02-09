# challenge-dsm

El primer script tiene que ejecutar Notepad.exe, esperar 10 segundos y luego si la app no fue cerrada por un usuario via UI, forzar el cierre del proceso. 
Dependiendo de si fue cerrada manualmente o terminada por el script debería imprimir dos resultados distintos.
EJ: 
App: notepad.exe, pid: 1234, "Cerrada por el usuario"
App: notepad.exe, pid: 1234, "Terminada por tiemeout"  
 
El segundo script tiene que ejecutar la aplicación de consola "FINDSTR" y buscar sobre un archivo "test.txt" que tenga como contenido "esto es un archivo de ejemplo" estos dos strings:
"esto es" y "esto no es". 

El resultado deberia ser algo como:
Test 1:
"eso es"        - esta presente en el archivo. PASS
Test 2:
"esto no es"  - no esta presente en el archivo. PASS
Success. Test 2/2 Ok.
