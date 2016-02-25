# -*- coding: utf-8 -*-
# vim: nu
# vim: expandtab shiftwidth=2 softtabstop=2 autoindent

#!/usr/bin/python

import sys
import pygame
import sprites

pygame.init()
WIDTH = 700										# arbitrary values for now
HEIGHT = 700
size = WIDTH, HEIGHT
WHITE      = (255, 255, 255)			      					#a few predefined constant colors
BLACK      = (  0,   0,   0)
BLUE       = (  0,   0, 255)
GREEN      = (  0, 255,   0)
RED        = (255,   0,   0)
ORANGE     = (255, 165,   0)
NEAR_BLACK = ( 25,  16,  16)                                                            #appears to be used rather than black
    

icon = pygame.Surface((24,24))
icon.fill(BLUE)
my_icon = sprites.Pokeball (0, 0, 0, 0, 1, NEAR_BLACK, WHITE, (255,123,123), icon)
my_icon.draw()
pygame.display.set_icon(icon)
pygame.display.set_caption("Gotta Catch 'Em All")
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

#pokemon  = sprites.Pokeball   (  0, 0, 0, 0, 1, NEAR_BLACK, WHITE,         (255,123,123),        screen)
#pokemon  = sprites.Bulbasaur  (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90),   (165,214,132), WHITE, screen)
#pokemon  = sprites.Ivysaur    (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90),   (165,214,132), WHITE, screen)
#pokemon  = sprites.Venasaur   (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90),   (165,214,132), WHITE, screen)
#pokemon  = sprites.Charmander (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,162,82),  WHITE, screen)
#pokemon  = sprites.Charmeleon (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,162,82),  WHITE, screen)
#pokemon  = sprites.Charizard  (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,162,82),  WHITE, screen)
#pokemon  = sprites.Squirtle   (  0, 0, 0, 0, 1, NEAR_BLACK, (115,156,206), (173,206,239), WHITE, screen)
#pokemon  = sprites.Wartortle  (  0, 0, 0, 0, 1, NEAR_BLACK, (115,156,206), (173,206,239), WHITE, screen)
#pokemon  = sprites.Blastoise  (  0, 0, 0, 0, 1, NEAR_BLACK, (115,156,206), (173,206,239), WHITE, screen)
#pokemon  = sprites.Caterpie   (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90),   (165,214,132), WHITE, screen)
#pokemon  = sprites.Metapod    (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90),   (165,214,132), WHITE, screen)
#pokemon  = sprites.Butterfree (  0, 0, 0, 0, 1, NEAR_BLACK, (115,156,206), (173,206,239), WHITE, screen)
#pokemon  = sprites.Weedle     (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#pokemon  = sprites.Kakuna     (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#pokemon  = sprites.Beedrill   (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#pokemon  = sprites.Pidgey     (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#pokemon  = sprites.Pidgeotto  (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#pokemon  = sprites.Pidgeot    (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#pokemon  = sprites.Rattata    (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#pokemon  = sprites.Raticate   (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#pokemon  = sprites.Spearow    (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#pokemon  = sprites.Fearow     (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#pokemon  = sprites.Ekans      (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#pokemon  = sprites.Arbok      (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#pokemon  = sprites.Pikachu    (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#pokemon  = sprites.Raichu     (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
#pokemon  = sprites.Sandshrew  (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#pokemon  = sprites.Sandslash  (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),  (230,165,123), WHITE, screen)
#pokemon  = sprites.NidoranF   (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189),  (148,165,222), WHITE, screen)
#pokemon  = sprites.Nidorina   (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189),  (148,165,222), WHITE, screen)
#pokemon  = sprites.Nidoqueen  (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189),  (148,165,222), WHITE, screen)
#pokemon  = sprites.NidoranM   (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#pokemon  = sprites.Nidorino   (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#pokemon  = sprites.Nidoking   (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#pokemon  = sprites.Clefairy   (  0, 0, 0, 0, 1, NEAR_BLACK, (230,123,173), (247,181,197), WHITE, screen)
#pokemon  = sprites.Clefable   (  0, 0, 0, 0, 1, NEAR_BLACK, (230,123,173), (247,181,197), WHITE, screen)
#pokemon  = sprites.Vulpix     (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,162,82),  WHITE, screen)
#pokemon  = sprites.Ninetails  (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0),   (255,230,115), WHITE, screen)
# TODO  39 - Jigglypuff
# TODO  40 - Wigglytuff
# TODO  41 - Zubat
# TODO  42 - Golbat
#pokemon  = sprites.Oddish     (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90),   (165,214,132), WHITE, screen)
#pokemon  = sprites.Gloom      (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,165,82),  WHITE, screen)
#pokemon  = sprites.Vileplume  (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,165,82),  WHITE, screen)
# TODO  46 - Paras
# TODO  47 - Parasect
#pokemon  = sprites.Venonat    (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#pokemon  = sprites.Venomoth   (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
# TODO  50 - Diglet
# TODO  51 - Dugtrio
# TODO  52 - Meowth
# TODO  53 - Persian
# TODO  54 - Psyduck
# TODO  55 - Golduck
# TODO  56 - Mankey
# TODO  57 - Primeape
#pokemon  = sprites.Growlithe  (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),   (230,165,123), WHITE, screen)
#pokemon  = sprites.Arcanine   (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74),   (255,165,82),  WHITE, screen)
#pokemon  = sprites.Poliwag    (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189),   (148,165,222), WHITE, screen)
pokemon  = sprites.Poliwhirl  (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189),   (148,165,222), WHITE, screen)
# TODO  61 - Poliwhirl
# TODO  62 - Poliwrath
#pokemon  = sprites.Abra     (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0), (255,230,115), WHITE, screen)
#pokemon  = sprites.Kadabra  (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0), (255,230,115), WHITE, screen)
#pokemon  = sprites.Alakazam (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0), (255,230,115), WHITE, screen)
# TODO  66 - Machop
# TODO  67 - Machoke
# TODO  68 - Machamp
#pokemon  = sprites.Bellsprout  (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90), (165,214,132), WHITE, screen)
#pokemon  = sprites.Weepinbell  (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90), (165,214,132), WHITE, screen)
#pokemon  = sprites.Victreebel  (  0, 0, 0, 0, 1, NEAR_BLACK, (74,165,90), (165,214,132), WHITE, screen)
# TODO  72 - Tentacool
# TODO  73 - Tentacruel
#pokemon  = sprites.Geodude   (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#pokemon  = sprites.Graveler  (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#pokemon  = sprites.Golem     (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#pokemon  = sprites.Ponyta    (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,162,82),  WHITE, screen)
#pokemon  = sprites.Rapidash  (  0, 0, 0, 0, 1, NEAR_BLACK, (214,82,49),   (255,162,82),  WHITE, screen)
# TODO  79 - Slowpoke
# TODO  80 - Slowbro
# TODO  81 - Magnemite
# TODO  82 - Magneton
# TODO  83 - Farfetch'd
#pokemon  = sprites.Doduo     (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74), (230,165,123), WHITE, screen)
#pokemon  = sprites.Dodrio    (  0, 0, 0, 0, 1, NEAR_BLACK, (173,115,74), (230,165,123), WHITE, screen)
# TODO  86 - Seel
# TODO  87 - Dewgong
# TODO  88 - Grimer
# TODO  89 - Muk
# TODO  90 - Shellder
# TODO  91 - Cloyster
#pokemon  = sprites.Gastly     (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#pokemon  = sprites.Haunter    (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#pokemon  = sprites.Gengar     (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#pokemon  = sprites.Onix       (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
# TODO  96 - Drowzee
# TODO  97 - Hypno
# TODO  98 - Krabby
# TODO  99 - Kingler
#pokemon  = sprites.Voltorb    (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0), (255,230,115), WHITE, screen)
#pokemon  = sprites.Electrode  (  0, 0, 0, 0, 1, NEAR_BLACK, (214,165,0), (255,230,115), WHITE, screen)
# TODO 102 - Exeggcute
# TODO 103 - Exeggutor
#pokemon  = sprites.Cubone     (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#pokemon  = sprites.Marowak    (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
# TODO 106 - Hitmonlee
# TODO 107 - Hitmonchan
# TODO 108 - Lickitung
#pokemon  = sprites.Koffing    (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
#pokemon  = sprites.Weezing    (  0, 0, 0, 0, 1, NEAR_BLACK, (173,123,189), (222,181,197), WHITE, screen)
# TODO 111 - Rhyhorn
# TODO 112 - Rhydon
# TODO 113 - Chansey
#pokemon  = sprites.Tangela    (  0, 0, 0, 0, 1, NEAR_BLACK, (90,123,189), (148,165,222), WHITE, screen)
# TODO 115 - Kangaskhan
# TODO 116 - Horsea
# TODO 117 - Seadra
# TODO 118 - Goldeen
# TODO 119 - Seaking
#pokemon  = sprites.Staryu    (  0, 0, 0, 0, 1, NEAR_BLACK, (255,165,82), (214,82,49), WHITE, screen)
#pokemon  = sprites.Starmie   (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
#pokemon  = sprites.Mr_Mime   (  0, 0, 0, 0, 1, NEAR_BLACK, (247,181,197), (230,123,173), WHITE, screen)
# TODO 123 - Scyther
# TODO 124 - Jynx
# TODO 125 - Electabuzz
# TODO 126 - Magmar
# TODO 127 - Pinsir
#pokemon  = sprites.Tauros    (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
# TODO 129 - Magikarp
# TODO 130 - Gyrados
# TODO 131 - Lapras
#pokemon  = sprites.Ditto     (  0, 0, 0, 0, 1, NEAR_BLACK, (123,123,148), (214,173,181), WHITE, screen)
# TODO 133 - Evee
# TODO 134 - Vaporeon
# TODO 135 - Jolteon
# TODO 136 - Flareon
# TODO 137 - Porygon
# TODO 138 - Omanyte
# TODO 139 - Omastar
# TODO 140 - Kabuto
# TODO 141 - Kabutops
# TODO 142 - Aerodactyl
# TODO 143 - Snorlax
# TODO 144 - Articuno
# TODO 145 - Zapdos
# TODO 146 - Moltres
# TODO 147 - Dratini
# TODO 148 - Dragonair
# TODO 149 - Dragonite
#pokemon  = sprites.Mewtwo     (  0, 0, 0, 0, 1, NEAR_BLACK, (132,115,156), (247,181,140), WHITE, screen)
#pokemon  = sprites.Mew        (  0, 0, 0, 0, 1, NEAR_BLACK, (132,115,156), (247,181,140), WHITE, screen)
#pokemon  = sprites.Missingno  (  0, 0, 0, 0, 1, NEAR_BLACK, WHITE, screen)
											#set sprite at location x,y, with velocity x,y,
											#with size multiplier 1,  with the following four colors
											#on the main screen
print pokemon.get_Name()
print str(pokemon.get_Number()).zfill(3)
print pokemon.get_Pokedex_Message()
while not done:

  #limit the clock to ten loops per second
  clock.tick(3)

  for event in pygame.event.get():							#allows you to exit by clicking x
    if event.type == pygame.QUIT:
      done =True

  screen.fill(RED)									#arbitrary color, good for spotting mistakes in the sprite

  pokemon.draw()

  pygame.display.flip()

pygame.quit()
