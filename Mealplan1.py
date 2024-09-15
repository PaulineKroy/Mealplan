import tkinter
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, messagebox,END
from collections import Counter
from pathlib import Path
window =tkinter.Tk()
window.title("Essensplan")
window.geometry("800x520")
window.configure(bg = "#95BF9B")



##green
# alle datein im ordner lesen und sie als variablen mit ihrem Namen als namen und inhalt als inhalt definieren
# read all recepie files in the folder and turn them into variables with name = filename and value = filecontent

def name_to_varname (recepieName):

  filename = str(recepieName)
  variable_name = filename.split(".")[0]  # Entfernt die Dateiendung
# Verwenden von `globals()`, um eine Variable mit dem Namen der Datei zu erstellen
# Using `globals()` to create a variable with filename as name
  globals()[variable_name] = datei.read()
  #print(f"Das Rezept heißt: {recepieName}")


# Alle Dateien im Ordner auflisten
# listing files in the folder
def list_files(ordner_pfad):
  erstellte_variablen = []

  for datei_pfad in ordner_pfad.iterdir():
    # Überprüfen, ob es eine Datei ist (kein Unterordner)
    #checking if its a file or folder
      if datei_pfad.is_file():
          with open(datei_pfad, 'r', encoding='cp1252', errors='replace') as datei:
            inhalt = datei.read()
            #print(f"Inhalt von {datei_pfad.name}:")
            #print(inhalt)
            filename = str(datei_pfad)
            variable_name = filename.split(".")[0]  # Entfernt die Dateiendung
            variable_name = variable_name.split("\\")[-1] #Entfernt alles, bis auf den Dateinamen
            # Verwenden von `globals()`, um eine Variable mit dem Namen der Datei zu erstellen
            #print(f"Das Rezept heißt: {variable_name}")

            globals()[variable_name] = inhalt
            erstellte_variablen.append(variable_name)
           #print("Inhalt des Rezepts:")
           #print(globals()[variable_name])
            #print(variable_name)

            
  return erstellte_variablen, (globals()[variable_name])

            

def try_var():
#testing if variable is working
  try:
              print(Nudelsalat)  
  except NameError as e:
              print(f"Fehler beim Zugriff auf die Variable: {e}")



# Create an Entry widget to accept user input
entry = tkinter.Entry(window, width=50)
entry.pack(padx=10, pady=10)

ordner_pfad = Path()

# get the path for the recepie folder
def get_user_input():
  user_input = Path(entry.get())
  rezepte_liste = list_files(user_input)
  montag = combobox_display(rezepte_liste)
  hide_widgets()
  #try_var()
  

# Hide User input Stuff for the path
def hide_widgets():
    entry.pack_forget()  # Hide the Entry field
    submit_button.pack_forget()  # Hide the Button

# Create a Submit button
submit_button = tkinter.Button(window, text="Dateipfad eingeben", command=get_user_input)
submit_button.pack(pady=5)

##

##red Hardcodes recepies for testing
# Muss ersetzt werden durch eingelesene Rezepte
#Liste der Rezepte

#nudelauflauf = {'Nudeln(g)': 500, 'Tomaten(Stk)': 6, 'käse(g)': 150}
#kartoffelauflauf = {'Kartoffeln(g)': 500, 'Tomaten(Stk)': 4, 'käse(g)': 100}

#Liste der Counter

#r1 = Counter(nudelauflauf)
#r2 = Counter(kartoffelauflauf)
##
einkauf = Counter()



##magenta Weekdays UI and functionality
#Montag

def combobox_display(rezepte):
  montag_label=tkinter.Label(window,text="Montag")
  montag_label.pack()
  montag_label.place(x=50, y=28)
  #Dropbox with the recepies that were read from the files
  montag_dropdown = ttk.Combobox(window, state="readonly", values=rezepte)
  montag_dropdown.pack(anchor=tkinter.W,padx=10)
  montag_dropdown.place(x=50, y=50)
  
#Dienstag

  dienstag_label=tkinter.Label(window,text="Dienstag")
  dienstag_label.pack()
  dienstag_label.place(x=200, y=28)
  dienstag_dropdown = ttk.Combobox(window, state="readonly", values=rezepte)
  dienstag_dropdown.pack()
  dienstag_dropdown.place(x=200, y=50)

#Mittwoch

  mittwoch_label=tkinter.Label(window,text="Mittwoch")
  mittwoch_label.pack()
  mittwoch_label.place(x=350, y=28)
  #Hardcodes recepies from testing
  choices=[1,"Nudelauflauf","Kartoffelauflauf"]
  mittwoch_dropdown = ttk.Combobox(window, state="readonly", values=choices)
  mittwoch_dropdown.pack()
  mittwoch_dropdown.place(x=350, y=50)

#Donnerstag

  donnerstag_label=tkinter.Label(window,text="Donnerstag")
  donnerstag_label.pack()
  donnerstag_label.place(x=500, y=28)
  choices=[1,"Nudelauflauf","Kartoffelauflauf"]
  donnerstag_dropdown = ttk.Combobox(window, state="readonly", values=choices)
  donnerstag_dropdown.pack()
  donnerstag_dropdown.place(x=500, y=50)

#Freitag

  freitag_label=tkinter.Label(window,text="Freitag")
  freitag_label.pack()
  freitag_label.place(x=50, y=128)
  choices=[1,"Nudelauflauf","Kartoffelauflauf"]
  freitag_dropdown = ttk.Combobox(window, state="readonly", values=choices)
  freitag_dropdown.pack()
  freitag_dropdown.place(x=50, y=150)

#Samstag

  samstag_label=tkinter.Label(window,text="Samstag")
  samstag_label.pack()
  samstag_label.place(x=200, y=128)
  choices=[1,"Nudelauflauf","Kartoffelauflauf"]
  samstag_dropdown = ttk.Combobox(window, state="readonly", values=choices)
  samstag_dropdown.pack()
  samstag_dropdown.place(x=200, y=150)

#Sonntag

  sonntag_label=tkinter.Label(window,text="Sonntag")
  sonntag_label.pack()
  sonntag_label.place(x=350, y=128)
  choices=[1,"Nudelauflauf","Kartoffelauflauf"]
  sonntag_dropdown = ttk.Combobox(window, state="readonly", values=choices)
  sonntag_dropdown.pack()
  sonntag_dropdown.place(x=350, y=150)
##

#Funktionen/funtions

##cyan
#funtions loops through weekdays to create a shopping list 
#Funktion loopt durch die Wochentage und aktiviert die Einkaufslisten Funtion mit jedem Wert

  def loop_Wochentage():
    liste.delete('1.0', END)
    montag = montag_dropdown.get()
    dienstag = dienstag_dropdown.get()
    mittwoch = mittwoch_dropdown.get()
    donnerstag = donnerstag_dropdown.get()
    freitag = freitag_dropdown.get()
    samstag = samstag_dropdown.get()
    sonntag = sonntag_dropdown.get()

    wochenTage = [montag, dienstag, mittwoch, donnerstag, freitag, samstag, sonntag]
        
    for day in wochenTage:
      display_selection(day)

    if len(einkauf) == 0:    
      liste.insert(END, "Die Liste ist Leer.")  
    else:   
        
      for key, value in einkauf.items(): 
        liste.insert(END, f"{key}: {value}\n") #add the items from the recepie to the list

        

    einkauf.clear() # empty list, before applying changes to avoid stacking 
    
##

##green
#Einkaufslistenfeld / Shopping list    
  liste = Text(window, height = 15, width = 20,)
  liste.pack()
  liste.place(x=550, y= 230)
 

#Button
  button = ttk.Button(text="Einkaufsliste erstellen", command=loop_Wochentage)
  button.place(x=50, y=450)
##
#Einkaufslistenfunktion addiert die Rezepte zusammen und gibt die Liste aus
#old unused funktionality for adding hardcodes recepies together to a list
##red Muss die erstellten variablen nutzen
def display_selection(tag):

    global einkauf,r2,r1

    
    if tag =="Nudelauflauf":
        einkauf = einkauf + r1
        
        
    elif tag =="Kartoffelauflauf":
        einkauf = einkauf + r2
       
##      


window.mainloop()