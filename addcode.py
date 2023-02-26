
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re
import codecs


# L'expression régulière permettant de trouver le tag dans le texte

CODE_RE = re.compile(r'\{% addcode ?(?P<src>[^\}]*) \%}')

class AddCodePreprocessor(Preprocessor):

# Le pré-processor
# Je lis les lignes de mon fichier markdown
# Je les mets une à une dans une liste
# Dès que je trouve une correspondance à mon expression régulière
# J'ouvre le fichier source
# Je le lis ligne à ligne en ajoutant une indentation de 4 espaces pour # le bloc de code markdown
# Je complète ma liste avec ces lignes
# Quand j'ai tout lu, je renvoie la liste pour la suite du traitement
# markdown

    def run(self, lines):
        new_lines = [];
        for line in lines:
            m = CODE_RE.match(line)
            if m:
                filein = m.group('src')
                for line in codecs.open(filein, 'r', encoding="utf-8"):
                    new_lines.append('    ' + line.rstrip())
            else:
                new_lines.append(line)
        return new_lines


class AddCodeExtension(Extension):
# Déclaration de mon extension
    def extendMarkdown(self, md):
        md.preprocessors.register(AddCodePreprocessor(md), 'addcode', 10)
        md.registerExtension(self)

def makeExtension():
    return AddCodeExtension()
