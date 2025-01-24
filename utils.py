import os, sys, time

def clean_screen():

  os.system("cls") if os.name == "nt" else os.system("clear")

def print_slow(text,delay = 0.015):

  for char in text:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(delay)
  print()

def progress_bar(percentual, largura=40, mensagem="EXECUTANDO"):

  preenchido = int(percentual / 100 * largura)
  barra = '█' * preenchido + '░' * (largura - preenchido)

  animacao_reticencias = ['.', '..', '...']
  animacao = animacao_reticencias[int((percentual / 100) * len(animacao_reticencias)) % len(animacao_reticencias)]

  progresso = f'\r[{barra}] {mensagem} {percentual:.0f}% {animacao}'
  sys.stdout.write(progresso)
  sys.stdout.flush()


def loading_simulator(tempo_total, largura_barra=50):

  intervalos = 100
  intervalo_tempo = tempo_total / intervalos

  for i in range(intervalos + 1):
      percentual = i
      progress_bar(percentual, largura_barra)
      time.sleep(intervalo_tempo)
  print()