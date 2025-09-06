import pyautogui, time

time.sleep(0.5)

while True: # Só irá parar de procurar até o item ser encontrado
    time.sleep(0.5)
    try: # Verificar se a imagem foi localizada
        pos = pyautogui.locateOnScreen('item.png', confidence=0.9) # Localizar o item e definir a precisão (O quão perto ele irá achar a posição), necessário ter imagem com o nome "item.png"
        if pos: # Se sim
            print(f'Item encontrado. Posição: {pos}')
            pyautogui.click(pos)
            break
        else: # Se não
            print('Item não encontrado! Tentando novamente...')
    except Exception as excecao: # Se houver uma exceção enquanto o try estiver rodando, irá parar o processo e mostrar qual foi a exceção
        print(f'Ocorreu um erro: {excecao}')