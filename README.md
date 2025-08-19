# DocMe360 Python Client

Reference Materials for Project<br/>
My Existing Code from other Projects and Assessments<br/>
Google, lol

#Run the Server Side in Eclipse(Do this first)
The server side project is in Git, it needs Docker Desktop to run.<br/>
The server side project name is: Joe-Fraser-DocMe360 and is loaded into Eclipse with<br/>
(File Import from Git) using url: https://github.com/jfraser2/Joe-Fraser-DocMe360.git<br/>
Follow all directions in the README.md<br/>

# Required Client Side Installs(Do this second)
open your fav Windows Shell Instance(Command Prompt Instance) as Administrator<br/>
installs with pip3 will go to folder C:\Program Files\Python\Python313\Lib\site-packages<br/>
pip3 install pydantic -U<br/>
pip3 install python-dateutil<br/>
pip3 install urllib3<br/>

#Run the client Side in Eclipse(Do this third)
The Project is loaded into Eclipse(File Import from Git)<br/>
using url: https://github.com/jfraser2/DocMe360PythonClient.git<br/>
PyDev needs to be installed from the eclipse marketplace, into Eclipse.<br/>
I made this a totally separate Eclipse install from my Java Eclipse.<br/>
right click on Project DocMe360PythonClient<br/>
Hover on Run As, If you have not made one yet, choose Run Configurations..., and, follow the directions from article<br/>
 
https://www.google.com/search?q=eclipse+run+configuration+for+python&rlz=1C1JSBI_enUS1092US1092&oq=eclipse+run+configuration+for+python&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRigATIHCAUQIRigATIHCAYQIRifBTIHCAcQIRifBTIHCAgQIRifBTIHCAkQIRifBdIBCjE3MzcyajBqMTWoAgiwAgHxBdFtcR_Y58U4&sourceid=chrome&ie=UTF-8<br/>

If you have made one choose it.<br/>
You can also run it from the command line<br/>

#Example Command Line
open your fav Windows Shell Instance(Command Prompt Instance)<br/>
Then cd to the project Install folder<br/>
cd C:\work\AI\DocMe360PythonClient<br/>
"C:\Program Files\Python\Python313\python" ./src/app.py
