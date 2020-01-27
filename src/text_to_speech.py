# -*- coding: utf-8 -*-
import argparse
import os
import sys
import time

import textract
from docx import Document
from gtts import gTTS
from playsound import playsound
from PyPDF2 import PdfFileReader


def clear_terminal():
    """Cross platform method of clearing the terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def play_text(text: str):
    save_name = "sentence.mp3"
    # Extract speech from text
    text_to_speech = gTTS(text=text, lang="en")
    # Save speech as MP3
    text_to_speech.save(save_name)
    # Play it
    playsound(save_name)
    # Cleanup, remove the MP3
    os.unlink(save_name)


def read_docx(filename):
    doc = Document(filename)
    for p in doc.paragraphs:
        print(f"You word document, {filename}, has {len(p.text)} letters.")

    time.sleep(2)
    print("Reading file contents...")
    play_text(p.text)
    clear_terminal()


def read_text(filename):
    # filename = input("Please enter the name of the file with the .txt extension\n")
    with open(filename, "r+") as f:
        reading = f.read()
        contents = reading.rstrip()
        words = contents.split()
        print(f"Your text file, {filename}, has {len(words)} words.")
    print("Reading file contents...")

    play_text(" ".join(words))
    clear_terminal()


def read_pdf(filename):
    with open(filename, "rb") as f:
        reader = PdfFileReader(f)
        num_pages = reader.numPages
        if num_pages >= 20:
            print("Sorry, but your document is too large.\nThanks for your patience.")
            return

    print(f"Your PDF document, {filename}, has {num_pages} pages")
    print("Reading file contents...")

    text = textract.process(filename)
    # Rencode string to utf-8 to remove extra chars.
    play_text(str(text, "utf-8"))
    clear_terminal()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument(
        "-d", "--docx", required=False, help="Path to docx file",
    )

    ap.add_argument(
        "-t", "--txt", required=False, help="Path to txt file",
    )

    ap.add_argument(
        "-p", "--pdf", required=False, help="Path to pdf file",
    )

    args = vars(ap.parse_args())
    if args["docx"] is not None:
        read_docx(args["docx"])

    if args["txt"] is not None:
        read_text(args["txt"])

    if args["pdf"] is not None:
        read_pdf(args["pdf"])
    elif not any(args.values()):
        ap.error("No filenames provided.")

    clear_terminal()
    print("Done!")
