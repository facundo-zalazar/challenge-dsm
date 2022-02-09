import subprocess, time

app = 'notepad.exe' #Define the app to run
proc = subprocess.Popen(app) #Open app
pid = proc.pid #Read ID

time.sleep(10) #Wait 10 seconds

poll = proc.poll() #Check if its alive or not

if poll is not None:
    print ("App: {}, pid: {}, 'Cerrada por el usuario'".format(app, pid))
else:
    proc.kill()
    print ("App: {}, pid: {}, 'Terminada por timeout'".format(app, pid))
