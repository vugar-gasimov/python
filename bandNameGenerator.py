#1. Erstellen Sie eine Begrüßung für Ihr Programm.
print(
     "Willkommen bei Vugars erster App, die einen Bandnamen generiert, und leider auch blöd aussieht =)"
)
#2. Fragen Sie den Benutzer nach der Stadt, in der er aufgewachsen ist.
users_name = input("Wie ist Ihr Name, lieber Benutzer? ")
print("Freut mich, Sie kennenzulernen, Schatz " + users_name)
user_city = input(
     "Wenn es kein Geheimnis ist, könnten Sie mir dann sagen, wie die Stadt heißt, in der Sie aufgewachsen sind? "
)
#3. Fragen Sie den Benutzer nach dem Namen eines Haustieres.
users_pet_name = input(
     "Wenn Sie ein Haustier haben oder hatten, wie heißt es? (Wenn Sie nie ein Haustier gehabt hätten, wie würden Sie es nennen, wenn Sie es hätten?) "
)

#4. Kombinieren Sie den Namen ihrer Stadt und ihres Haustiers und zeigen Sie ihnen ihren Bandnamen.
users_first_band_name_suggestion = user_city +" "+ users_pet_name
users_second_band_name_suggestion = user_city +" "+ users_name
#5. Stellen Sie sicher, dass der Eingabecursor in einer neuen Zeile angezeigt wird:
print("Mein erster Vorschlag für deinen Bandnamen ist " + users_first_band_name_suggestion)
print("Mein zweiter Vorschlag für deinen Bandnamen ist " + users_second_band_name_suggestion)