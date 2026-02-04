import pygame
import random

pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulateur Self-KYC : État & Téléphone")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
ORANGE = (255, 165, 0)
GREEN = (50, 200, 50)
BLUE = (50, 100, 200)

font = pygame.font.SysFont("Arial", 24)

# Base de données simulée
known_sims = {"SIM123": "0999999999", "SIM456": "0888888888"}
known_imeis = {"IMEI111", "IMEI222"}

# Variables dynamiques
current_sim = None
current_number = None
current_imei = None
status = "Aucun appareil"
color = BLACK

# Fonction centrale (État)
def etat_decision(sim, imei, validated=False):
    if validated:
        return "Services ACTIVÉS par l'État", GREEN
    if sim in known_sims and imei not in known_imeis:
        return "Blocage PARTIEL (SIM connue, IMEI inconnu)", ORANGE
    elif sim not in known_sims and imei not in known_imeis:
        return "Blocage TOTAL (SIM inconnue, IMEI inconnu)", RED
    else:
        return "Services ACTIVÉS (SIM/IMEI reconnus)", GREEN

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Actions clavier
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # insérer une SIM
                current_sim, current_number = random.choice(list(known_sims.items()) + [("SIM999","0777777777")])
            if event.key == pygame.K_t:  # insérer un téléphone
                current_imei = random.choice(list(known_imeis) + ["IMEI999"])
            if event.key == pygame.K_v:  # validation par l'État
                status, color = etat_decision(current_sim, current_imei, validated=True)
                continue

            if current_sim and current_imei:
                status, color = etat_decision(current_sim, current_imei)

    # Affichage
    screen.fill(WHITE)

    # Bloc Téléphone
    pygame.draw.rect(screen, BLUE, (50, 100, 400, 400), 3)
    tel_title = font.render("Téléphone", True, BLUE)
    sim_text = font.render(f"SIM: {current_sim}", True, BLACK)
    num_text = font.render(f"Numéro: {current_number}", True, BLACK)
    imei_text = font.render(f"IMEI: {current_imei}", True, BLACK)

    screen.blit(tel_title, (200, 110))
    screen.blit(sim_text, (70, 180))
    screen.blit(num_text, (70, 220))
    screen.blit(imei_text, (70, 260))

    # Bloc État
    pygame.draw.rect(screen, BLACK, (550, 100, 400, 400), 3)
    etat_title = font.render("Centrale (État)", True, BLACK)
    status_text = font.render(status, True, color)

    screen.blit(etat_title, (700, 110))
    screen.blit(status_text, (570, 200))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
