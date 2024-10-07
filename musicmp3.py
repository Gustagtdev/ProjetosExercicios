import pygame 


# Inicializa o pygame
pygame.init()
# Carrega o arquivo de áudio
pygame.mixer.music.load('DinoRock.mp3')

#regula o volume da música(opcional)
pygame.mixer.music.set_volume(0.3)
# Reproduz o áudio
pygame.mixer.music.play()
input()
pygame.event.wait()

pygame.quit()

'''
# Outra forma de reproduzir o aúdio
pygame.init()
# Carrega o arquivo de áudio
pygame.mixer.music.load('numb.mp3')

#regula o volume da música(opcional)
pygame.mixer.music.set_volume(0.3)

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)

# Finaliza o pygame
pygame.quit()
'''