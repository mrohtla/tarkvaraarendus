import pygame # importib mooduli

pygame.init()# käivitab selle mooduli
screen=pygame.display.set_mode([300,300])# teeb 300x300 akna
pygame.display.set_caption("Foor - Merili Rohtla")# paneb akna nimeks "Foor - Merili Rohtla"
pygame.draw.rect(screen, [128, 128, 128], [89, 10, 100, 272], 2)# teeb valge ristküliku x=89, y=15,w=100, h=275, joonepaksus=2
pygame.draw.circle(screen, [255, 0, 0], [139,60], 40, 0) # teeb punase täidetud ringi x = 139, y=65, raaduius=40 joone paksus=0 et täidaks.
pygame.draw.circle(screen, [255, 255, 0], [139,145], 40, 0)# teeb kollase täidetud ringi x = 139, y=150, raaduius=40 joone paksus=0 et täidaks.
pygame.draw.circle(screen, [102, 255, 51], [139,230], 40, 0)# teeb rohelise täidetud ringi x = 139, y=235, raaduius=40 joone paksus=0 et täidaks.


pygame.display.flip()# värskendab ekraani



# selle jaoks et aken ära ei kaoks ja kinni saaks panna, internetist võetud.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()