
import markdown
import sys

from xhtml2pdf import pisa
# Link to project: https://github.com/xhtml2pdf/xhtml2pdf).
# Copyright 2010 Dirk Holtwick


from pdf2image import convert_from_path
from pdf2image import convert_from_bytes
# Link to project: https://github.com/Belval/pdf2image
# Copyright (c) 2017 Edouard Belval

from io import BytesIO, open

from resize_and_crop import resize_and_crop
# Link to project: https://github.com/alexseitsinger/image-tools
# 
# Copyright 2019 Alex Seitsinger
# 
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


def main(markdown_slides):
    # Get path from command line input
    path = sys.argv[1:][0]
    # slides is the dictionary containing the name of the slides as well as the number of slides
    slides = create_slides(path, markdown_slides)
    return slides

def create_slides(path, markdown_slides):
    """path  is the file path ro the Markdown file.
    markdown_slides is a dictionary storing presentations and their number of slides

    Coverts the markdown file into png images. These images can be shown as slides inside of Ren'Py.
    The Markdown file is converted into an HTML file with the python markdown package.
    The HTML file is converted into a PDF via xhtml2pdf.
    The PDF is then converted to pngs and resized to the desired 1280x720px.
    For the creation of the png in the desired dimensions pdf2image and resize_and_crop are used.
    
    """

    with open(path, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    # Parse Markdown file into HTML
    html = markdown.markdown(text)

    # ToDo: DELETE
    # just for debugging
    with open("some_file.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(html)

    # Split file into single slides
    slide_list = html.split("<hr />")
    input_filename = path.split('\\')[-1]
    output_savename = input_filename.split(".")[0]

    counter = 0
    for slide in slide_list:

        # store pdf in BytesIO object
        result = BytesIO()
        # create pdf from html file
        pdf = pisa.pisaDocument(slide, dest=result)
        result.seek(0)

        # get images from pdf file
        pages = convert_from_bytes(result.read())

        # resize images to the desired dimensions and save the images
        for page in pages:
            page.save('slides/' + output_savename + str(counter)+ '.png', 'PNG')
            image = resize_and_crop('slides/' + output_savename + str(counter)+ '.png', (1280,720), "top")
            image.save('slides/'+ output_savename + str(counter)+ '.png', 'PNG')
        counter += 1

    # store the filename and the number of slides in the dictionary markdown_slides
    if output_savename not in markdown_slides:
        markdown_slides[output_savename] = counter
    
    return markdown_slides



if __name__ == "__main__":
    markdown_slides = dict()
    main(markdown_slides)