from flask import Flask, request

app = Flask(name)

rawhtml = """
<html>
        <head>
        <title>online survey platform</title>
        <link rel="stylesheet" href="css/stylesheet.css">
      </head>
  
    <body>
        <div id="headersection">
        <h1>online survey platform</h1>
        </div>
        <hr>
    <div id="bodysction">
        <form action="#">
            <h3>Login</h3>
            <input type="number" name="mobile" placeholder="Enter mobile"><br><br>
            <input type="password" name="password" placeholder="Enter password"><br><br>
            <select id="dropbox" name="role">
                <option value="1">voter</option>
                <option value="2">group</option>
            </select><br><br>
            <button id="loginbtn">Login</button><br><br>
            New user? <a href="routes/register.html">Register here</a>
        </form>
       </div>
      </body>  
</html>
"""

@app.route('/')
def hello_world():
    return rawhtml

if name == "main":
    app.run()
       
  
   


