import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def init_script():
    acao()

def dica():
    copia_dica = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/nav/div[2]/div[1]/div/div").text
    print(copia_dica + "\n")
    return copia_dica.lower()

def answers(guess_an_answer):
    try:
        driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/form/label/input").send_keys(guess_an_answer)
        driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/form/label/input").send_keys(Keys.ENTER)
    except Exception as e:
        #print(e)
        acertou_check()

textbox_status = True
def acertou_check() :
    textbox_status = False


def write_file(write_f) :
    file = open("dicionario.txt", "a")
    file.write(write_f + "\n")
    file.close()

def read_file(metodo, word) :
    file = open("dicionario.txt", "r")
    if metodo == "ler_todos" :
        lidos = 0
        for line in file:
            lidos += 1
        return lidos

    elif metodo == "procurar_igual" :
        for line in file:
            line = line.rstrip('\n')
            if len(line) == len(word) and textbox_status :
                i = 0
                for letra_line in line :
                    if letra_line == word[i] or word[i] == " " :
                        i += 1
                        if i == len(word) :
                            answers(line)
                            time.sleep(1)
                    else:
                        i = 0
                        break
        if not textbox_status :
            print("Textbox bloqueada")
    elif metodo == "checar_se_existe" :
        for line in file:
            if line == word + "\n" :
                return True;
def acao():
    while(True) :
        textbox_status = True
        acao_script = input("Verificar dica(vd) | Nova palavra(np): ")
        if acao_script == "vd" :
            if len(dica()) > 0 :
                dica_recebida = dica()
                read_file("procurar_igual", dica_recebida)
        elif acao_script == "np" :
            new_word = input("Nova palavra: ")
            if not read_file("checar_se_existe", new_word) :
                write_file(new_word)
                print("Palavra adicionada!\n\nTotal de palavras agora: " + str(read_file("ler_todos", 0)))
            else:
                print("Palavra já existente.\n")

chrome_options = Options()
chrome_options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://gartic.com.br/")
driver.maximize_window()

command_script = input("Comando? iniciar(i): ")

if command_script == "i" :
    init_script()
else:
    exit()
