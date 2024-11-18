import pygame
import os

# ---------------------------------------- Paramètres ----------------------------------------------- #
screen_width, screen_height = 1080, 720
taille_tuile = 30  # 36x24 Tile pour dimension de 1080x720
joueur_x, joueur_y = (0,) * 2
# --------------------------------------------------------------------------------------------------- #


# ------------------------ Importation des images (Buttons / blocs / props...) ------------------------ #
logo = pygame.image.load("logo.png")
Titre_bloc = pygame.image.load("assets/Buttons/Titre_bloc.png")
bouton_jouer_img = pygame.image.load("assets/Buttons/Jouer.png")
bouton_quitter_img = pygame.image.load("assets/Buttons/Quitter.png")
bouton_rejouer_img = pygame.image.load("assets/Buttons/Rejouer.png")
bouton_reprendre_img = pygame.image.load("assets/Buttons/Reprendre.png")
bouton_menu_img = pygame.image.load("assets/Buttons/Menu.png")
bouton_new_game_img_1 = pygame.image.load("assets/Buttons/New_game_1.png")
bouton_new_game_img_2 = pygame.image.load("assets/Buttons/New_game_2.png")
bouton_load_game_img_1 = pygame.image.load("assets/Buttons/Load_game_1.png")
bouton_load_game_img_2 = pygame.image.load("assets/Buttons/Load_game_2.png")
bouton_scoreboard_img_1 = pygame.image.load("assets/Buttons/Scoreboard_1.png")
bouton_scoreboard_img_2 = pygame.image.load("assets/Buttons/Scoreboard_2.png")
bouton_profile_1_img_1 = pygame.image.load("assets/Buttons/profile_1_1.png")
bouton_profile_1_img_2 = pygame.image.load("assets/Buttons/profile_1_2.png")
bouton_profile_2_img_1 = pygame.image.load("assets/Buttons/profile_2_1.png")
bouton_profile_2_img_2 = pygame.image.load("assets/Buttons/profile_2_2.png")
bouton_profile_3_img_1 = pygame.image.load("assets/Buttons/profile_3_1.png")
bouton_profile_3_img_2 = pygame.image.load("assets/Buttons/profile_3_2.png")
fleche_img = pygame.image.load("assets/Buttons/fleche.png")

texte_intro_1 = pygame.image.load("assets/Texts/texte_intro_1.png")
texte_intro_2 = pygame.image.load("assets/Texts/texte_intro_2.png")
texte_intro_3 = pygame.image.load("assets/Texts/texte_intro_3.png")
texte_cle = pygame.image.load("assets/Texts/texte_cle.png")
texte_boss = pygame.image.load("assets/Texts/texte_centipede.png")
texte_ha = pygame.image.load("assets/Texts/ha.png")
texte_cine_bob_1 = pygame.image.load("assets/Texts/texte_cine_bob_1.png")
texte_cine_bob_2 = pygame.image.load("assets/Texts/texte_cine_bob_2.png")
texte_cine_vi_1 = pygame.image.load("assets/Texts/texte_cine_vi_1.png")
texte_cine_vi_2 = pygame.image.load("assets/Texts/texte_cine_vi_2.png")
texte_cine_vi_3 = pygame.image.load("assets/Texts/texte_cine_vi_3.png")
texte_cine_vi_4 = pygame.image.load("assets/Texts/texte_cine_vi_4.png")
texte_cine_vi_5 = pygame.image.load("assets/Texts/texte_cine_vi_5.png")
texte_cine_vi_6 = pygame.image.load("assets/Texts/texte_cine_vi_6.png")
texte_cine_bob_3 = pygame.image.load("assets/Texts/texte_cine_bob_3.png")
texte_cine_bob_4 = pygame.image.load("assets/Texts/texte_cine_bob_4.png")
texte_cine_bob_5 = pygame.image.load("assets/Texts/texte_cine_bob_5.png")
texte_cine_bob_6 = pygame.image.load("assets/Texts/texte_cine_bob_6.png")
texte_cine_bob_7 = pygame.image.load("assets/Texts/texte_cine_bob_7.png")

background_night = pygame.image.load("background_night.png")
background_night_cine_1 = pygame.image.load("background_night_cine_1.png")
background_night_cine_2 = pygame.image.load("background_night_cine_2.png")
background_night_flou = pygame.image.load("background_night_flou.png")
background_cave = pygame.image.load("background_cave.png")
background_pause = pygame.image.load("background_pause.png")
background_off = background_night
black_circle = pygame.image.load("black-circle.png")
vide_img = pygame.image.load("assets/entities/Tile_2/Tile_0.png")
cristaux_img = pygame.image.load("assets/entities/cristaux_2/cristal_1.png")
caillou_img = pygame.image.load("assets/entities/caillou_2/1.png")
nuage_img = pygame.image.load("assets/nuages/cloud_night.png")
BarreDeVie0 = pygame.image.load("BarreDeVie0.png")
BarreDeVie1 = pygame.image.load("BarreDeVie1.png")
BarreDeVie2 = pygame.image.load("BarreDeVie2.png")
BarreDeVie3 = pygame.image.load("BarreDeVie3.png")
game_over = pygame.image.load("game_over.png")

dico = {}
L_assets = ["Tile", "cave", "boxe", "fence", "ladder", "pointer", "lamp", "flag", "arch", "pillar",
            "wagon", "chest", "crystal", "caillou", "plante"]

# Création d'un dictionnaire des assets, chacun associé à un ID (la clé du dico)
k = 1
for assets in L_assets:
    fichiers = os.listdir("assets/{}".format(assets))
    cpt_fichiers = len(fichiers)  # Compteur du nombre de fichiers existants dans le dossier
    for i in range(1, cpt_fichiers + 1):
        # Importation des assets dans le dico
        dico[k] = pygame.image.load("assets/{}/{}_{}.png".format(assets, assets, i))
        k += 1
# ------------------------------------------------------------------------------------------------ #


