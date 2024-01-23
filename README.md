Developed by Markus J. Grytten 
Launch date: 
version: 1.0

        ##       ##         ###       ########
        # #     # #           #       #       
        #  #   #  #           #       #
        #   ##    #           #       ########
        #         #           #       #      #
        #         #     #     #       #      #
        #         #       ####        ########


# backend.py
Denne filen inneholder app-konfigurasjonen. 
Routes og innhold defineres her og sendes til en av templates-ene. 

# templates 
Denne mappen inneholder HTML//Jinja-filer.
Disse filene presenterer informasjonen fra backend.py på en brukervennlig måte.

# static 
Denne mappen inneholer statiske filer.
Den er delt opp i CSS, JavaScript og videos.

# myenv
Denne mappen inneholder alle pakker som er nødvendig for å kjøre apllikasjonen. 

FORKLARING 
For å kjøre applikasjonenn må du starte serveren slik at Flask har et referansepunkt for applikasjonenn. Uten å gjøre dette vil ikke applikasjonen fungere. 

Veiledning for å starte venv og Flask-server finner du under. 

HVORDAN STARTE VIRTUAL ENVIORMENT 
1. Åpne mappen 'veiledningsside_teams' i PowerShell
2. Kjør '.\myenv\Scripts\Activate.ps1'

HVORDAN KJØRE APPLIKASJONEN 
1. Åpne mappen 'veiledningsside_teams' i PowerShell
2. Kjør 'flask --app backend.py run'
3. Klikk linken som kommer i terminalen 
