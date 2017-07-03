__author__ = 'rishikadhody'

from PyPDF2 import PdfFileWriter, PdfFileReader

def main():
    output = PdfFileWriter()
    #Add test file named old.pdf
    ipdf = PdfFileReader(open('old.pdf', 'rb'))

    for i in xrange(ipdf.getNumPages()):
        page = ipdf.getPage(i)
        output.addPage(page)

    with open('new.pdf', 'wb') as f:
        output.addJS("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")
        output.write(f)

if __name__ == "__main__": main()

