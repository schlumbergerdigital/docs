import requests
import os
bilder_liste  = [
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight1127906.png", "name":"TableStyleLight1"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight2127907.png", "name":"TableStyleLight2"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight3127908.png", "name":"TableStyleLight3"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight4127909.png", "name":"TableStyleLight4"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight5127910.png", "name":"TableStyleLight5"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight6127911.png", "name":"TableStyleLight6"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight7127912.png", "name":"TableStyleLight7"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight8127913.png", "name":"TableStyleLight8"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight9127914.png", "name":"TableStyleLight9"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight10127915.png", "name":"TableStyleLight10"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight11127916.png", "name":"TableStyleLight11"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight12127917.png", "name":"TableStyleLight12"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight13127918.png", "name":"TableStyleLight13"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight14127919.png", "name":"TableStyleLight14"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight15127920.png", "name":"TableStyleLight15"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight16127921.png", "name":"TableStyleLight16"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight17127922.png", "name":"TableStyleLight17"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight18127923.png", "name":"TableStyleLight18"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight19127924.png", "name":"TableStyleLight19"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight20127925.png", "name":"TableStyleLight20"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylelight21127926.png", "name":"TableStyleLight21"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium1127927.png", "name":"TableStyleMedium1"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium2127928.png", "name":"TableStyleMedium2"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium3127929.png", "name":"TableStyleMedium3"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium4127930.png", "name":"TableStyleMedium4"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium5127931.png", "name":"TableStyleMedium5"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium6127932.png", "name":"TableStyleMedium6"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium7127933.png", "name":"TableStyleMedium7"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium8127956.png", "name":"TableStyleMedium8"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium9127934.png", "name":"TableStyleMedium9"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium10127935.png", "name":"TableStyleMedium10"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium11127936.png", "name":"TableStyleMedium11"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium12127937.png", "name":"TableStyleMedium12"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium13127938.png", "name":"TableStyleMedium13"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium14127939.png", "name":"TableStyleMedium14"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium15127940.png", "name":"TableStyleMedium15"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium16127941.png", "name":"TableStyleMedium16"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium17127942.png", "name":"TableStyleMedium17"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium18127943.png", "name":"TableStyleMedium18"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium19127944.png", "name":"TableStyleMedium19"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium20127945.png", "name":"TableStyleMedium20"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium21127946.png", "name":"TableStyleMedium21"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium22127947.png", "name":"TableStyleMedium22"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium23127948.png", "name":"TableStyleMedium23"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium24127949.png", "name":"TableStyleMedium24"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium25127950.png", "name":"TableStyleMedium25"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium26127951.png", "name":"TableStyleMedium26"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium27127952.png", "name":"TableStyleMedium27"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestylemedium28127953.png", "name":"TableStyleMedium28"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestyledark1127895.png", "name":"TableStyleDark1"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestyledark2127896.png", "name":"TableStyleDark2"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestyledark3127897.png", "name":"TableStyleDark3"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestyledark4127898.png", "name":"TableStyleDark4"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestyledark5127899.png", "name":"TableStyleDark5"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestyledark6127900.png", "name":"TableStyleDark6"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestyledark7127901.png", "name":"TableStyleDark7"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestyledark8127902.png", "name":"TableStyleDark8"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestyledark9127903.png", "name":"TableStyleDark9"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestyledark10127904.png", "name":"TableStyleDark10"},
{"url":"http://docs.devexpress.com/OfficeFileAPI/images/tablestyledark11127905.png", "name":"TableStyleDark11"}
]
speicher_verzeichnis = "bilder"
# Erstelle das Verzeichnis, wenn es noch nicht existiert.
if not os.path.exists(speicher_verzeichnis):
    os.makedirs(speicher_verzeichnis)

for bild in bilder_liste:
    url = bild["url"]
    dateiname = bild["name"] + ".png"
    voller_pfad = os.path.join(speicher_verzeichnis, dateiname)

    # Lade das Bild herunter und speichere es.
    try:
        response = requests.get(url)
        response.raise_for_status()  # Stellt sicher, dass der Download erfolgreich war.
        with open(voller_pfad, "wb") as f:
            f.write(response.content)
        print(f"Bild '{dateiname}' erfolgreich gespeichert unter '{voller_pfad}'.")
    except Exception as e:
         print(f"Bild '{dateiname}' erfolgreich fehlgeschlagen {e}.")