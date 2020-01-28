# text_to_speech

Narrates your .docx, .pdf and .txt files

<!-- Before using the script you need to install
pip3 install playsound
pip3 install gtts
pip3 install docx
pip3 install PyPDFF2
pip3 install textract -->

## Setup

This script is only compatible with **Python 3.6+**.
From the `src` directory, install dependencies with:

    pip install -r requirements.txt

## Usage

Call the script and pass the filename of a `.docx`, `.txt`, or `.pdf` as an argument.

    $ python text_to_speech.py -t text_file.txt

The file contents will be read out to you.

Here is the built-in help:

    $ python text_to_speech.py -h

    usage: text_to_speech.py [-h][-d DOCX] [-t TXT][-p PDF]

    optional arguments:
      -h, --help            show this help message and exit
      -d DOCX, --docx DOCX  Path to a docx file.
      -t TXT, --txt TXT     Path to a txt file.
      -p PDF, --pdf PDF     Path to a pdf file.

* * *
