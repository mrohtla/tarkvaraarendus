import pygame  # Impordib pygame

pygame.init()  # Käivitab pygame mooduli

screen = pygame.display.set_mode([300, 300])  # Teeb 300x300 ekraani

pygame.display.set_caption("Lumemees - Merili Rohtla")  # Nimetab ekraani nimeliseks

screen.fill([102, 255, 255], (0, 0, screen.get_width(), 242))  # Teeb akna taeva osa siniseks
screen.fill([250, 250, 250], (0, 242, screen.get_width(), screen.get_height()))  # Teeb akna maa osa valgeks ehk lumeks
pygame.draw.circle(screen, [255, 255, 0], [0, 0], 50, 0)  # Teeb särava kollase päikese
pygame.draw.line(screen, [255, 255, 0], [11, 58], [14, 75], 3)  # Teeb päikese kiire
pygame.draw.line(screen, [255, 255, 0], [35, 50], [46, 62], 3)  # Teeb päikese kiire
pygame.draw.line(screen, [255, 255, 0], [50, 27], [69, 34], 3)  # Teeb päikese kiire
pygame.draw.line(screen, [255, 255, 0], [58, 10], [79, 13], 3)  # Teeb päikese kiire


pygame.draw.circle(screen, [255,255,255], [250,70], 15, 0) # pilv
pygame.draw.circle(screen, [255,255,255], [230,70], 20, 0) # pilv
pygame.draw.circle(screen, [255,255,255], [210,70], 15, 0) # pilv

pygame.draw.circle(screen, [255,255,255], [100,70], 15, 0) # pilv
pygame.draw.circle(screen, [255,255,255], [80,70], 20, 0) # pilv
pygame.draw.circle(screen, [255,255,255], [60,70], 15, 0) # pilv

pygame.draw.circle(screen, [255,255,255], [230,140], 15, 0) # pilv
pygame.draw.circle(screen, [255,255,255], [210,140], 20, 0) # pilv
pygame.draw.circle(screen, [255,255,255], [190,140], 15, 0) # pilv


pygame.draw.circle(screen, [255, 255, 255], [150, 85], 30, 0)  # Teeb valge lumememme pea
pygame.draw.circle(screen, [0, 0, 0], [138, 82], 5, 0)  # Teeb musta lumememme vasaku silma
pygame.draw.circle(screen, [0, 0, 0], [162, 82], 5, 0)  # Teeb musta lumememme parema silma
pygame.draw.polygon(screen, [255, 0, 0], [[145, 90], [155, 90], [150, 105]], 0)  # Teeb punase lumememme nina
pygame.draw.polygon(screen, [192,192,192], [[118, 60], [180, 60], [167, 30], [131, 30]])  # Teeb lumememmele ämbri/mütsi pähe
pygame.draw.circle(screen, [255, 255, 255], [150,150], 40, 0)  # Teeb valge lumememme keskmise palli
pygame.draw.circle(screen, [255, 255, 255], [150, 235], 50, 0)  # Teeb valge lumememme alumise palli
pygame.draw.line(screen, [165, 42, 42], [120,120], [50,110], 4) # vasak käsi
pygame.draw.line(screen, [165, 42, 42], [180,120], [240,115], 4) # parem käsi
pygame.draw.line(screen, [165, 42, 42], [260,78], [240,117], 4) # parem üleval käe oks
pygame.draw.line(screen, [165, 42, 42], [240,117], [266,150], 4)# parem all käe oks
pygame.draw.line(screen, [165, 42, 42], [51,110], [38,76], 4) # vasak üleval käe oks
pygame.draw.line(screen, [165, 42, 42], [51,110], [36,140], 4) # vasak all käe oks
pygame.draw.circle(screen, [0, 0, 0], [151, 130], 5, 0) # ülemine nööp
pygame.draw.circle(screen, [0, 0, 0], [151, 145], 5, 0) # keskmine nööp
pygame.draw.circle(screen, [0, 0, 0], [151, 160], 5, 0) # alumine nööp
pygame.draw.line(screen, [165, 42, 42], [254,160], [253,57], 4) # hari vars
pygame.draw.polygon(screen, [255, 255, 0], [[254,57],[262,44],[244,44]], 0) # hari kollane osa
pygame.display.flip()  # Värskendab ekraani

# Selle jaoks, et ekraani saaks kinni panna.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if running == False:
            pygame.quit()