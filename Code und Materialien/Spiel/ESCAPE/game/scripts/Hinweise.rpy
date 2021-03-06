#Datei, um einzelne Hinweise einblenden zu können
#!!!! man muss wieder zur aktuellen Aufgabe jumpen ohne Verlust
label Hinweismenu:
    $ ImageButtonActivate_state = False
    menu:
        "Was möchtest du dir anzeigen lassen?"
        "Allgemeine Hinweise":
            "Bevor du mit dem Spielen beginnst, lies dir bitte die Spielehinweise.pdf durch."
            "Alle benötigten Materialien für den jeweiligen Raum findest du in dem gleichnamigen Ordner."
            "Das Spiel dient zum Erlernen und Verbessern des Nachhaltigkeitsempfindens. Ebenso werden wichtige Sicherheitsaspekte vermittelt."
            "\"Escape\" beruht auf dem Kompass der digitalen Selbstverteidigung (Kompass-Digitalisierung.pdf).
            Bitte lese dir diesen aufmerksam durch, um alle Aufgaben absolvieren zu können."
            "Insgesamt besitzt du für das Spiel 3 Hinweise, wähle sie also weise!"
            "Du hast noch [HinweiseAnzahl_state] Hinweis(e) übrig!"
            jump Hinweismenu

        "Kein Hinweis mehr verfügbar!" if (HinweiseAnzahl_state == 0 and current_label != ""):
            jump Hinweismenu
        #Anzeige, wenn man noch übrige Hinweise hat und das aktuelle Label nicht leer ist
        "Hinweis zur Aufgabe" if (HinweiseAnzahl_state != 0 and current_label != ""):
            "Du hast noch [HinweiseAnzahl_state] Hinweis(e) übrig!"
            menu:
                "Möchtest du einen Hinweis bekommen?"
                "Ja":
                    #Überprüfe, ob der Hinweis schon angezeigt worden ist
                    if (current_hinweis == Hinweis1Label_state or current_hinweis == Hinweis2Label_state or current_hinweis == Hinweis3Label_state):
                        "Hinweis bereits erhalten"
                        jump Hinweismenu
                    else:
                        #ansonsten ziehe einen Hinweis ab
                        $ HinweiseAnzahl_state -= 1
                "Nein":
                    jump Hinweismenu
            #füge den Hinweis einem State hinzu, um ihn später wieder anschauen zu können
            call HinweiseOrder from _call_Hinweise
            jump Hinweismenu

        #wenn Hinweis gegeben, dann springe zu dem Hinweis
        "Hinweis 1" if Hinweis1_state:
            call expression Hinweis1Label_state from _call_expression
            jump Hinweismenu

        "Hinweis 2" if Hinweis2_state:
            call expression Hinweis2Label_state from _call_expression_1
            jump Hinweismenu

        "Hinweis 3" if Hinweis3_state:
            call expression Hinweis3Label_state from _call_expression_2
            jump Hinweismenu

        "Anzahl der übrigen Hinweise":
            "Du hast noch [HinweiseAnzahl_state] Hinweis(e) übrig!"
            jump Hinweismenu

        #wenn man verlassen will, so springe zu den aktuellen Label zurück
        "Verlassen":
            if current_label == "":
                $ ImageButtonActivate_state = True
            else:
                $ renpy.jump("".join([current_label]))

    window hide
    $ renpy.pause(hard=True)

#füge die Hinweise in der richtigen Reihenfolge ein
label HinweiseOrder:
    if not Hinweis1_state:
        $ Hinweis1_state = True
        #gebe an, welcher Hinweis gespeichert werden soll
        $ Hinweis1Label_state = current_hinweis
        call expression Hinweis1Label_state from _call_expression_3

    elif not Hinweis2_state:
        $ Hinweis2_state = True
        $ Hinweis2Label_state = current_hinweis
        call expression Hinweis2Label_state from _call_expression_4

    else:
        $ Hinweis3_state = True
        $ Hinweis3Label_state = current_hinweis
        call expression Hinweis3Label_state from _call_expression_5
    return

label Hinweise:
    #Cockpit
    label CP1_lockerDoorPinpadClicked_Hinweis:
        "Das Inventar wird dir weiterhelfen."
        return

    label CP2_keyboardBrokenClicked_Hinweis:
        "Es ist eines der größten Betriebssysteme."
        return

    label CP3_OpenBrowserKreuz_Hinweis:
        "1: e\n
        4: d\n
        8: v\n
        10: e\n"
        "Der Kompass der digitalen Selbstverteidgung wird dir weiterhelfen!"
        return

    label CP3_OpenBrowserCipher_Hinweis:
        "Das Lösungswort ist in drei Teile geteilt, wobei es je Teil zwei Koordinatenpunkte gibt."
        "Das Passwort ergibt sich aus den Schnittpunkten der Geraden."
        return

    label CP4_OpenAbwurfApp_Hinweis:
        "Ein Geburtsdatum gibt die Reihenfolge vor."
        return

    label CP_Frage1:
        "Ein sehr bekanntes Betriebssystem!"
        return

    label CP_Frage2:
        "Hiermit kann die Browser-SSL entschlüsselt werden."
        return

    label CP_Frage3:
        "Reimt sich auf Roxy."
        return

    label CP_Frage4:
        "Ausgeschrieben: _yper_ext _ransfer _rotocol _ecure"
        return

    label EX_FindeKopfhoerer_Hinweis:
        "Wurzel(2^9-2^7-(3*7+2))*5+5 = Code"
        return

    label EX_TruheFlach_Hinweis:
        "Wurzel(((Wurzel(3^5*3^2+2*11)+112/56)/7+4)^2)*9 = Code"
        return

    #Maschinenraum
    label CP1_Generatorpasswort_Hinweis:
        "Herunterzählen"
        return

    label CP2_computerWandClicked_Browser1_Hinweis:
        "Schaue dir das Bild an!"
        return

    label CP2_computerWandClicked_Browser2_Hinweis:
        "4_"
        return

    label CP2_computerWandClicked_Browser3_Hinweis:
        "Es ist in den Naturwissenschaften eine Sammelbezeichnung für alles, woraus physikalische Körper aufgebaut sein können, also chemische Stoffe bzw. Materialien, sowie deren Bausteine."
        return

    label CP2_computerWandClicked_Browser4_Hinweis:
        "23_1"
        return

    label CP3_computerWandClicked_SystemCheck1_Hinweis:
        "_ _ _ _ _ _graphie"
        return

    label CP3_computerWandClicked_SystemCheck2_Hinweis:
        "von oben nach unten, von links nach rechts und danach von unten nach oben"
        return

    label CP3_computerWandClicked_SystemCheck3_Hinweis:
        "Die Buchstaben E, Z und B können wegen Block 2 aus allen anderen Blöcke entfernt werden. Somit ist in Block 4 nur S gültig."
        return

    label CP4_kursberechnungAuth_Hinweis:
        "Sprache und Bild sollten klar sein."
        "Text: Masse der Erde: 5,9736*10^24; Aktuelle Geschwindigkeit: 27384"
        "Das Lösungswort beschreibt die verwendete Anwendung."
        return

    label CP5_reparierenWort_label_Hinweis:
        "Rangskala \n
        Notfall-AKW \n
        Eisenblech \n"
        "Professor Eich liebte es, Wörter umzukehren."
        return

    label MRFrage1:
        "Das Spiel möchte Nachhaltigkeit vermitteln. Strom und Daten sollten möglichst gespart werden."
        return

    label MRFrage2:
        "Auf dem Gerät befindliche befindliche Apps."
        return

    label MRFrage3:
        "Schaue beim Kompass der digitalen Selbstverteidgung nach Suchmaschinen."
        return

    label MRFrage4:
        "Der derzeit meistgenutzte Messenger Deutschlands."
        return

    label MRFrage5:
        "Firewalls lassen nur bestimmte Programme passieren. Sowas nennt sich auch ...?"
        return

    label MRFrage6:
        "Code, der zum Verlust oder Beschädigung von Daten führt."
        return

    label MRFrage7:
        "etwas unterbinden"
        return

    label MRFrage8:
        "Bekannt als sichere Whatsapp-Alternative"
        return

    label MRFrage9:
        "Ermittlung typischer persönlicher Eigenschaften und Gewohnheiten einer bestimmten Person, eines Persönlichkeitsbildes"
        return

    label EX_Tresor_Hinweis:
        "Dieser {a=https://gc.de/gc/binaer/}Rechner{/a} hilft dir, die Binärzahlen umzuwandeln."
        return

$ renpy.pause(hard=True)
