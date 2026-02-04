import pygame
import random

pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulateur Self-KYC : Téléphone & État")

# Couleurs
WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 50)
GREEN = (50, 200, 50)
RED = (200, 50, 50)
ORANGE = (255, 165, 0)
BLUE = (50, 100, 200)

font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 32)

# Base de données simulée
known_sims = {"SIM123": "0999999999", "SIM456": "0888888888"}
known_imeis = {"IMEI111", "IMEI222"}

# Variables dynamiques
current_sim = None
current_number = None
current_imei = None
status = "Aucun appareil"
color = BLACK

def etat_decision(sim, imei, validated=False):
    if validated:
        return "✅ Services ACTIVÉS par l'État", GREEN
    if sim in known_sims and imei not in known_imeis:
        return "⚠️ Blocage PARTIEL (SIM connue, IMEI inconnu)", ORANGE
    elif sim not in known_sims and imei not in known_imeis:
        return "⛔ Blocage TOTAL (SIM inconnue, IMEI inconnu)", RED
    else:
        return "✅ Services ACTIVÉS (SIM/IMEI reconnus)", GREEN

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                current_sim, current_number = random.choice(list(known_sims.items()) + [("SIM999","0777777777")])
            if event.key == pygame.K_t:
                current_imei = random.choice(list(known_imeis) + ["IMEI999"])
            if event.key == pygame.K_v:
                status, color = etat_decision(current_sim, current_imei, validated=True)
                continue
            if current_sim and current_imei:
                status, color = etat_decision(current_sim, current_imei)

    screen.fill(WHITE)

    # Téléphone stylisé
    pygame.draw.rect(screen, DARK_GRAY, (80, 80, 300, 500), border_radius=20)
    pygame.draw.rect(screen, (200, 230, 200), (100, 120, 260, 300), border_radius=15)
    pygame.draw.circle(screen, GRAY, (230, 470), 20)

    screen.blit(big_font.render("Téléphone", True, WHITE), (140, 90))
    screen.blit(font.render(f"SIM: {current_sim}", True, BLACK), (110, 140))
    screen.blit(font.render(f"Numéro: {current_number}", True, BLACK), (110, 180))
    screen.blit(font.render(f"IMEI: {current_imei}", True, BLACK), (110, 220))
    pygame.draw.rect(screen, GRAY, (150, 300, 160, 40), border_radius=10)
    screen.blit(font.render("Valider (V)", True, WHITE), (170, 310))

    # État stylisé
    pygame.draw.rect(screen, BLACK, (600, 150, 320, 300), border_radius=15)
    pygame.draw.rect(screen, WHITE, (610, 190, 300, 220), border_radius=10)
    screen.blit(big_font.render("État", True, WHITE), (720, 160))
    screen.blit(font.render(status, True, color), (620, 220))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
