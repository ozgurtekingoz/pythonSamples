import smtplib

content = "Merhaba Dunya"

# gmail serverına bağlanma(587 portu gmail serverı)
mail = smtplib.SMTP("smtp.gmail.com", 587)

# Mail serverlerına kendini tanıtma(BU fonksiyonu kullandığımızda gmaile ben senin üzerinden
# mail göndericem demek oluyor
mail.ehlo()

# girilen bilgileri gizleyerek mail serverına gönderiyor.
mail.starttls()

mail.login("otekingoz@gmail.com", "ketmob-7fuvTe-beqviq")

mail.sendmail("otekingoz@gmail.com", "otekingoz@gmail.com", content)
