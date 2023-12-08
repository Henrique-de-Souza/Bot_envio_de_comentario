import pyautogui as pg
import time

# mover até a página
pg.moveTo(-815,783, duration=1)

# rolar para o camppo de mensagem
pg.scroll(-1000)

# mover para o campo de mensagem
pg.moveTo(-1036,390, duration=1)
pg.click()

# escrever a mensagem 
pg.typewrite('Esse comentario esta sendo enviado automaticamente pelo codigo a seguir:   ')


# abrir uma nova aba
pg.moveTo(-1316,10, duration=1)
pg.click()
time.sleep(3)

# Mover para o icone do site da ControlC 
pg.moveTo(-524,86, duration=1)
pg.click()

# esperar 10 segundos para a página carregar
time.sleep(10)

# Mover para Vs Code com o código da automação
pg.moveTo(503,390, duration=1)

# clicar em um campo vazio
pg.click()

# selecionar todo o código e colá-lo
pg.hotkey('ctrl', 'a')
pg.hotkey('ctrl', 'c')

# voltar para o site da ControlC
pg.moveTo(-1265,15)
pg.click()

# mover para o campo onde copiarei o código:
pg.moveTo(-977,354, duration=1)
pg.click()

# colar o código copiado
pg.hotkey('ctrl', 'v')
time.sleep(1)

# Mover-se para seta do campo "Enable code highlighting? e clicar
pg.moveTo(-806,626, duration=1)
pg.click()

# mover para sim
pg.moveTo(-806,626, duration=1)
pg.click()


# clicar em "Não sou um robô kkkk"
pg.moveTo(-757,614, duration=1)
pg.click()

# clicar em "submit"
pg.moveTo(-434,591, duration=1)
pg.click()

# esperar a página recarregar
time.sleep(20)

# mover-se para o link gerado
pg.moveTo(-855,290)
pg.click()

# copiar o link
pg.hotkey('ctrl', 'a')
pg.hotkey('ctrl','c')


# voltar para a página da Dev aprender
pg.moveTo(-1433,11, duration=1)
pg.click()

# mover-se para o campo de mensagem mais uma vez
pg.moveTo(-704,383, duration=1)
pg.click()

# colar o link copiado no site da controlc
pg.hotkey('ctrl', 'v')
time.sleep(5)

# Enviar a mensagem
pg.press('ENTER')
