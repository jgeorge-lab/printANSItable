# coding: utf-8

# ============================================================
# * ... Config
# ------------------------------------------------------------
# Ce module contient toutes les constantes de configuration.
# Il contient aussi les dictionnaires.
# ============================================================


# * ... Constantes de configuration
RESCUE_MODE = True

# * ... Constantes de configuration
DEFAULT_LANGUAGE = 'FR'
MAX_ANSI_VALUE = 255
OPT_DISPLAY = True # * ... Set it to False if you don't want optimised display.
MAX_LINES = 1 # * ... Will be for a next version, maybe.

# * ... Variable locale dynamique
language = DEFAULT_LANGUAGE


# * ... Dictionnaires
ANSI_SYMBOLS =  {

                 0:     'NUL',  1:   'SOH',          2:     'STX',
                 3:     'ETX',  4:   'EOT',          5:     'ENQ',
                 6:     'ACK',  7:   'BEL',          8:     'BS' ,
                 9:     'HT' ,  10:  'LF' ,          11:    'VT' ,
                 12:    'FF' ,  13:  'CR' ,          14:    'SO' ,
                 15:    'SI' ,  16:  'DLE',          17:    'DC1',
                 18:    'DC2',  19:  'DC3',          20:    'DC4',
                 21:    'NAK',  22:  'SYN',          23:    'ETB',
                 24:    'CAN',  25:  'EM' ,          26:    'SUB',
                 27:    'ESC',  28:  'FS' ,          29:    'GS' ,
                 30:    'RS' ,  31:  'US' ,          32:    'SP' ,
                 
                 # * ... Clear caracters until the last one.

                 127:   'DEL',

                 # * ... ANSI:
                 128:   '€',    129: 'UNDEFINED',   130:    ',',
                 131:   'ƒ',    132: '„',           133:    '…',
                 134:   '†',    135: '‡',           136:    'ˆ',
                 137:   '‰',    138: 'Š',           139:    '‹',
                 140:   'Œ',    141: 'UNDEFINED',   142:    'Ž',
                 143:   'UNDEFINED',
                 144:   'UNDEFINED',
                 145:   '‘',    146: '’',           147:    '“',
                 148:   '”',    149: '•',           150:    '–',
                 151:   '—',    152: '˜',           153:    '™',
                 154:   'š',    155: '›',           156:    'œ',
                 157:   'UNDEFINED',
                 158:   'ž',    159: 'Ÿ',           160:    'No-break Space'

                 # * ... lol, the ANSI table almost looks like a svastika...
                 
                 }


# * ... (i18n un peu pauvre)
DICO_FR = {
            # * ... UI.
            'ErreurSaisie':             '\n'                                                +\
                                        '+-----------------------------------------+\n'     +\
                                        '| /!\\ Vous avez fait une erreur de saisie.|\n'    +\
                                        '+-----------------------------------------+\n',
            'DernierChar':              'Nous allons directement vous afficher le dernier caractère de la table ANSI.',
            'StartpointPareilEndpoint': 'Votre point de départ et d\'arrivée sont les mêmes.\n' +
                                        'Nous ne vous afficherons que le caractère correspondant.\n',
            'EnTeteTableau':            ['INDEX', 'ASCII()', 'HEXADECIMAL', 'BINAIRE', 'CARACTERE'],
            'ConfirmMultiCara':         'Bien ! Vous souhaitez donc récupérer plusieurs caractères.\n',
            'ConfirmSoloCara':          'Bien ! Vous souhaitez donc récupérer un seul caractère.\n',
            'MessageBienvenue':         '-----------------------------------------------------------------------------------------------\nBienvenue dans ce merveilleux programme qui vous fera peut-être vous passer d\'internet.\nCelui-ci vous permet de poser des interrogations à la table ANSI.\n-----------------------------------------------------------------------------------------------\n',
            # * ... ^ C'est vraiment pas très Charlie de faire un truc pareil. Mais il existe....
            'MessageBienvenue':         '-----------------------------------------------------------------------------------------------\n' +\
                                        'Bienvenue dans ce merveilleux programme qui vous fera peut-être vous passer d\'internet.\n' +\
                                        'Celui-ci vous permet de poser des interrogations à la table ANSI.\n' +\
                                        '-----------------------------------------------------------------------------------------------\n',
            # * ... Une façon bien plus Charlie de l'écrire.
            'EOF':                      'Appuyez sur la touche Entrée pour quitter ce programme.',

            # * ... Choices.
            'UnSeulCaractère':          'Souhaitez-vous ne récupérer qu\'un seul charactère ? ',
            'RechercheParIndex':        'Souhaitez-vous faire une recherche par index ?',
            'EcrireCaractère':          'Veuillez écrire votre caractère :',
            'EcrireIndex':              'Veuillez écrire un index (min : 0, max : ' + str(MAX_ANSI_VALUE) + ') :',
            'PremierIndex':             'Veuillez entrer l\'index du premier caractère (min : 0, max : ' + str(MAX_ANSI_VALUE) + ') :',
            'SecondIndex':              'Veuillez entrer l\'index du second caractère (min : votre point de départ, max : ' + str(MAX_ANSI_VALUE) + ') :',
            'ChoixLibre':               '\n[Ce choix est libre. Veuillez entrer la valeur souhaitée...]',

            # vvv [DON'T EDIT THIS LINE] vvv #
                 'ErreurDictionnaire': -1
            # ^^^ [DON'T EDIT THIS LINE] ^^^ #
}

DICO_EN = {
            # * ... UI.
            'ErreurSaisie':             '\n'                                    +\
                                        '+-------------------------------+\n'   +\
                                        '| /!\\ You made an input mistake.|\n'  +\
                                        '+-------------------------------+\n',
            'DernierChar':              'We will show you the last character of the ANSI table.',
            'StartpointPareilEndpoint': 'Your entry and exit points are the same.\n' +
                                        'We only will show the corresponding character.\n',
            'EnTeteTableau':            ['INDEX', 'ASCII()', 'HEXADECIMAL', 'BINARY', 'CHARACTER'],
            'ConfirmMultiCara':         'Good! Hence, you want several characters.\n',
            'ConfirmSoloCara':          'Good! Hence, you want only one character.\n',
            'MessageBienvenue':         '--------------------------------------------------------------------------------------------------\nWelcome in this fabulous program which will perhaps make you solve your problem without internet.\nIt allows you to retrieve values in the ANSI table.\n--------------------------------------------------------------------------------------------------\n',
            # * ... ^ It's not very Charlie to do such an horrible thing. But there is...
            'MessageBienvenue':         '--------------------------------------------------------------------------------------------------\n'  +\
                                        'Welcome in this fabulous program which will perhaps make you solve your problem without internet.\n'   +\
                                        'It allows you to retrieve values in the ANSI table.\n'                                                 +\
                                        '--------------------------------------------------------------------------------------------------\n',
            # * ... A way Charliest way to write it.
            'EOF':                      'Press the ENTER key to exit this program.\nSpecial thanks to Mr. Jacob for giving us this exercice! \n(Yes, that\'s an Easter Egg, because you wanted to see if this program were really multilingual).',

            # * ... Choices.
            'UnSeulCaractère':          'Would you want to get only one character? ',
            'RechercheParIndex':        'Would you like to make an index search?',
            'EcrireCaractère':          'Please, write your character:',
            'EcrireIndex':              'Please, write an index (min: 0, max: ' + str(MAX_ANSI_VALUE) + '):',
            'PremierIndex':             'Please, enter your first character\'s index (min: 0, max: ' + str(MAX_ANSI_VALUE) + '):',
            'SecondIndex':              'Please, enter your second character\'s index (min: your entry point, max: ' + str(MAX_ANSI_VALUE) + '):',
            'ChoixLibre':               '\n[This is a free choice. Please, put the value you want...]',

            # vvv [DON'T EDIT THIS LINE] vvv #
                 'ErreurDictionnaire': -1
            # ^^^ [DON'T EDIT THIS LINE] ^^^ #
}
