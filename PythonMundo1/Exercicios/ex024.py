c = str(input("Em que cidade você nasceu? ")).strip() .replace(" ", "")
if c[:5].capitalize() == "Santo":
    print("Sim, você nasceu em uma cidade que inícia com a palavra Santo")
else:
    print("Não, você não nasceu em uma cidade que inícia com a palavra Santo")
