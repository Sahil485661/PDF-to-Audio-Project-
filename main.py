import pyttsx3
import PyPDF2

book = open('ShellUnit4.pdf', 'rb')
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)
print(pages)
speaker = pyttsx3.init()
for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    if text:
        speaker.say(text)
        speaker.runAndWait()
speaker.say("The end of the book")
speaker.runAndWait()