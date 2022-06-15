import pygame # importib mooduli

pygame.init()# käivitab selle mooduli
screen=pygame.display.set_mode([300,600])# teeb 300x600 akna
pygame.display.set_caption("Foor - Merili Rohtla")# paneb akna nimeks "Foor - Merili Rohtla"
pygame.draw.rect(screen, [128, 128, 128], [100, 10, 100, 272], 2)# teeb valge ristküliku x=100, y=10,w=100, h=272, joonepaksus=2
pygame.draw.circle(screen, [255, 0, 0], [150,60], 40, 0) # teeb punase täidetud ringi x = 150, y=60, raaduius=40 joone paksus=0 et täidaks.
pygame.draw.circle(screen, [255, 255, 0], [150,145], 40, 0)# teeb kollase täidetud ringi x = 150, y=145, raaduius=40 joone paksus=0 et täidaks.
pygame.draw.circle(screen, [102, 255, 51], [150,230], 40, 0)# teeb rohelise täidetud ringi x = 150, y=230, raaduius=40 joone paksus=0 et täidaks.

pygame.draw.rect(screen, [128, 128, 128], [145, 280, 10, 150], 0)#teeb halli ristküliku x=145, y=280, w=10, h=150
pygame.draw.polygon(screen, [0, 0, 255], [[100,430],[200,430],[215,460],[85,460],[100,430]], 0)#teeb sisnise täidetud hulknurga mille tippude koordinaadid (100,430), (200,430), (215,460), (85, 460), (100,430)
pygame.draw.polygon(screen, [255, 255, 255], [[65,495],[235,495],[255,530],[50,530],[65,495]], 0)#teeb valge täidetud hulknurga tipu koordinaatidega (65,495),(235,495),(255,530),(50,530),(65,495)
pygame.draw.polygon(screen, [128, 128, 128], [[100,430],[200,430],[255,530],[50,530],[65,495]], 2)#teeb halli hulknurga tipu koordinaatidega (100,430),(200,430),(255,530),(50,530),(65,495)


pygame.display.flip()# värskendab ekraani



# selle jaoks et aken ära ei kaoks ja kinni saaks panna, internetist võetud.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()