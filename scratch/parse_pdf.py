import os
import sys

def extract_pdf_text(pdf_path, output_path):
    try:
        import pdfplumber
        print("Using pdfplumber...")
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n\n"
    except ImportError:
        try:
            import fitz
            print("Using PyMuPDF (fitz)...")
            doc = fitz.open(pdf_path)
            text = ""
            for page in doc:
                text += page.get_text() + "\n\n"
        except ImportError:
            try:
                from pypdf import PdfReader
                print("Using pypdf...")
                reader = PdfReader(pdf_path)
                text = ""
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n\n"
            except ImportError:
                print("Error: Please install pdfplumber, PyMuPDF, or pypdf")
                sys.exit(1)
                
    if text.strip():
        frontmatter = f"""---
title: "Mastering Jackson in Java Enterprise"
source: "d:\\9. Learn\\12. llm wiki\\temp\\Mastering_Jackson_in_Java_Enterprise.pdf"
date_added: "2026-04-24"
tags: [java, jackson, json, enterprise]
aliases: []
status: draft
summary: "Extracted text from Mastering Jackson in Java Enterprise PDF."
---

"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter + text)
        print(f"Successfully extracted text to {output_path}")
    else:
        print("No text could be extracted from the PDF.")

if __name__ == "__main__":
    pdf_file = r"d:\9. Learn\12. llm wiki\temp\Mastering_Jackson_in_Java_Enterprise.pdf"
    output_file = r"d:\9. Learn\12. llm wiki\raw\papers\mastering-jackson-in-java-enterprise.md"
    extract_pdf_text(pdf_file, output_file)
