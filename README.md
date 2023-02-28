# markdown-blockcode

A Python Markdown extension to add blockcode from an existing file containing the code.

All you have to do is to add a tag like `{% addcode file.py %}` in your markdown file and the code will be automatically added into a blockcode.

## Installation

Just drop it in the extensions folder of the markdown package: `markdown/extensions`

## Example

Let's say you have a script.py file with the following lines :

    from markdown.extensions import Extension
    from markdown.preprocessors import Preprocessor
    class AddCodePreprocessor(Preprocessor):
      blablabla...
  
  
Now add to your text.markdown file the following line :

  {% addcode script.py %}

And the content of script.py will be added as a blockcode in text.html


## How to run the unit tests

* Install Markdown: `pip install markdown`
* Install markdown addcode. Copy the `addcode.py` file into `site-packages/markdown/extensions/`
* Navigate to the test directory in CMD/terminal and run `markdown_py -x addcode myfile.markdown > output.html`

