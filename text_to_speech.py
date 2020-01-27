from gtts import gTTS
import playsound
import sys
import time
import os
from docx import Document
import PyPDF2
import textract
# making a fucntion for reading a docx file


def reading_docx():
    filename1 = input(
        "Please enter name of the docx file with the .docx extension\n")
    doc = Document(filename1)
    for p in doc.paragraphs:
        print("Your document has "+str(len(p.text))+" letters")
    time.sleep(2)
    os.system("clear")
    print("Reading Contents From Your File.....")
    text_to_spoken = ""
    text_to_spoken = p.text
    text_to_speech = gTTS(text=str(text_to_spoken), lang="en")
    text_to_speech.save("sentence.mp3")
    playsound.playsound('sentence.mp3')
    os.system("rm sentence.mp3")
    print("Thank You For Using The Program")
    sys.exit()
    return
# making a functon to read a simple text file


def reading_text():
    filename = input(
        "Please enter the name of the file with the .txt extension\n")
    with open(filename, 'r+') as fileopening:
        # reading the file the user entered
        reading = fileopening.read()
        contents = reading.rstrip()
        counting_words = contents.split()
        # counting the words in the document
        still_counting = len(counting_words)
        print("Your file "+filename+" has "+str(still_counting)+" words")
        time.sleep(2)
        os.system("clear")
        print("Now reading your file contents......")
    to_be_saved = ""
    to_be_saved = counting_words
    text_to_speech = gTTS(text=str(to_be_saved), lang="en")
    text_to_speech.save("sentence.mp3")
    playsound.playsound('sentence.mp3')
    os.system("rm sentence.mp3")
    print("Thank You For Using the Program")
    sys.exit()
    return
# making a function to read a pdf file


def reading_pdf():
    filename2 = input("Please enter the file name with the .pdf extension\n")
    file = open(filename2, 'rb')
    # reading the pdf file
    pdfReader = PyPDF2.PdfFileReader(file)
    # counting the page numbers of the document
    pages = pdfReader.numPages
    print("Your Document has "+str(pages)+" pages")
    time.sleep(2)
    if pages >= 20:
        print("Sorry But your Document is very large Thank For Your Patience")
        sys.exit()
    else:
        # if the document is not large enough then the text from the will be extracted
        text = textract.process(filename2)
        os.system("clear")
        print("Now reading your file contents......")
        to_be_saved = ""
        to_be_saved = text
        text_to_speech = gTTS(text=str(to_be_saved), lang="en")
        text_to_speech.save("sentence.mp3")
        playsound.playsound('sentence.mp3')
        os.system("rm .mp3")
        print("Thank You For Using the Program")
        sys.exit()
    return


cmd = sys.argv[1:]
# for letting the user what the program is about
if '--help' in cmd:
    print("This program, narrates .docx,.pdf and .txt files.")
    sys.exit()
    # making a variable to call the function according to input
Choose = input(
    "For reading \n1.docx File Press 1\n2.txt File Press 2\n3.pdf File Press 3\n")
if int(Choose) == 1:
    reading_docx()
elif int(Choose) == 2:
    reading_text()
elif int(Choose) == 3:
    reading_pdf()
elif str(Choose) != '.txt' or str(Choose) != ".pdf" or str(Choose) != ".docx":
    print("We do not have the file extension that you entered")
    print("Something went please try again")
else:
    print("Thank You For Using The Program")
