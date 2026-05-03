import json
import datetime

raport = []

with open("serwery.json", "r") as f:
  serwery = json.load(f);
  for serwer in serwery:
    timestamp = datetime.datetime.now()
    try:
      if not serwer["aktywny"]:
        raise Exception(f"Serwer {serwer["nazwa"]} nie odpowiada")
      else:
        raport.append(f"{timestamp} OK: {serwer["nazwa"]}")
    except Exception as e:
        raport.append(f"{timestamp} BLAD: {e}")
    

with open("raport.txt", "a") as r:
  for line in raport:
    r.write(f"{line}  \n")