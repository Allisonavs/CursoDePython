import pygame
import sys

pygame.init()

# Definições de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (255, 182, 193)  # Rosa pastel

# Configurações da tela
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Exemplo de Menu")

# Inicialização do mixer para reprodução de música
pygame.mixer.init()
pygame.mixer.music.load('flamingo8bit.mp3')
pygame.mixer.music.play(-1)  # -1 significa tocar indefinidamente
pygame.mixer.music.set_volume(0.5)  # Configura o volume da música (0.0 a 1.0)

# Função para desenhar o texto na tela
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Função para exibir o menu
def show_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(PINK)  # Preenche o fundo com rosa pastel
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Definição das opções do menu
        font = pygame.font.Font(None, 50)
        start_game_text = "Iniciar Jogo"
        options_text = "Opções"
        quit_text = "Sair"

        # Verificação do clique do mouse nas opções do menu
        start_game_button = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 - 50, 200, 30)
        options_button = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 + 20, 200, 30)
        quit_button = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 + 90, 200, 30)

        # Desenho dos botões e verificação do mouse sobre eles
        if start_game_button.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, PINK, start_game_button)
            if pygame.mouse.get_pressed()[0]:
                print("Iniciar Jogo")
        else:
            pygame.draw.rect(screen, RED, start_game_button)

        if options_button.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, PINK, options_button)
            if pygame.mouse.get_pressed()[0]:
                print("Opções")
        else:
            pygame.draw.rect(screen, RED, options_button)

        if quit_button.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(screen, PINK, quit_button)
            if pygame.mouse.get_pressed()[0]:
                print("Sair")
        else:
            pygame.draw.rect(screen, RED, quit_button)

        # Desenho do menu
        draw_text(start_game_text, font, BLACK, WIDTH / 2, HEIGHT / 2 - 35)
        draw_text(options_text, font, BLACK, WIDTH / 2, HEIGHT / 2 + 35)
        draw_text(quit_text, font, BLACK, WIDTH / 2, HEIGHT / 2 + 105)

        pygame.display.flip()

# Execução do menu
show_menu()
