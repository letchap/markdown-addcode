
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re
import codecs


# The regex to find where to add the code. In my pages, it looks like {% addcode content/code/addcode.py %}

CODE_RE = re.compile(r'\{% addcode ?(?P<src>[^\}]*) \%}')

class AddCodePreprocessor(Preprocessor):

    def run(self, lines):
        new_lines = [];
        for line in lines:                                              # I read the file containing the code and add the content to my markdown file
            m = CODE_RE.match(line)
            if m:
                filein = m.group('src')
                for line in codecs.open(filein, 'r', encoding="utf-8"):
                    new_lines.append('    ' + line.rstrip())            # 4 spaces added to have blockcode in the markdown file
            else:
                new_lines.append(line)
        return new_lines


class AddCodeExtension(Extension):
# declare extension (addcode)
    def extendMarkdown(self, md):
        md.preprocessors.register(AddCodePreprocessor(md), 'addcode', 10)
        md.registerExtension(self)

def makeExtension():
    return AddCodeExtension()
