import random
import time

import pygame.sprite

from settings import *  # Importation des paramètres

# Niveaux intro 0
from niveau_0_0_data import *  # Importation des données du niveau
from niveau_0_1_data import *
from niveau_0_2_data import *
from niveau_0_3_data import *

# Niveau 1
from niveau_1_0_data import *

# Niveau 2
from niveau_2_0_data import *
from niveau_2_1_data import *

# Niveau 3
from niveau_3_0_data import *

# Niveau 4
from niveau_4_0_data import *

# Niveau 5
from niveau_5_0_data import *

# Niveau 6
from niveau_6_0_data import *

pygame.init()  # Lancement du module Pygame et création de la fenêtre

# Initialisation de la musique dans le jeu
pygame.mixer.init()
# Musique de fond, -1 pour répétition infinie, 0 pour le premier canal afin de pouvoir mettre plusieurs sons en même temps
pygame.mixer.Channel(0).play(pygame.mixer.Sound("muse.mp3"), -1)

# Configurations
screen = pygame.display.set_mode(
    (screen_width, screen_height))  # Création de la fenêtre (note : + pygame. FULLSCREEN pour plein écran)
pygame.display.set_caption("Super Miner Bros.")  # Titre de la fenêtre
clock = pygame.time.Clock()  # Création d'une horloge pour limiter le nombre de FPS


# Fonctions
def get_niveau(profil):  # Fonction qui permet de récupérer le niveau en fonction du profil
    with open("save.txt", 'r') as fr:
        lignes = fr.read()
        profil_niveau = lignes.split("profile:")[profil]
    Niveau_off = profil_niveau.replace("\n", "")
    return Niveau_off


def save_niveau(profil, niveau):  # Fonction qui permet de sauvegarder le niveau en fonction du profil
    with open("save.txt", 'r') as fr:
        lignes = fr.readlines()
    with open("save.txt", 'w') as fw:
        lignes[profil - 1] = "profile:" + str(niveau) + "\n"
        for ligne in lignes:
            fw.write(ligne)


def grille():  # Création de lignes formant une grille en fonction de la taille des tuiles définie
    for line in range(0, 40):
        pygame.draw.line(screen, (255, 0, 255), (0, line * taille_tuile), (screen_width, line * taille_tuile))
        pygame.draw.line(screen, (255, 0, 255), (line * taille_tuile, 0), (line * taille_tuile, screen_height))


def tuile_bloc(bloc, cpt_colonne, cpt_ligne, tuile_list, id):  # Fonction crée un tuple d'informations des tuiles
    # Redimensionne à la bonne taille de tuile définie
    img = pygame.transform.scale(bloc, (taille_tuile, taille_tuile))
    # Création d'un tuple d'informations des tuiles
    img_rect = img.get_rect()
    img_rect.x = cpt_colonne * taille_tuile
    img_rect.y = cpt_ligne * taille_tuile
    tuile = (img, img_rect, id)
    tuile_list.append(tuile)


def dialogue_1(dialogue_off, Niveau_off, cpt_off, cpt_2_off,
               game_pause_off):  # Fonction création de dialogue.
    texte = texte_intro_1
    if Niveau_off == 1:
        texte = texte_intro_2
    if Niveau_off == 2:
        texte = texte_intro_3
    if Niveau_off == 5 or Niveau_off == 6:
        texte = texte_cle
    if Niveau_off == 10:
        texte = texte_boss
    touche = pygame.key.get_pressed()
    if (touche[pygame.K_LEFT] or touche[pygame.K_RIGHT] or touche[pygame.K_SPACE]) and not game_pause_off:
        cpt_off += 1
    if cpt_off > 20:
        dialogue_off = not dialogue_off
        cpt_off = 0

    screen.blit(texte.convert_alpha(), (-175, -475))

    return dialogue_off, cpt_off, cpt_2_off


def dialogue_2(new_intro, cpt_off, cpt_2_off, Mort_off, go_off, go_2_off, go_3_off, dx_off,
               dy_off, dx_2_off, dy_2_off, dx_3_off, dy_3_off, end_vgo_cine_off):
    # Fonction création de dialogue
    if Mort_off == 3:
        if pygame.key.get_pressed()[pygame.K_a] and cpt_2_off == 0 and cpt_off == 0:
            cpt_2_off = 1
        if cpt_2_off == 0:
            texte_intro = pygame.image.load("assets/Texts/texte_cine_bob_1.png")
        elif cpt_2_off == 1 and cpt_off == 0:
            texte_intro = pygame.image.load("assets/Texts/texte_cine_bob_2.png")

        if pygame.key.get_pressed()[pygame.K_b] and cpt_off == 0:
            cpt_off = -1
        if cpt_off == -1:
            texte_intro = pygame.image.load("assets/Texts/texte_cine_vi_1.png")

        if pygame.key.get_pressed()[pygame.K_a] and cpt_off == -1:
            cpt_off = 2
        if cpt_off == 2:
            texte_intro = pygame.image.load("assets/Texts/texte_cine_bob_3.png")

        if pygame.key.get_pressed()[pygame.K_b] and cpt_off == 2:
            cpt_off = 3
        if cpt_off == 3:
            texte_intro = pygame.image.load("assets/Texts/texte_cine_bob_4.png")

        if pygame.key.get_pressed()[pygame.K_a] and cpt_off == 3:
            cpt_off = 4
        if cpt_off == 4:
            texte_intro = pygame.image.load("assets/Texts/texte_cine_vi_2.png")

        if pygame.key.get_pressed()[pygame.K_b] and cpt_off == 4:
            cpt_off = 5
        if cpt_off == 5:
            texte_intro = pygame.image.load("assets/Texts/texte_cine_bob_5.png")

        if pygame.key.get_pressed()[pygame.K_a] and cpt_off == 5:
            cpt_off = 6
        if cpt_off == 6:
            texte_intro = pygame.image.load("assets/Texts/texte_cine_bob_6.png")

        if pygame.key.get_pressed()[pygame.K_b] and cpt_off == 6:
            cpt_off = 7
        if cpt_off == 7:
            texte_intro = pygame.image.load("assets/Texts/texte_cine_vi_3.png")

        if pygame.key.get_pressed()[pygame.K_a] and cpt_off == 7:
            cpt_off = 8
        if cpt_off == 8:
            texte_intro = pygame.image.load("assets/Texts/texte_cine_vi_4.png")

        if pygame.key.get_pressed()[pygame.K_b] and cpt_off == 8:
            cpt_off = 9
        if cpt_off == 9:
            texte_intro = pygame.image.load("assets/Texts/texte_cine_vi_5.png")

        if pygame.key.get_pressed()[pygame.K_a] and cpt_off == 9:
            cpt_off = 10
        if cpt_off == 10:
            texte_intro = pygame.image.load("assets/Texts/texte_cine_vi_6.png")

        if pygame.key.get_pressed()[pygame.K_b] and cpt_off == 10:
            cpt_off = 11
        if cpt_off == 11:
            texte_intro = pygame.image.load("assets/Texts/texte_cine_bob_7.png")
            go_off, go_2_off, go_3_off, dx_off, dy_off, dx_2_off, dy_2_off, dx_3_off, dy_3_off = HA.event(go_off,
                                                                                                          go_2_off,
                                                                                                          go_3_off,
                                                                                                          dx_off,
                                                                                                          dy_off,
                                                                                                          dx_2_off,
                                                                                                          dy_2_off,
                                                                                                          dx_3_off,
                                                                                                          dy_3_off)

        if pygame.key.get_pressed()[pygame.K_a] and cpt_off == 11:
            end_vgo_cine_off = True

        screen.blit(texte_intro.convert_alpha(), (-175, -475))

        return new_intro, cpt_off, cpt_2_off, go_off, go_2_off, go_3_off, dx_off, dy_off, dx_2_off, dy_2_off, dx_3_off, dy_3_off, end_vgo_cine_off


def reset_niveau(Niveau_off):  # Niveau suivant

    # Supprimer les entités existantes à chaque nouveau niveau
    ennemi_groupe.empty()
    vide_groupe.empty()
    pnj_groupe.empty()
    caillou_groupe.empty()
    sortie_groupe.empty()
    sortie_2_groupe.empty()

    # Génération arrière-plan / Monde / Coordonnées d'apparition du joueur en fct du niveau
    dico_niveaux = {
        # Niveaux introduction
        0: {"Niveaux": [lvl0_0_1, lvl0_0_2, lvl0_0_3], "Coordonnées": (65, 540), "Background": background_night},
        1: {"Niveaux": [lvl0_1_1, lvl0_1_2, lvl0_1_3], "Coordonnées": (65, 540), "Background": background_night},
        2: {"Niveaux": [lvl0_2_1, lvl0_2_2, lvl0_2_3], "Coordonnées": (65, 540), "Background": background_night},
        3: {"Niveaux": [lvl0_3_1, lvl0_2_2, lvl0_2_3], "Coordonnées": (870, 520), "Background": background_night},

        # Niveau 1
        4: {"Niveaux": [lvl1_1, lvl1_2, lvl1_3], "Coordonnées": (65, 550), "Background": background_cave},
        5: {"Niveaux": [lvl2_1, lvl2_2, lvl2_3], "Coordonnées": (65, 550), "Background": background_cave},
        6: {"Niveaux": [lvl2_1_2, lvl2_2_2, lvl2_3_2], "Coordonnées": (975, 42), "Background": background_cave},
        7: {"Niveaux": [lvl3_1, lvl3_2, lvl3_3], "Coordonnées": (40, 450), "Background": background_cave},
        8: {"Niveaux": [lvl4_1, lvl4_2, lvl4_3], "Coordonnées": (65, 550), "Background": background_cave},
        9: {"Niveaux": [lvl5_1, lvl5_2, lvl5_3], "Coordonnées": (65, 620), "Background": background_cave},
        10: {"Niveaux": [lvl6_1, lvl6_2, lvl6_3], "Coordonnées": (10, 600), "Background": background_cave},
    }

    world_off_1 = Monde(dico_niveaux[Niveau_off]["Niveaux"][0])  # Importation calque 1
    world_off_2 = Monde(dico_niveaux[Niveau_off]["Niveaux"][1])  # Importation calque 2
    world_off_3 = Monde(dico_niveaux[Niveau_off]["Niveaux"][2])  # Importation calque 3
    joueur_x_off = dico_niveaux[Niveau_off]["Coordonnées"][0]  # Importation coordonnée en x
    joueur_y_off = dico_niveaux[Niveau_off]["Coordonnées"][1]  # Importation coordonnée en y
    new_background = dico_niveaux[Niveau_off]["Background"]  # Importation background

    return world_off_1, world_off_2, world_off_3, new_background, joueur_x_off, joueur_y_off


def fade_inout(screen_width_off, screen_height_off, speed, direction_off):  # Fonction fade in/out
    fade = pygame.Surface((screen_width_off, screen_height_off))
    fade.fill((0, 0, 0))
    if direction_off == "in":
        alpha_off = 0
        while alpha_off < 60:  # Vitesse de fondu
            alpha_off += 2
            fade.set_alpha(alpha_off)
            screen.blit(fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(speed)
    else:
        pass
    return True


def screen_shaking(game_pause_off, rx_off, ry_off, cpt_off):  # Fonction écran qui tremble
    if not game_pause_off:
        if cpt_off < 200:
            cpt_off += 1
            if cpt_off % 5 == 0:
                rx_off += 1
                ry_off -= 1
            r1 = random.randint(rx_off, ry_off)
            r2 = random.randint(rx_off, ry_off)
            screen.blit(screen, (r1, r2))

    return rx, ry, cpt_off


# Class
class Bouton:  # Bouton Jouer
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clique = False

    def create(self, idd):  # Création du bouton
        action = False

        # Récupère position du pointeur de la souris et vérifie s'il entre dans la zone du bouton + avec le click
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clique:
                action = True
                self.clique = True
        # Permet de pouvoir re-cliquer sur le bouton s'il réapparaîtra
        if pygame.mouse.get_pressed()[0] == 0:
            self.clique = False
        # Importation de l'image du bouton
        screen.blit(self.image, self.rect)

        if pygame.key.get_pressed()[pygame.K_SPACE] and idd == 1:
            action = True
        # Récupérer valeur de "action" pour actionner le bouton ou non
        return action

    def create_and_on(self, img1, img2, idd):  # Création du bouton du titre
        # Importation de l'image du bouton
        if idd == 0:
            self.image = img1
        else:
            self.image = img2

        screen.blit(self.image, self.rect)

        # Récupère position du pointeur de la souris et vérifie s'il entre dans la zone du bouton sans le click
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            action = True
        else:
            action = False
        return action

    def on_click(self):  # Teste si le bouton est cliqué
        action = False
        if pygame.mouse.get_pressed()[0] == 1 and not self.clique:
            action = True
            self.clique = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clique = False
        return action


class Caillou(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.angle = random.randint(1, 360)
        self.image = pygame.transform.rotate(pygame.transform.scale(image, (48, 48)), self.angle)
        self.rect = self.image.get_rect()
        self.rect.x = 182
        self.rect.y = -50

    def update(self):
        self.rect.y += 20
        if self.rect.y > screen_height:
            caillou_groupe.remove(self)
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)  # Hit-box du caillou
        # Suppression du caillou après certaines coordonnées


class EventCaillou(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.time = 0

    def event(self):
        self.time += 1
        if self.time >= 100:
            caillou_groupe.add(Caillou(caillou_img))
            self.time = 0


class Monde:  # Création du monde et de l'environnement
    def __init__(self, data):  # Boucle de reconnaissance des blocs dans les listes niveaux
        self.tuile_list = []
        cpt_ligne = 0
        for ligne in data:
            cpt_colonne = 0
            for id in ligne:
                if type(id) == int and 1 <= id <= 285:
                    tuile_bloc(dico[id], cpt_colonne, cpt_ligne, self.tuile_list, id)

                if id == "sc":  # Scorpion ennemi
                    ennemi = Scorpion(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile - 15)
                    ennemi_groupe.add(ennemi)

                if id == "s":  # Slime ennemi
                    ennemi = Slime(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile)
                    ennemi_groupe.add(ennemi)

                if id == "b":  # Chauve-souris ennemie
                    ennemi = Bat(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile, False)
                    ennemi_groupe.add(ennemi)

                if id == "w":  # Wagon ennemi
                    wagon = Wagon(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile - 15)
                    ennemi_groupe.add(wagon)

                if id == "/":  # Vide
                    vide = Vide(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile + (taille_tuile // 2), vide_img)
                    vide_groupe.add(vide)

                if id == "c1" or id == "c2":  # Cristaux
                    cristaux = Cristaux(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile, cristaux_img, id)
                    vide_groupe.add(cristaux)

                if id == "v":  # Villageois
                    pnj = Villageois(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile - 15)
                    pnj_groupe.add(pnj)

                if id == ">":  # Sortie
                    sortie = RandomBloc(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile, vide_img)
                    sortie_groupe.add(sortie)

                if id == ">2":  # Sortie avec condition
                    sortie_2 = RandomBloc(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile, vide_img)
                    sortie_2_groupe.add(sortie_2)

                if id == "vgo":  # Cinématique
                    vgo = RandomBloc(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile, vide_img)
                    vgo_groupe.add(vgo)

                if id == "key":  # Clé
                    key = TheKey(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile)
                    key_groupe.add(key)

                if id == "key1":  # Clé
                    key1 = TheKey(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile)
                    key_groupe_1.add(key1)

                if id == "key2":  # Clé
                    key2 = TheKey(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile)
                    key_groupe_2.add(key2)

                if id == "key3":  # Clé
                    key3 = TheKey(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile)
                    key_groupe_3.add(key3)

                if id == "chest1":  # Coffre
                    chest = Coffre(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile - 15)
                    chest_groupe_1.add(chest)

                if id == "chest2":  # Coffre
                    chest = Coffre(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile - 15)
                    chest_groupe_2.add(chest)

                if id == "chest3":  # Coffre
                    chest = Coffre(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile - 15)
                    chest_groupe_3.add(chest)

                if id == "crystal":  # Crystal de Boss
                    crystal = Crystal(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile - 10)
                    crystal_groupe.add(crystal)

                if id == "boss":  # Boss ennemi
                    boss = Boss(cpt_colonne * taille_tuile, cpt_ligne * taille_tuile - 90)
                    boss_groupe.add(boss)

                cpt_colonne += 1
            cpt_ligne += 1

    def create(self):  # Création des blocs des niveaux
        for tuile in self.tuile_list:
            screen.blit(tuile[0], tuile[1])
            # pygame.draw.rect(screen, (255, 0, 255), tuile[1], 1)  # Hit-box des blocs


class Joueur:  # Création du joueur

    def __init__(self, x, y):
        self.images_mort_gauche, self.images_mort_droite = [], []
        self.image_mort = {"droite": [], "gauche": []}
        self.images_gauche, self.images_droite = [], []
        self.images_base = {"droite": [], "gauche": [], "droite_vgo": [], "gauche_vgo": []}
        self.index, self.index_2, self.index_3, self.cpt, self.cpt_2, self.cpt_3, self.index_2_cpt = (0,) * 7
        self.pause = False

        # Animation Base (= immobile)
        for num in range(1, 5):
            joueur_base_droite = pygame.image.load("assets/player/Idle/Idle_{}.png".format(num))
            joueur_base_droite = pygame.transform.scale(joueur_base_droite, (27, 48))  # Rescale
            joueur_base_gauche = pygame.transform.flip(joueur_base_droite, True, False)  # Effet miroir de l'image
            self.images_base["droite"].append(joueur_base_droite)
            self.images_base["gauche"].append(joueur_base_gauche)

        for num in range(5, 9):
            joueur_base_gauche = pygame.image.load("assets/player/Idle/Idle_{}.png".format(num))
            self.images_base["gauche_vgo"].append(joueur_base_gauche)
            joueur_base_droite = pygame.transform.flip(joueur_base_gauche, True, False)  # Effet miroir de l'image
            self.images_base["droite_vgo"].append(joueur_base_droite)

        # Animation Marche
        for num in range(1, 7):
            joueur_droite = pygame.image.load("assets/player/Walk/Walk_{}.png".format(num))
            joueur_droite = pygame.transform.scale(joueur_droite, (27, 48))
            joueur_gauche = pygame.transform.flip(joueur_droite, True, False)
            self.images_gauche.append(joueur_gauche)
            self.images_droite.append(joueur_droite)

        # Animation Mort
        for num in range(1, 5):
            joueur_mort_droite = pygame.image.load("assets/player/Death/Death_{}.png".format(num))
            joueur_mort_droite = pygame.transform.scale(joueur_mort_droite, (44, 56))
            joueur_mort_gauche = pygame.transform.flip(joueur_mort_droite, True, False)
            self.image_mort["droite"].append(joueur_mort_droite)
            self.image_mort["gauche"].append(joueur_mort_gauche)

        self.image = self.images_droite[self.index]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width() - 10  # *** modification à apporter ici
        self.width_off = self.image.get_width()
        self.height = self.image.get_height()
        self.v_y = 0
        self.direction = 0
        self.jump = False

    def update(self, Mort_off, key_taken_off, key_taken_off_1, key_taken_off_2, key_taken_off_3, crystal_taken_off,
               chest_opened_off,
               chest_opened_off_1, chest_opened_off_2, chest_opened_off_3, condition_next_off, check, can_pause_off,
               cine_fin_off, vie_boss_off):  # Physique
        if not check:
            dx_off = 0
            dy_off = 0
            vitesse_animation = 7

            if Mort_off == 0:  # Joueur vivant

                # Contrôles
                if not self.pause and not cine_fin_off:  # Vérification si le jeu est en pause
                    touche = pygame.key.get_pressed()
                    if touche[pygame.K_SPACE] and not self.jump:  # Si le joueur appuie sur espace et qu'il n'est pas en train de sauter
                        self.v_y = -24
                        self.jump = True
                    if touche[pygame.K_LEFT]:  # Si le joueur appuie sur la flèche gauche
                        dx_off -= 5  # On déplace le joueur vers la gauche
                        self.cpt += 1
                        self.direction = -1  # On change la direction du joueur
                    if touche[pygame.K_RIGHT]:  # Si le joueur appuie sur la flèche droite
                        dx_off += 5  # On déplace le joueur vers la droite
                        self.cpt += 1
                        self.direction = 1  # On change la direction du joueur
                    if not touche[pygame.K_LEFT] and not touche[pygame.K_RIGHT] \
                            or touche[pygame.K_LEFT] and touche[pygame.K_RIGHT]:  # Si le joueur ne bouge pas
                        self.cpt = 0
                        self.index = 0
                        if self.direction == 1:
                            self.image = self.images_droite[self.index]
                        if self.direction == -1:
                            self.image = self.images_gauche[self.index]
                    if not touche[pygame.K_LEFT] and not touche[pygame.K_RIGHT] \
                            and not touche[pygame.K_SPACE] and not self.jump:  # Si le joueur ne bouge pas et qu'il n'est pas en train de sauter
                        self.idle_animation(0)  # On lance l'animation de repos du joueur

                    # Menu pause
                    if touche[pygame.K_ESCAPE] and not self.pause and can_pause_off:
                        self.pause = True

                # Animation et direction
                if not self.pause:
                    self.cpt += 1
                    if self.cpt > vitesse_animation:
                        self.cpt = 0
                        self.index += 1
                        if self.index >= len(self.images_droite):
                            self.index = 0
                        if self.direction == 1:
                            self.image = self.images_droite[self.index]
                        if self.direction == -1:
                            self.image = self.images_gauche[self.index]

                # Poids et gravité
                if not self.pause:
                    self.v_y += 1.9
                    if self.v_y > 20:
                        self.v_y = 17
                    dy_off += self.v_y  # On ajoute la gravité au déplacement vertical

                # Collisions
                for tuile in world.tuile_list:
                    # Collisions en x
                    if tuile[1].colliderect(self.rect.x + dx_off, self.rect.y, self.width_off - 1.2,
                                            self.height):  # Si le joueur touche une tuile à gauche ou à droite
                        dx_off = 0
                    if tuile[2] != 39:
                        # Collisions en y
                        if tuile[1].colliderect(self.rect.x, self.rect.y + dy_off, self.width_off - 1.2,
                                                self.height):  # Si le joueur touche une tuile en dessous ou au-dessus
                            # 1 = rectangle / 0 = img
                            # Vérification si sous un sol = self.jump
                            if self.v_y < 0:
                                dy_off = tuile[1].bottom - self.rect.top
                                self.v_y = 0
                            # Vérification si sur le sol = fall
                            elif self.v_y >= 0:
                                dy_off = tuile[1].top - self.rect.bottom
                                self.v_y = 0
                                self.jump = False

                if self.rect.x == 0:
                    self.rect.x = 0

                # Vérification collision avec ennemis
                if pygame.sprite.spritecollide(self, vide_groupe, False) \
                        or pygame.sprite.spritecollide(self, ennemi_groupe, False) \
                        or pygame.sprite.spritecollide(self, caillou_groupe, False) \
                        or pygame.sprite.spritecollide(self, boss_groupe, False):
                    Mort_off = -1  # Joueur mort

                # Vérification collision avec la sortie
                if pygame.sprite.spritecollide(self, sortie_groupe, False):
                    Mort_off = 1  # Niveau suivant

                # Vérification collision bloc lançant l'animation avec villageois
                if pygame.sprite.spritecollide(self, vgo_groupe, False):
                    Mort_off = 2  # Lancement animation

                # Vérification collision avec la clé
                if pygame.sprite.spritecollide(self, key_groupe, False):
                    key_taken_off = 1  # Clé prise
                # Vérification collision avec la sortie avec condition
                if key_taken_off == 1:
                    if pygame.sprite.spritecollide(self, sortie_2_groupe, False):
                        condition_next_off = True  # Sortie avec condition + clé prise
                        Mort_off = 1
                        key_taken_off = -1

                if pygame.sprite.spritecollide(self, key_groupe_1, False):
                    key_taken_off_1 = 1  # Clé prise

                if pygame.sprite.spritecollide(self, key_groupe_2, False):
                    key_taken_off_2 = 1  # Clé prise

                if pygame.sprite.spritecollide(self, key_groupe_3, False):
                    key_taken_off_3 = 1  # Clé prise

                # Vérification collision avec le coffre avec condition
                if key_taken_off_1 == 1:
                    if pygame.sprite.spritecollide(self, chest_groupe_1, False):
                        chest_opened_off_1 = True  # Coffre ouvert
                        key_taken_off_1 = -1
                        vie_boss_off -= 1

                if key_taken_off_2 == 1:
                    if pygame.sprite.spritecollide(self, chest_groupe_2, False):
                        chest_opened_off_2 = True  # Coffre ouvert
                        key_taken_off_2 = -1
                        vie_boss_off -= 1

                if key_taken_off_3 == 1:
                    if pygame.sprite.spritecollide(self, chest_groupe_3, False):
                        chest_opened_off_3 = True  # Coffre ouvert
                        key_taken_off_3 = -1
                        vie_boss_off -= 1

                # Vérification collision avec le crystal
                if pygame.sprite.spritecollide(self, crystal_groupe, False):
                    crystal_taken_off = 1  # Crystal pris

                # MAJ coordonnées du joueur
                self.rect.x += dx_off  # Déplacement horizontal
                self.rect.y += dy_off  # Déplacement vertical

                # Bordure de map
                if self.rect.x < 0:
                    self.rect.x = 0
                if self.rect.x > screen_width - self.width_off:
                    self.rect.x = screen_width - self.width_off  # Joueur vivant
            # Insertion du joueur
            screen.blit(self.image, self.rect)
            # pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)  # Hit-box du joueur
        if Mort_off == -1:  # Joueur mort
            self.death_animation()

        return Mort_off, key_taken_off, key_taken_off_1, key_taken_off_2, key_taken_off_3, crystal_taken_off, chest_opened_off, chest_opened_off_1, chest_opened_off_2, chest_opened_off_3, condition_next_off, self.rect.x, self.rect.y, self.pause, self.direction, vie_boss_off

    def idle_animation(self, id):  # Animation base (= immobile)
        if self.direction == -1:
            if id == 0:
                side = "gauche"
            else:
                side = "droite_vgo"
        else:
            if id == 0:
                side = "droite"
            else:
                side = "gauche_vgo"
        self.index_2_cpt += 1
        if self.index_2_cpt % 17 == 0:
            self.index_2 += 1
            self.index_2_cpt = 0
        if self.index_2 == 4:
            self.index_2 = 0
        self.image = self.images_base[side][self.index_2]

    def death_animation(self):  # Animation de mort
        if self.direction == -1:
            key = "gauche"
        else:
            key = "droite"
        self.cpt_3 += 1
        if self.cpt_3 >= 30:
            self.index_3 += 1
            self.cpt_3 = 0
        if self.index_3 == 4:
            self.index_3 = 3
        self.image = self.image_mort[key][self.index_3]

        screen.blit(self.image, self.rect)

    def cinematic(self):  # Cinématique avec villageois
        if self.direction == -1:
            self.direction = 1
        self.idle_animation(1)
        self.rect.x = 530
        self.rect.y = 540 - self.image.get_height()
        screen.blit(self.image, self.rect)

    def pause_menu(self, Pygame_off, Niveau_off, Menu_off, joueur_x_off, joueur_y_off, Mort_off):  # Menu pause
        if self.pause:
            screen.blit(background_pause, (0, 0))
            if bouton_reprendre.create(0):
                self.pause = False
            if bouton_menu.create(0):
                save_niveau(profile, Niveau_off)
                Mort_off = 1
                self.pause = False
                Menu_off = True
            if bouton_quitter_2.create(0):
                Pygame_off = False

        return Pygame_off, Menu_off, joueur_x_off, joueur_y_off, Mort_off


class Pluie:
    def __init__(self):
        self.pluie = []
        self.nuage_liste = []
        self.nuage = nuage_img
        self.rect = self.nuage.get_rect()
        self.rect.x = 1080
        self.rect.y = 30
        self.cpt = 0

    def up(self, radius, vx, vy, game_pause_off):
        for goutte in range(6):
            pluie_x = random.randrange(0, 2 * screen_width)
            pluie_y = random.randrange(-500, screen_height - 150)
            if not game_pause_off:
                self.pluie.append([pluie_x, pluie_y])
        if self.cpt == 0:
            self.cpt += 1
        self.event(radius, vx, vy, game_pause_off)

    def event(self, radius, vx, vy, game_pause_off):
        for goutte in self.pluie:
            if not game_pause_off:
                goutte[1] += vx  # Axe Y de la goutte
                goutte[0] -= vy  # Axe X de la goutte
            if goutte[1] > screen_height:
                self.pluie.remove(goutte)
            pygame.draw.circle(screen, (255, 255, 255), goutte, radius)

        # Nuages
        if self.cpt == 1 and radius != 4:
            screen.blit(self.nuage, self.rect)
            if not game_pause_off:
                self.rect.x -= 2
                if self.rect.x < -300:
                    self.rect.x = 1080


class Scorpion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("assets/1-assets_next/scorpion/scorpion_1.png")
        self.image = pygame.transform.scale(self.image, (45, 45))  # Rescale

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_cpt = 0

    def update(self):
        # Direction
        self.rect.x += self.move_direction
        self.move_cpt += 1

        if abs(self.move_cpt) > 30:
            self.move_direction *= -1
            self.move_cpt *= -1


class Slime(pygame.sprite.Sprite):
    k = 0
    L = {-1: [], 1: []}
    key = 0
    side = 1

    for ID in range(1, 5):  # Importation des images
        image = pygame.image.load("assets/1-assets_next/Slime/Walk/Slime_Walk_{}.png".format(ID))
        L[-1].append(image)
        L[1].append(pygame.transform.flip(image, True, False))

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_cpt = 0

    def update(self, game_pause_off):
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)  # Hit-box du Slime
        if not game_pause_off:
            self.rect.x += self.move_direction
            self.move_cpt += 1

            if abs(self.move_cpt) > 50:
                self.move_direction *= -1
                self.move_cpt *= -1
                self.side *= -1

            # Animation marche
            if self.move_cpt % 7 == 0:
                self.image = self.L[self.side][self.k]
                if self.k == 3:
                    self.k = 0
                else:
                    self.k += 1


class Bat(pygame.sprite.Sprite):
    k = 0
    L = {-1: [], 1: []}
    key = 0
    side = 1

    for ID in range(1, 5):  # Importation des images
        image = pygame.image.load("assets/1-assets_next/Bat/Walk/Bat_Walk_{}.png".format(ID))
        L[-1].append(image)
        L[1].append(pygame.transform.flip(image, True, False))

    def __init__(self, x, y, id):
        pygame.sprite.Sprite.__init__(self)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_cpt = 0
        self.id = id
        self.cpt_rand = 0
        self.rand = 0
        self.rand_2 = 0
        self.rand_3 = 0

    def update(self, game_pause_off):
        if not game_pause_off:
            self.rect.x += self.move_direction
            self.move_cpt += 1
            if self.id != "boss":  # S'il n'est pas encore apparu
                if abs(self.move_cpt) > 50:
                    self.move_direction *= -1
                    self.move_cpt *= -1
                    self.side *= -1

            elif self.id == "boss":  # S'il est apparu
                self.cpt_rand += 5
                self.rand_2 = random.randrange(100, 200, 300)
                if self.cpt_rand % self.rand_2 == 0:
                    self.rand = random.randrange(-6, 6)
                    self.rand_3 = random.randrange(-6, 6)
                if self.rand < 0:
                    self.side = -1
                elif self.rand > 0:
                    self.side = 1
                self.rect.y -= self.rand_3  # Valeurs aléatoires ajoutées en x et y
                self.rect.x += self.rand
                if self.rect.x < 0 or self.rect.x > 1080 or self.rect.y < 0 or self.rect.y > 720:
                    self.kill()

            # Animation marche
            if self.move_cpt % 7 == 0:
                self.image = self.L[self.side][self.k]
                if self.k == 3:
                    self.k = 0
                else:
                    self.k += 1


class Wagon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        L = [pygame.image.load("assets/1-assets_next/wagon_2/1.png"),
             pygame.image.load("assets/1-assets_next/wagon_2/2.png")]
        rand = random.randint(0, 1)  # Choix aléatoire de l'image
        self.image = L[rand]
        self.image = pygame.transform.scale(self.image, (45, 45))  # Rescale

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 2
        self.move_cpt = 0
        self.move_cpt_2 = 0

    def update(self, game_pause_off):
        if not game_pause_off:
            # Direction
            self.rect.x += self.move_direction
            self.move_cpt += 1

            if abs(self.move_cpt) > 50:
                self.move_direction *= -1
                self.move_cpt *= -1


class Boss(pygame.sprite.Sprite):
    k = 0
    k_2 = 0
    k_3 = 0
    L = {-3: [], -2: [], -1: []}
    side = -1

    for i in range(1, 3):
        for ID in range(1, 3):  # Importation des images
            image = pygame.image.load("assets/1-assets_next/Centipede/Hurt/Centipede_Hurt_{}.png".format(ID))
            image = pygame.transform.scale(image, (144, 120))  # Rescale
            L[-2].append(image)

    for ID in range(1, 10):  # Importation des images
        image = pygame.image.load("assets/1-assets_next/Centipede/Death/Centipede_Death_{}.png".format(ID))
        image = pygame.transform.scale(image, (144, 120))  # Rescale
        L[-3].append(image)

    for ID in range(1, 7):  # Importation des images
        image = pygame.image.load("assets/1-assets_next/Centipede/Sneer/Centipede_Sneer_{}.png".format(ID))
        image = pygame.transform.scale(image, (144, 120))  # Rescale
        L[-1].append(image)

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_cpt = 0
        self.move_cpt_2 = 0
        self.move_cpt_3 = 0
        self.min = 3
        self.cpt_image = 0
        self.end = False
        self.spawn_cpt = 0

    def update(self, game_pause_off, vie_boss_off):
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)  # Hit-box du Boss
        if not game_pause_off:
            if self.side == -1:
                # ---------- Animation Basique ---------- #
                self.move_cpt += 1
                if self.move_cpt % 7 == 0:
                    self.image = self.L[self.side][self.k]
                if self.k == 5:
                    self.k = 0
                else:
                    self.k += 1
                # --------------------------------------- #

            if vie_boss_off < self.min and vie_boss_off != 0:
                if self.hit():
                    self.min = vie_boss_off
                    self.side = -1

            if vie_boss_off == 0 and not self.end:
                if self.death():
                    self.end = True

            if not self.end:
                # Spawn de chauve-souris
                random_time = random.randint(0, 1000)
                if random_time % 100 == 0:
                    self.spawn()

            elif self.end:
                boss_groupe.empty()
                ennemi_groupe.empty()  # Suppression des entités
                pygame.mixer.Channel(2).fadeout(1000)  # Arrêt de la musique *épique*

        BarreDeVie = pygame.image.load("BarreDeVie{}.png".format(vie_boss_off))
        screen.blit(BarreDeVie, (screen_width / 2 - BarreDeVie1.get_width() / 2, 15))

    def hit(self):
        self.side = -2
        if self.k_2 != len(self.L[-2]):
            # ------------ Animation Hurt ------------ #
            self.move_cpt_2 += 1
            if self.move_cpt_2 % 7 == 0:
                self.image = self.L[-2][self.k_2]
                self.k_2 += 1
            # ---------------------------------------- #
        else:
            self.k_2 = 0
            return 1

    def death(self):
        self.side = -3
        if self.k_3 != len(self.L[self.side]):
            # ------------ Animation Death ------------ #
            self.move_cpt_3 += 1
            if self.move_cpt_3 % 7 == 0:
                self.image = self.L[self.side][self.k_3]
                self.k_3 += 1
            # ---------------------------------------- #
        else:
            self.k_3 = 0
            return 1

    def spawn(self):
        # Spawn de chauve-souris
        if len(ennemi_groupe) < 10:
            bat = Bat(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2, "boss")
            ennemi_groupe.add(bat)
        self.spawn_cpt += 1


class TheKey(pygame.sprite.Sprite):
    k = 0
    L = []
    for ID in range(1, 5):  # Importation des images
        image = pygame.image.load("assets/1-assets_next/Key/Key_{}.png".format(ID))
        L.append(image)

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_cpt = 0
        self.var_x = 30

    def update(self, game_pause_off, key_taken_off, condition_next_off, joueur_x_off, joueur_y_off, direction_off):
        if not game_pause_off:
            # Animation
            self.move_cpt += 1
            if self.move_cpt % 15 == 0:
                self.image = self.L[self.k]
                if self.k == 2:
                    self.k = 0
                else:
                    self.k += 1

            # Suit le joueur
            if key_taken_off == 1:
                if direction_off == 1:
                    self.var_x = -30
                elif direction_off == -1:
                    self.var_x = 30
                self.rect.x = joueur_x_off + self.var_x
                self.rect.y = joueur_y_off + 20
            elif key_taken_off == -1:
                self.rect.x = -3000
                self.rect.y = -3000


class Crystal(pygame.sprite.Sprite):
    k = 0
    L = []
    for ID in range(1, 5):  # Importation des images
        image = pygame.image.load("assets/1-assets_next/Crystal/Crystal_{}.png".format(ID))
        image = pygame.transform.scale(image, (30, 30))
        L.append(image)

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_cpt = 0
        self.var_x = 30

    def update(self, game_pause_off, crystal_taken_off, joueur_x_off, joueur_y_off, direction_off):
        if not game_pause_off:
            # Animation
            self.move_cpt += 1
            if self.move_cpt % 15 == 0:
                self.image = self.L[self.k]
                if self.k == 2:
                    self.k = 0
                else:
                    self.k += 1

            # Suit le joueur
            if crystal_taken_off == 1:
                screen.blit(game_over, (0, 0))
                if direction_off == 1:
                    self.var_x = -30
                elif direction_off == -1:
                    self.var_x = 30
                self.rect.x = joueur_x_off + self.var_x
                self.rect.y = joueur_y_off + 20
            elif crystal_taken_off == -1:
                self.rect.x = -3000
                self.rect.y = -3000


class Coffre(pygame.sprite.Sprite):
    k = 0
    L = []
    for ID in range(5, 18):  # Importation des images
        image = pygame.image.load("assets/1-assets_next/coffre_2/Chest_{}.png".format(ID))
        image = pygame.transform.scale(image, (45, 45))
        L.append(image)

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_cpt = 0
        self.var_x = 30

    def update(self, game_pause_off, key_taken_off, chest_opened_off):
        if not game_pause_off:
            if chest_opened_off:
                # Animation d'ouverture
                self.move_cpt += 1
                if self.move_cpt % 10 == 0:
                    self.image = self.L[self.k]
                    if self.k == 12:
                        self.image = self.L[12]
                    else:
                        self.k += 1
            else:
                self.image = self.L[0]


class Vide(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(image, (taille_tuile, taille_tuile // 2))  # Rescale
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Cristaux(pygame.sprite.Sprite):
    def __init__(self, x, y, image, id):
        pygame.sprite.Sprite.__init__(self)

        if id == "c2":
            image = pygame.transform.rotate(image, 90)
        self.image = pygame.transform.scale(image, (taille_tuile, taille_tuile))  # Rescale
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class RandomBloc(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (taille_tuile, taille_tuile))  # Rescale
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Villageois(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.flip(pygame.image.load("assets/Villageois/Idle_1.png"), True, False)
        self.image = pygame.transform.scale(self.image, (25, 45))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class VillageoisCinematic(pygame.sprite.Sprite):
    k = 0
    L = []
    for ID in range(4, 7):  # Importation des images
        image = pygame.transform.flip(pygame.image.load("assets/Villageois/Idle_{}.png".format(ID)), True, False)
        L.append(image)

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_cpt = 0

    def update(self):

        # Animation
        self.move_cpt += 1
        if self.move_cpt % 30 == 0:
            self.image = self.L[self.k]
            if self.k == 2:
                self.k = 0
            else:
                self.k += 1

    def cinematic(self):  # Cinématique avec villageois
        self.rect.x = 670
        self.rect.y = 540 - self.image.get_height()
        self.update()
        screen.blit(self.image, self.rect)


class HA:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/Texts/ha.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def event(self, go_off, go_2_off, go_3_off, dx_off, dy_off, dx_2_off, dy_2_off, dx_3_off, dy_3_off):
        if go_off:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("HA.mp3"),
                                         2)  # Son du HA sur un 2e canal pour laisser la musique de fond à côté

            go_off = False
        elif not go_off:
            vx = random.randint(-7, -1)
            vy = random.randint(-7, -1)
            co_1 = [dx_off, dy_off]
            co_1[0] += vx
            co_1[1] += vy
            dx_off = co_1[0]
            dy_off = co_1[1]
            if dx_off < 570:
                go_2_off = True
            screen.blit(self.image, tuple(co_1))

        if go_2_off:
            vx = random.randint(-7, -1)
            vy = random.randint(-7, -1)
            co_2 = [dx_2_off, dy_2_off]
            co_2[0] += vx
            co_2[1] += vy
            dx_2_off = co_2[0]
            dy_2_off = co_2[1]
            if dx_2_off < 570:
                go_3_off = True
            screen.blit(self.image, tuple(co_2))

        if go_3_off:
            vx = random.randint(-7, -1)
            vy = random.randint(-7, -1)
            co_3 = [dx_3_off, dy_3_off]
            co_3[0] += vx
            co_3[1] += vy
            dx_3_off = co_3[0]
            dy_3_off = co_3[1]
            screen.blit(self.image, tuple(co_3))

        return go_off, go_2_off, go_3_off, dx_off, dy_off, dx_2_off, dy_2_off, dx_3_off, dy_3_off


# Joueur
Joueur = Joueur(-500, -500)
VillageoisCinematic = VillageoisCinematic(0, 0)

# Caillou + Pluie + texte
GrosCaillouEvent = EventCaillou()
GrosCaillou = Caillou(caillou_img)
Pluie = Pluie()
HA = HA(0, 0)

# Groupes
ennemi_groupe, boss_groupe, vide_groupe, pnj_groupe, caillou_groupe, sortie_groupe, sortie_2_groupe, vgo_groupe, key_groupe, crystal_groupe, chest_groupe_1, chest_groupe_2, chest_groupe_3, key_groupe_1, key_groupe_2, key_groupe_3 \
    = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()

# Créations des boutons
bouton_rejouer = Bouton(screen_width // 2 - 125, screen_height // 2 - 100, bouton_rejouer_img)
bouton_jouer = Bouton(screen_width // 2 - 125, screen_height // 2 + 75, bouton_jouer_img)
bouton_quitter_1 = Bouton(screen_width // 2 - 125, screen_height // 2 + 200, bouton_quitter_img)

bouton_reprendre = Bouton(screen_width // 2 - 150, screen_height // 2 - 135, bouton_reprendre_img)
bouton_menu = Bouton(screen_width // 2 - 100, screen_height // 2, bouton_menu_img)
bouton_quitter_2 = Bouton(screen_width // 2 - 125, screen_height // 2 + 135, bouton_quitter_img)

bouton_new_game_1 = Bouton(390, 265, bouton_new_game_img_1)
bouton_load_game_1 = Bouton(375, 345, bouton_load_game_img_1)
bouton_scoreboard_1 = Bouton(363, 425, bouton_scoreboard_img_1)

bouton_profile_1_1 = Bouton(80, 280, bouton_profile_1_img_1)
bouton_profile_2_1 = Bouton(400, 280, bouton_profile_2_img_1)
bouton_profile_3_1 = Bouton(720, 280, bouton_profile_3_img_1)

# Déclaration de variables importantes pour le jeu
Pygame, intro, Menu, game_pause, can_pause, Menu_2, Menu_3, Menu_4, ok, key_taken, go, go_2, go_3, end_vgo_cine, condition_next, chest_opened, key_taken_1, key_taken_2, key_taken_3, chest_opened_1, chest_opened_2, chest_opened_3, cine_fin, crystal_taken = True, True, True, True, True, False, False, False, False, 0, True, False, False, False, False, False, False, False, False, False, False, False, False, False
cpt, cpt_2, cpt_3, cpt_4, cpt_fin, id_1, id_2, id_3, id_4, id_5, id_6 = (0,) * 11
rx, ry = -8, 8
vie_boss = 3
Mort = 1
profile, Niveau = (None,) * 2
dx, dx_2, dx_3 = (640,) * 3
dy, dy_2, dy_3 = (420,) * 3

# Boucle infinie permettant l'ouverture permanente de la fenêtre Pygame
while Pygame:  # Exécution en boucle
    FPS = clock.tick(50)  # Gestion des FPS

    if Menu:  # Menu principal
        screen.blit(background_night_flou, (0, 0))  # Insertion de l'arrière-plan
        screen.blit(logo, (0, 0))  # Insertion du logo du jeu
        if bouton_jouer.create(0):
            Menu, Menu_2 = False, True
        if bouton_quitter_1.create(0):
            Pygame = False

    elif not Menu and Menu_2:  # Menu secondaire
        screen.blit(background_night_flou, (0, 0))  # Insertion de l'arrière-plan
        screen.blit(Titre_bloc, (0, 0))  # Insertion du titre du jeu

        if bouton_new_game_1.create_and_on(bouton_new_game_img_1, bouton_new_game_img_2,
                                           id_1):  # Insertion du bouton de nouvelle partie
            id_1 = 1
            screen.blit(fleche_img, (bouton_new_game_1.rect.x - fleche_img.get_width() - 10,
                                     bouton_new_game_1.rect.y + bouton_new_game_1.rect.height // 2 - fleche_img.get_height() // 2))
            if bouton_new_game_1.on_click() == 1:
                time.sleep(0.2)
                Menu_2, Menu_3 = False, True

        if bouton_load_game_1.create_and_on(bouton_load_game_img_1, bouton_load_game_img_2,
                                            id_2):  # Insertion du bouton de chargement de partie
            id_2 = 1
            screen.blit(fleche_img, (bouton_load_game_1.rect.x - fleche_img.get_width() - 10,
                                     bouton_load_game_1.rect.y + bouton_load_game_1.rect.height // 2 - fleche_img.get_height() // 2))
            if bouton_load_game_1.on_click() == 1:
                time.sleep(0.2)
                Menu_2, Menu_4 = False, True

        if bouton_scoreboard_1.create_and_on(bouton_scoreboard_img_1, bouton_scoreboard_img_2,
                                             id_3):  # Insertion du bouton de tableau de scores
            id_3 = 1
            screen.blit(fleche_img, (bouton_scoreboard_1.rect.x - fleche_img.get_width() - 10,
                                     bouton_scoreboard_1.rect.y + bouton_scoreboard_1.rect.height // 2 - fleche_img.get_height() // 2))
        if not bouton_new_game_1.create_and_on(bouton_new_game_img_1, bouton_new_game_img_2, id_1) \
                and not bouton_load_game_1.create_and_on(bouton_load_game_img_1, bouton_load_game_img_2, id_2) \
                and not bouton_scoreboard_1.create_and_on(bouton_scoreboard_img_1, bouton_scoreboard_img_2, id_3):
            id_1, id_2, id_3 = (0,) * 3

    elif not Menu and not Menu_2 and Menu_3 or Menu_4:  # Menu de nouvelle partie
        screen.blit(background_night_flou, (0, 0))  # Insertion de l'arrière-plan
        with open("save.txt", "r") as sr:  # Ouverture du fichier de sauvegarde
            save = sr.readlines()
        if bouton_profile_1_1.create_and_on(bouton_profile_1_img_1, bouton_profile_1_img_2,
                                            id_4):  # Insertion du bouton de profil 1
            id_4 = 1
            if bouton_profile_1_1.on_click() == 1:
                profile = 1
                if Menu_3:  # Si on est dans le menu de nouvelle partie
                    save_niveau(profile, "-1")
                    Niveau = int(get_niveau(profile))
                    Menu_3 = False
                elif Menu_4:  # Si on est dans le menu de chargement de partie
                    Niveau = int(get_niveau(profile))
                    if Niveau != -1:
                        Niveau -= 1
                    Menu_4 = False
        if bouton_profile_2_1.create_and_on(bouton_profile_2_img_1, bouton_profile_2_img_2,
                                            id_5):  # Insertion du bouton de profil 2
            id_5 = 1
            if bouton_profile_2_1.on_click() == 1:
                profile = 2
                if Menu_3:
                    save_niveau(profile, "-1")
                    Niveau = int(get_niveau(profile))
                    Menu_3 = False
                elif Menu_4:
                    Niveau = int(get_niveau(profile))
                    if Niveau != -1:
                        Niveau -= 1
                    Menu_4 = False
        if bouton_profile_3_1.create_and_on(bouton_profile_3_img_1, bouton_profile_3_img_2,
                                            id_6):  # Insertion du bouton de profil 3
            id_6 = 1
            if bouton_profile_3_1.on_click() == 1:
                profile = 3
                if Menu_3:
                    save_niveau(profile, "-1")
                    Niveau = int(get_niveau(profile))
                    Menu_3 = False
                elif Menu_4:
                    Niveau = int(get_niveau(profile))
                    if Niveau != -1:
                        Niveau -= 1
                    Menu_4 = False
        if not bouton_profile_1_1.create_and_on(bouton_profile_1_img_1, bouton_profile_1_img_2, id_4) \
                and not bouton_profile_2_1.create_and_on(bouton_profile_2_img_1, bouton_profile_2_img_2, id_5) \
                and not bouton_profile_3_1.create_and_on(bouton_profile_3_img_1, bouton_profile_3_img_2, id_6):
            id_4, id_5, id_6 = (0,) * 3

    else:
        screen.blit(background_off, (0, 0))  # Insertion de l'arrière-plan
        if Mort == 0:  # Joueur vivant

            # Spécificités par niveau
            # Niveaux 0 introduction
            if 0 <= Niveau <= 3:
                Pluie.up(1, 10, 15, game_pause)
                if dialogue:
                    dialogue, cpt, cpt_2 = dialogue_1(dialogue, Niveau, cpt, cpt_2, game_pause)

            # Niveau 1
            if Niveau == 4:
                for objet in caillou_groupe:
                    objet.update()
                    caillou_groupe.draw(screen)
                GrosCaillouEvent.event()

            # Création des calques
            world.create()
            world_2.create()
            Mort, key_taken, key_taken_1, key_taken_2, key_taken_3, crystal_taken, chest_opened, chest_opened_1, chest_opened_2, chest_opened_3, condition_next, joueur_x_2, joueur_y_2, game_pause, direction, vie_boss \
                = Joueur.update(Mort, key_taken, key_taken_1, key_taken_2, key_taken_3, crystal_taken, chest_opened,
                                chest_opened_1, chest_opened_2, chest_opened_3, condition_next, False, can_pause,
                                cine_fin, vie_boss)
            world_3.create()
            ennemi_groupe.update(game_pause)
            boss_groupe.update(game_pause, vie_boss)
            key_groupe.update(game_pause, key_taken, condition_next, joueur_x_2, joueur_y_2, direction)
            crystal_groupe.update(game_pause, crystal_taken, joueur_x_2, joueur_y_2, direction)
            key_groupe_1.update(game_pause, key_taken_1, condition_next, joueur_x_2, joueur_y_2, direction)
            key_groupe_2.update(game_pause, key_taken_2, condition_next, joueur_x_2, joueur_y_2, direction)
            key_groupe_3.update(game_pause, key_taken_3, condition_next, joueur_x_2, joueur_y_2, direction)
            chest_groupe_1.update(game_pause, key_taken, chest_opened_1)
            chest_groupe_2.update(game_pause, key_taken, chest_opened_2)
            chest_groupe_3.update(game_pause, key_taken, chest_opened_3)
            ennemi_groupe.draw(screen)
            pnj_groupe.draw(screen)
            vide_groupe.draw(screen)
            sortie_groupe.draw(screen)
            sortie_2_groupe.draw(screen)
            crystal_groupe.draw(screen)
            key_groupe.draw(screen)
            key_groupe_1.draw(screen)
            key_groupe_2.draw(screen)
            key_groupe_3.draw(screen)
            chest_groupe_1.draw(screen)
            chest_groupe_2.draw(screen)
            chest_groupe_3.draw(screen)
            boss_groupe.draw(screen)

        # Suite spécificités par niveau
        if Niveau == 5 or Niveau == 6:
            if key_taken == 1:
                if dialogue:
                    dialogue, cpt, cpt_2 = dialogue_1(dialogue, Niveau, cpt, cpt_2, game_pause)
        if key_taken == 1 and Niveau == 5 and joueur_x_2 == 975 and joueur_y_2 == 42:
            Mort = 1

        if Niveau == 10:
            cine_fin = True
            pygame.mixer.Channel(0).fadeout(1000)

            if dialogue:
                dialogue, cpt, cpt_2 = dialogue_1(dialogue, Niveau, cpt, cpt_2, game_pause)
            cpt_fin += 1
            if cpt_fin == 30:
                pygame.mixer.Channel(2).play(pygame.mixer.Sound("musique_boss.mp3"), -1)
            elif 70 < cpt_fin < 110:
                rx, ry, cpt_4 = screen_shaking(game_pause, rx, ry, cpt_4)
            elif 150 < cpt_fin < 190:
                rx, ry, cpt_4 = screen_shaking(game_pause, rx, ry, cpt_4)
            elif 230 < cpt_fin < 400:
                rx, ry, cpt_4 = screen_shaking(game_pause, rx, ry, cpt_4)
            elif cpt_fin > 400:
                cine_fin = False
            r = random.randint(0, 10000)
            if r % 300 == 0:
                pass  # Animation random
            # !!!

        Mort = Joueur.update(Mort, key_taken, key_taken_1, key_taken_2, key_taken_3, crystal_taken, chest_opened,
                             chest_opened_1,
                             chest_opened_2, chest_opened_3, condition_next, True, can_pause, cine_fin, vie_boss)[0]

        if Mort == -1:  # Joueur mort
            Joueur.death_animation()
            world.create()  # Conservation des calques
            world_2.create()
            world_3.create()
            world_3.create()
            ennemi_groupe.draw(screen)
            boss_groupe.draw(screen)
            pnj_groupe.draw(screen)
            Joueur.death_animation()

            if joueur_y_2 < 700:
                screen.blit(black_circle.convert_alpha(), (joueur_x_2 - 1010, joueur_y_2 - 1000))
            else:
                screen.blit(black_circle.convert_alpha(), (joueur_x_2 - 1010, joueur_y_2 - 1050))
            Joueur.death_animation()  # Animation de mort

            # Bouton rejouer
            if bouton_rejouer.create(1):
                Joueur.__init__(joueur_x, joueur_y)
                Mort = 0  # Joueur vivant

                # Suppression des entités existantes
                caillou_groupe.empty()

        if Mort == 1:  # Niveau suivant
            can_pause = True
            Niveau += 1

            # Sauvegarde
            save_niveau(profile, Niveau)

            if Niveau < 3 or Niveau == 5 or Niveau == 10:
                dialogue = True
            if Niveau <= 11:
                world, world_2, world_3, background_off, joueur_x, joueur_y = reset_niveau(Niveau)
                Joueur.__init__(joueur_x, joueur_y)
                Mort = 0  # Joueur vivant
            else:
                # Restart game
                pass

        if Mort == 2:  # Cinématique avec villageois
            if fade_inout(screen_width, screen_height, 50, "in"):
                Mort = 3
        if Mort == 3:
            can_pause = False
            screen.blit(background_night_cine_1, (0, 0))
            Pluie.up(4, 20, 25, game_pause)
            screen.blit(background_night_cine_2, (0, 0))
            Joueur.cinematic()
            VillageoisCinematic.cinematic()
            dialogue, cpt, cpt_2, go, go_2, go_3, dx, dy, dx_2, dy_2, dx_3, dy_3, end_vgo_cine = dialogue_2(dialogue, cpt, cpt_2, Mort, go, go_2, go_3, dx, dy, dx_2, dy_2, dx_3, dy_3, end_vgo_cine)
            if pygame.key.get_pressed()[pygame.K_a] and end_vgo_cine:
                vgo_groupe.empty()
                dialogue = False
                Mort = 1

    Pygame, Menu, joueur_x, joueur_y, Mort = Joueur.pause_menu(Pygame, Niveau, Menu, joueur_x, joueur_y, Mort)  # Menu Pause
    # grille()  # Affichage de la grille
    # Affichage plein écran
    # screen.blit(pygame.surface.Surface((400, 720)), (1080, 0))
    # Quitter le jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Pygame = False
    pygame.mouse.get_pos()
    pygame.display.update()  # Mise à jour en permanence de la fenêtre de Pygame
