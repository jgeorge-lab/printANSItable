# coding: utf-8

"""
Par    : Julien GEORGE.
Le     : 01/12/2019.
Contact: jgBtsSio@gmail.com
Version: 4.0


* * * * * * * * 
 [ CHANGELOG ]
* * * * * * * * 

v. 1.0, 01/12/2019
N'affiche pas correctement les 33 premiers éléments de la table ANSI.

v. 2.0, 02/12/2019
Ajout d'un dictionnaire de symboles ANSI dans config.py pour aider Python dans son affichage.

v. 3.0, 02/12/2019
Dictionnaire de symboles ANSI réalisé intégralement.

v. 4.0, 02/12/2019
Optimisation de l'utilisation de l'écran (UNSAFE).

- J'aime perdre mon temps à faire du code "over-engineer" en écoutant des musiques
 insoutenables comme : https://www.youtube.com/watch?v=TKfS5zVfGBc
                  ou : https://www.youtube.com/watch?v=iVcG8bJBkKk
                  (Merci à King Kadelfek, AKA Marc Kruzik pour la découverte...)

v. 5.0, 02/12/2019 (coming soon)
Optimisation++ de l'utilisation de l'écran.

* * *

- J'aime perdre mon temps à faire du code "over-engineer" en écoutant des musiques
 insoutenables comme : https://www.youtube.com/watch?v=TKfS5zVfGBc
                  ou : https://www.youtube.com/watch?v=iVcG8bJBkKk
                  (Merci à King Kadelfek, AKA Marc Kruzik pour la découverte...)

* * *

Ce programme permet de sommairement manipuler la table ANSI...
Premièrement, il demande à l'utilisateur s'il veut obtenir un intervalle de caractères ou seulement un seul.
Si l'utilisateur choisit de n'avoir qu'un seul résultat, il peut même directement écrire un caractère.
Ensuite, le programme gère l'affichage de ce qui a été demandé.

Programme dispo en Français comme en Anglais.
(Grâce à des rustines pas très belles).
"""

# * ... Anecdote très instructive : afficher le 7e caractère de la table
# * ... ASCII fait jouer un son de notification à mon Windows 10.
# * ... Je trouve ça très amusant.
# * ... (Il s'agit du char "Bell").

from components.tools import vocab, is_string_of_digits, represent_my_array, choice
from dependencies.tabulate import tabulate

from components import config
from components.config import MAX_ANSI_VALUE
import re

# -------------------------------
# * ... Message d'introduction
# -------------------------------

choix = choice('[EN] Choose your language!\n[FR] Choisissez votre langue!', 'FR', 'EN')
config.language = choix.upper()

print(vocab('MessageBienvenue'))

# -------------------------------------------------
# * ... {Interaction} Choix de l'utilisateur.
# * ... [Rang de caractères, caractère unique]
# -------------------------------------------------

unSeulCaractere = choice('UnSeulCaractère', 'O', 'n')

if unSeulCaractere.lower() == 'o':
    unSeulCaractere = True
else:
    unSeulCaractere = False

if not unSeulCaractere:

    # * ... L'utilisateur souhaite récupérer plusieurs caractères.
    print(vocab('ConfirmMultiCara'))

    # ------------------------------------------------------------
    # * ... {Interaction} Choix de l'utilisateur.
    # * ... ['free']
    # * ... On fait définir un point de départ à l'utilisateur.
    # ------------------------------------------------------------

    startpoint = ''
    while not is_string_of_digits(startpoint) or int(startpoint) < 0 or int(startpoint) > MAX_ANSI_VALUE:
        startpoint = choice('PremierIndex', '[free]')
        if not is_string_of_digits(startpoint) or int(startpoint) < 0 or int(startpoint) > MAX_ANSI_VALUE:
            print(vocab('ErreurSaisie'))

    startpoint = int(startpoint)

    if startpoint == MAX_ANSI_VALUE:

        # * ... L'utilisateur a demandé le dernier élément de la table ANSI.
        print(vocab('DernierChar'))
        endpoint = startpoint

    else:

        # * ... L'utilisateur n'a pas demandé le dernier élément de la table ANSI.
        # * ... On lui fait donc définir un point de fin.

        # ------------------------------------------------------------
        # * ... {Interaction} Choix de l'utilisateur.
        # * ... ['free']
        # * ... On fait définir un point de fin à l'utilisateur.
        # ------------------------------------------------------------

        endpoint = ''
        while not is_string_of_digits(endpoint) or int(endpoint) < 0 or int(endpoint) > MAX_ANSI_VALUE or int(endpoint) < startpoint:
            endpoint = choice('SecondIndex', '[free]')
            if not is_string_of_digits(endpoint) or int(endpoint) < 0 or int(endpoint) > MAX_ANSI_VALUE or int(endpoint) < startpoint:
                print(vocab('ErreurSaisie'))

        endpoint = int(endpoint)

        if startpoint == endpoint:
            
            # * ... Affichage d'un message d'alerte si le point de fin et le point de départ sont les mêmes.
            print(vocab('StartpointPareilEndpoint'))

else:

    # * ... L'utilisateur ne souhaite récupérer qu'un seul caractère.
    print(vocab('ConfirmSoloCara'))

    # ----------------------------------------------------------------
    # * ... {Interaction} Choix de l'utilisateur.
    # * ... [Recherche par index, Recherche par caractère]
    # * ... L'utilisateur souhaite ne récupérer qu'un seul caractère.
    # ----------------------------------------------------------------

    choix = choice(vocab('RechercheParIndex'), 'O', 'n')
    rechercheParIndex = False
    if choix.lower() == 'o':
        rechercheParIndex = True

    choix = ''
    # * ... Reset du choix.

    if not rechercheParIndex:

        # * ... Recherche par caractère.

        while len(choix) != 1:

            # * ... Choix du caractère.
            choix = choice('EcrireCaractère', '[free]')
            if len(choix) != 1:
                print(vocab('ErreurSaisie'))
    else:

        # * ... Recherche par index.
        while not is_string_of_digits(choix):

            # * ... Choix de l'index.
            choix = choice('EcrireIndex', '[free]')
            if not is_string_of_digits(choix):
                print(vocab('ErreurSaisie'))

if unSeulCaractere:
    if rechercheParIndex:

        # * ... Recherche par index.
        representation = represent_my_array('index', choix)
    else:

        # * ... Recherche par caractère.
        representation = represent_my_array('chr', str(choix))

else:

    # * ... L'utilisateur a demandé un rang.
    charlist = []  # * ... Stocke la liste des caractères demandés.
    for index in range(startpoint, endpoint + 1):
        charlist.append(index)

    charlist = list(range(startpoint, endpoint+1))

    representation = represent_my_array('indexlist', charlist)

# * ... Dessine le tableau.

print(
 tabulate(representation['tail'],
          representation['head'],
          tablefmt='fancy_grid',
          stralign='center')
)

input(vocab('EOF'))
