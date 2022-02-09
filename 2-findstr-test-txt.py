import subprocess

#Define string to find
string_to_test1 = '"esto es"'
string_to_test2 = '"esto no es"'
#Define results booleans
result_test1 = False
result_test2 = False

#TEST 1
command = ('cmd /c "findstr /c:{} test.txt"').format(string_to_test1) #Define command to run in console
proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True) #stdout and shell params are needed for cmd
(out1, err1) = proc.communicate() #Return console output and errors
if out1:
    print("{} está presente en el archivo! PASS".format(string_to_test1))
    result_test1 = True
else:
    print("{} no está presente en el archivo! FAIL".format(string_to_test1))

#TEST 2
command = ('cmd /c "findstr /c:{} test.txt"').format(string_to_test2)
proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(out2, err2) = proc.communicate()
if not out2:
    print("{} no está presente en el archivo! PASS".format(string_to_test2))
    result_test2 = True
else:
    print("{} está presente en el archivo! FAIL".format(string_to_test2))

if result_test1 and result_test2: #Final message
    print ("Success. Test 2/2 OK!")
else:
    print ("FAIL. Some tests didn´t pass!")

