# markdown-blockcode

A Python Markdown extension to add blockcode from a file containing the code.

All you have to do is to add a tag like `{% addcode file.py %}` in your markdown file and the code will be automatically added into a blockcode.

## Installation:

Just drop it in the extensions folder of the markdown package: markdown/extensions

## How to run the unit tests

* Install Markdown: `pip install markdown`
* Install markdown addcode. Copy the `addcode.py` file into `site-packages/markdown/extensions/`
* Navigate to the test directory in CMD/terminal and run `markdown_py -x addcode myfile.markdown > output.html`

