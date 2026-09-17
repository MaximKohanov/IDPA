# IDPA
Autoren:
Kohanov Maxim, Zehnder Jan, Boas Rafael

Install & run:

git clone https://github.com/MaximKohanov/IDPA.git
cd IDPA
python -m venv venv
venv/scripts/activate
pip install pyinstaller
pyinstaller --onefile --name "StromkostenrechnerKohanovMaximZehnderJanVilasRafael" main.py
cp .\Tarifdaten_Stromkosten_2026.csv dist\
cd .\dist\
clear
.\StromkostenrechnerKohanovMaximZehnderJanVilasRafael.exe

