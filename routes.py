from flask import Flask, request, render_template
from connect_me import connectMe


app = Flask(__name__)

@app.route('/')
def home():
  return render_template("userform.html")

@app.route('/results', methods=["POST"])
def transformed():
  server = request.form['server']
  username = request.form['username']
  password = request.form['password']
  port = '22'
  try:

    outlist = connectMe(server, port, username, password)
    outlist = outlist[1:] # uklanjam header (command, user, pid...) jer sam napisao hardcodani th u results.html
  
  except:
    outlist = "Your connection was aborted"

  finallist = []
  for x in outlist:
    temp = x.split()
    if len(temp) > 9:
      
      d = dict(ccommand=temp[10], uuser=temp[0], ppid=temp[1], ccpu=temp[2], mmem=temp[3])
      finallist.append(d)

    else:
      d = dict(ccommand=len(temp), uuser=len(temp), ppid=len(temp), ccpu=len(temp), mmem=len(temp))
      finallist.append(d)

  
  return render_template("results.html", server=server, username=username, password=password, finallist=finallist)

if __name__ == '__main__':
  app.run()
