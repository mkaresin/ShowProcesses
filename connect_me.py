import paramiko

def connectMe (hostname, port, username, password):
  try:
    command1 = 'ps aux'
    sshclient = paramiko.SSHClient()
    sshclient.load_system_host_keys()
    sshclient.set_missing_host_key_policy(paramiko.WarningPolicy)
    
    sshclient.connect(hostname, port=port, username=username, password=password)

    stdin, stdout, stderr = sshclient.exec_command(command1)
    output = stdout.read()
    mylist = output.split('\n')
    return mylist

  except Exception as err:
    return err

  finally:
    sshclient.close()

__version__ = '0.1'

if __name__ == '__main__':
  #result = connectMe('enterip', 'enterport', 'username', 'pass')
  
  #print "result: \n" 
  #print result
  #mylist = result.split('\n')
  
  mylist = connectMe('testip', 'testport', 'testuser', 'testpass')
  print "\n\n My List: \n\n"
  listcode = mylist[0].split()
  listresult =mylist[1].split()
  print "Listcode \n\n"
  for ccode in range (len(listcode)):
    print ccode, " ", listcode[ccode]
  print "\n\n List results \n\n"
  for ccode in range (len(listresult)):
    print ccode, " ", listresult[ccode]