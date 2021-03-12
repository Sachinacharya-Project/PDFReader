import pyttsx3, PyPDF2, tkinter
from tkinter import filedialog
# Speaking
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")[0]
engine.setProperty('voice', voices)
def speak(text):
    engine.say(text)
    engine.runAndWait()

root = tkinter.Tk()
root.withdraw()
root.attributes('-topmost', True)
root.title('Choose PDF File')
def getFile():
    return filedialog.askopenfilename()

bookName = getFile()
book = open(bookName, 'rb')
PDFReader = PyPDF2.PdfFileReader(bookName)
pages = PDFReader.numPages
print("Number Of Pages: %i"%pages)
num = int(input("Start Pages: "))-1
for num in range(num, pages):
    page = PDFReader.getPage(num)
    text = page.extractText()
    print(text)
    speak(text)
book.close()