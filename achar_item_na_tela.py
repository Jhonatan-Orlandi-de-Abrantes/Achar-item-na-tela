import pyautogui, time, keyboard as kb

key = 'F8' # Tecla que ativa/desativa o script
confirm = False

def toggle(e): # Função "toggle", ou seja, ativa e desativa o processo com um clique
    global confirm
    confirm = not confirm
    print(f'Condicao = {confirm}')

def search():
    global confirm
    while True:
        if confirm:
            while confirm:
                time.sleep(0.5)
                try:
                    # Verifica primeiro se a imagem que deve ser evitada está na tela
                    evitar = pyautogui.locateOnScreen('evitar_este_item.png', confidence=0.7)
                    if evitar:
                        print('Imagem para EVITAR encontrada. Ignorando tentativa de clique...')
                        continue # Pula para a próxima iteração sem procurar o item
                    
                    # Agora verifica a imagem do item, já que a de evitar não foi encontrada
                    pos = pyautogui.locateOnScreen('item.png', confidence=0.7)
                    if pos:
                        print(f'Item encontrado. Posição: {pos}')
                        pyautogui.click(pos)
                    else:
                        print('Item não encontrado! Tentando novamente...')
                except Exception as e:
                    print(f'Erro ao procurar as imagens: {e}')
        else:
            time.sleep(0.1) # Evitar o uso excessivo de CPU quando inativo

# Associa a tecla para ligar/desligar á função desejada
kb.on_press_key(key, toggle)
# Inicia a busca
search()
