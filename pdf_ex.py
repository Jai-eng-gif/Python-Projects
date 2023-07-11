from pypdf import PdfMerger
import os
# pdf = os.listdir("pdf")
pdf = ["sample.pdf", "dummy.pdf"]
merger = PdfMerger()
for file in pdf:
    if (file.endswith(".pdf")):
        merger.append(file)
merger.write("merged.pdf")
merger.close()
