# coding: utf-8

# ======================================================
# * ... Outils
# ------------------------------------------------------
# * ... Ce module contient une collection d'outils
# * ... annexes utiles pour notre programme.
# ======================================================

# ---------------------------------
# * ... Importation des constantes
# ---------------------------------

from components import config


# ===================================================================
# * ... Vocab (Computation)
# -------------------------------------------------------------------
# * ... Cette méthode permet de renvoyer les affichages
# * ... fréquents stockés dans notre dictionnaire et de simplement
# * ... gérer plusieurs langues.
# ===================================================================


def vocab(flag, lang=''):

    """Dictionnaire contenant le vocabulaire de l'application en plusieurs langues.
    Utilisez les symboles adéquats.
    Par exemple : flag="ErreurSaisie" et lang="FR". Lang a pour valeur par défaut la valeur courante."""

    # * ... Met à jour l'argument lang si l'utilisateur laisse courir.
    if not lang:
        lang = config.language

    if lang == 'FR':
        dictionnary = config.DICO_FR
    elif lang == 'EN':
        dictionnary = config.DICO_EN
    return dictionnary.get(flag, dictionnary.get('ErreurDictionnaire'))


# =============================================================================
# * ... Is String of Digits ? (Command)
# -----------------------------------------------------------------------------
# * ... Cette méthode sert à vérifier si une chaîne de caractères ne contient
# * ... que des nombres entiers
# =============================================================================


def is_string_of_digits(s):
    """Retourne True si tous les caractères d'une string sont bien des digits."""
    import re

    # * ... Retourne False si la chaîne de caractère est vide.
    if not s:
        return s

    # * ... Vérifie si la chaîne ne contient que des digits.
    for i in range(len(s)):
        if not re.match('\d', s[i]):
            return False

    # * ... Il n'y a pas eu de return jusqu'à présent. On retourne donc true.
    return True


# ===============================================================================
# * ... Represent my Array (Effect)
# -------------------------------------------------------------------------------
# * ... Cette méthode sert à créer la représentation de l'array.
# ===============================================================================

def represent_my_array(flag, src):
    head = vocab('EnTeteTableau')
        
    if flag == 'indexlist':

        # * ... Vérifie si l'on va devoir utiliser l'affichage dynamique.

        if config.RESCUE_MODE:
            if not config.MAX_LINES > 0:
                config.MAX_LINES = 1
                print('RESCUE') # * ... Pas encore d'error handling,
                                # * ... je ne connais encore suffisamment Python pour raise. :'(
            
        dynamic_display = config.OPT_DISPLAY and config.MAX_LINES > 0

        if dynamic_display:
            distance = len(src)
            head *= 2 # * {UNSAFE} head *= times
            times = (len(src) // config.MAX_LINES)

        stack = list(src)
        
        tail = []
        index = 0
        
        # * ... Balayage de la stack.
        while(len(stack) > 0):
            index += 1
            element = stack[0] 
            stack.remove(element)
            
            # * ... Représentation d'une liste de caractères selon leur index.
            tail.append(generate_line(element))

            if dynamic_display:

                # * ... Génère le suffixe, sauf si la stack est déjà vide.
                if len(stack) > 0:

                    dyn_index = index - 1 + (distance//2)

                    if len(src) > dyn_index:
                        element = src[dyn_index]
                        suffix = generate_line(element)
                        
                        # * ... Ajoute le suffixe à la ligne qui vient d'être générée.
                        tail[-1] += suffix
                        stack.remove(element)
                    
        return {'head': head, 'tail': tail}
    else:

        # * ... Représentation d'un seul caractère.

        # * ... Si l'utilisateur a entré un index, on le convertit en nombre entier.
        if flag == 'index':
            src = int(src)

        # * ... Si l'utilisateur a entré un chr (on aurait aussi pu faire if flag == "chr"),
        # * ... on convertit son chr avec ord.
        if not isinstance(src, int):

            # * ... Convertit la clé en index ANSI.
            src = ord(src)

        tail = []
        tail.append(generate_line(src))
        return {'head': head, 'tail': tail}


def generate_line(index):
    character = chr(index)
    binary, hexa =\
        bin(ord(character)), hex(ord(character))

    if index in config.ANSI_SYMBOLS:
        character = config.ANSI_SYMBOLS[index]
    return [index, ascii(chr(index)), hexa, binary, character]

# ========================================================================================
# * ... Choice (Effect)
# ----------------------------------------------------------------------------------------
# * ... Cette méthode permet de modéliser un choix et renvoie celui de l'utilisateur.
# ========================================================================================


def choice(question, *args):
    """Gestion des choix (non sensible à la casse).
    Ecrivez '[free]' comme deuxième argument pour obtenir un choix libre."""

    # * ... Stocke le contenu de args.
    old_args = args
    choix = -1
    choix_libre = args[0].lower() == '[free]'

    # * ... Vérifie si la question est un symbole contenu dans le dictionnaire ou non.
    if vocab(question) != -1:

        # * ... Dans le cas où la question est référencée.
        question = vocab(question)

    # * ... Retire les potentiels espaces superflus et en rajoute un en fin de question.
    question = question.strip()
    question += ' '

    # * ... Vérifie si le choix est libre ou non.
    if choix_libre:

        # * ... Affiche le message correspondant dans le cas où c'est le cas.
        liste_choix = vocab('ChoixLibre')
    else:

        # * ... Génère la liste de réponses sous forme de chaîne de caractères dans le cas contraire.

        # * ... Dessine le début de la liste de choix.
        liste_choix = '['
        for eachChoice in args:

            # * ... Ajoute le choix.
            liste_choix += eachChoice

            # * ... Dessine un séparateur si un autre choix reste à ajouter.
            if eachChoice != args[-1]:
                liste_choix += '/'

        # * ... Dessine la fin de la liste de choix.
        liste_choix += ']'

    # * ... Vérifie si le choix est libre ou non.
    if choix_libre:

        # * ... Ouvre le prompt et retourne directement la valeur si c'est le cas.
        input_value = input(question + liste_choix + '\n')
        return input_value

    # * ... Passe toutes les valeurs dans le args en minuscules afin de simplifier la lecture.
    args = []
    for eachChoice in old_args:
        args.append(str(eachChoice).lower())

    while choix == -1:

        # * ... Prompt
        input_value = input(question + liste_choix + '\n')
        input_value = input_value.lower()
        if input_value in args:
            choix = old_args[args.index(input_value)]
            # * ... On fait tandem entre les deux représenations de args pour ne pas être sensible à la casse.
        if choix == -1:
            print(vocab('ErreurSaisie'))
    return choix
