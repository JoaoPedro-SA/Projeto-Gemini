

def Configuracao_IA(x):
    temp = 1
    top_k = 0
    top_p = 0.95
    token = 1200
    escolha_IA = "gemini-1.5-pro-latest"
    IA = 'gemini-1.5-pro-latest'
    key_IA = x 
    while True:
        menu = """
    Configuração da IA
--------------------------------------------------
[1] Nivel de Criatividade (temperature)
[2] top_p   [3] top_k   [4] Quantidade maxima de Texto
[5] Modelo da IA [6] Troca ou colocar Chave da API.
[7] sair         [8] Help

--------------------------------------------------

|| """
        menu_modelo_IA = """
--------------------------------------
[1] Gemini 1.0 Pro  // Otimizado para Tarefas de linguagem natural, chat de código e texto com várias interações e geração de código
[2] Gemini 1.5 Pro  // Otimizado para Tarefas complexas de raciocínio, como geração de código e texto, edição de texto, solução de problemas, extração e geração de dados.
[3] Gemini 1.5 Flash // Otimizado para Desempenho rápido e versátil em diversas tarefas

--------------------------------------
|| """


        escolha = int(input(menu))
        if escolha == 7:
            break
        while True:
            if escolha < 1 or escolha > 8 :
                escolha = int(input(menu))
            else:
                break
        while True:
            if escolha == 1:
                temp = float(input("\nQual vai ser o nivel  (- criativo) 0.00 a 1.00 (+ criativo) \n? "))
                if temp <= 1 and temp >= 0:
                    break
                continue
            elif escolha == 3:
                top_k = float(input("Qual e o nivel do top_k da IA de 0.00 a 1.00?  "))
                if temp <= 1 and temp >= 0:
                    break
                continue
            elif escolha == 2:
                top_p == float(input("Qual e o nivel do top_p da IA 0.00 a 1.00? "))
                break
            elif escolha == 4:
                token = float(input("\nQuantos tokens vc quer no seu texto? (1 token == 1 palavra)\n "))
                break
            elif escolha == 5:
                escolha_IA = float(input(menu_modelo_IA))
                if escolha_IA == 2:
                    IA = 'gemini-1.5-pro-latest'
                    break
                elif escolha_IA == 1:
                    IA = "models/gemini-1.0-pro"
                    break
                elif escolha_IA == 3:
                    IA = "gemini-1.5-flash-latest"
                    break
                else:
                    continue
            elif escolha == 6:
                print("""
                      
Se caso vc não tenha a chave para acessa a API do Gemini Por favor
acesse esse link e solicite a sua chave
# https://aistudio.google.com/app/prompts/new_chat
                      
           Totorial Passo a Passo
# https://www.youtube.com/watch?v=OVnnVnLZPEo (English)
# https://www.youtube.com/watch?v=rYF1PQpZ0c8 (PT-BR)
                      
                      """)
                key_IA = input("Cole aqui a nova chave para o gemini:\n\n|| ")
                break
            elif escolha == 8:
                text = """
temperature: Este parâmetro controla a aleatoriedade na geração de texto. Valores mais baixos resultam em saídas mais determinísticas e repetitivas, enquanto valores mais altos aumentam a criatividade e a diversidade das respostas. Um valor de 1 é um bom equilíbrio entre previsibilidade e criatividade.

top_p: Conhecida como amostragem de núcleo, top_p considera os tokens com a probabilidade cumulativa p mais alta. Com top_p definido como 0.95, a geração de texto é limitada aos tokens que juntos têm 95% de probabilidade cumulativa, o que ajuda a evitar respostas irrelevantes ou incoerentes.

top_k: Este parâmetro define quantos dos tokens mais prováveis são considerados na geração de cada token subsequente. Com top_k definido como 0, não há limite no número de tokens considerados, permitindo uma maior variedade de respostas. Se um valor específico fosse definido, como 50, apenas os 50 tokens mais prováveis seriam considerados.

max_output_tokens: Este parâmetro define o número máximo de tokens (palavras ou partes de palavras) que a IA pode gerar em uma única resposta. Com max_output_tokens definido para 1200, a resposta gerada será restrita a 1200 tokens, o que ajuda a controlar a extensão das respostas e evitar saídas muito longas.
                
                """
                print(text)
                num = int(input("[1] voltar \n\n|| "))               
                if num == 1:
                   break
                continue
                          
        
        return temp,top_k,top_p,token,IA,key_IA

                
key_IA = ""      
   
if key_IA == "":
    key_IA = input("""

Se caso vc não tenha a chave para acessa a API do Gemini Por favor
acesse esse link e solicite a sua chave
# https://aistudio.google.com/app/prompts/new_chat
                      
           Totorial Passo a Passo
# https://www.youtube.com/watch?v=OVnnVnLZPEo (English)
# https://www.youtube.com/watch?v=rYF1PQpZ0c8 (PT-BR)

Cole aqui a nova chave para o gemini:\n\n|| """)
    
print("""

** BEM VINDO AO GEMINI **

Aperta enter para continuar      """)

menu = input()

menu = """


                MENU PRINCIPAL
|-----------------------------------------------|
|[1] Configurar IA  [2] Inicia O chat           | 
|[3] Sair           [4] Colocar uma API keys    |
|                                               | 
|(!) VC SO PODERAR MANDA 3 MENSAGENS PARA O CHAT|  
|-----------------------------------------------|
    
|| """

escolha = int(input(menu))
while True:
    if escolha < 0 and escolha > 3:
        escolha = int(input(menu))
    else:
        break
temp = 1
top_k = 0
top_p = 0.95
token = 1200
escolha_IA = "gemini-1.5-pro-latest"
IA = escolha_IA
e = ""
while True:    
    if escolha == 1:
        temp,top_k,top_p,token,escolha_IA,key_IA = Configuracao_IA(key_IA)
        escolha = int(input(menu))
        continue
    elif escolha == 2:
        break
    elif escolha == 3:
        import sys
        sys.exit()
    elif escolha == 4:
        key_IA = input("Cole aqui a nova chave para o gemini:\n\n|| ")
        continue
    else:
        escolha = int(input(menu))
        continue
        
    
# print("")
# print("temp = ", temp)
# print("top_p = ", top_p)
# print("top_k = ", top_k)
# print("token = ", token)
# print("escolha_IA = ", escolha_IA)
# print("key_IA = ", key_IA)

     
     
     
import google.generativeai as genai
# Chave para acessar o serviço da google
genai.configure(api_key=key_IA)

# Set up the model
# configuração de funcionamento do gemini 
generation_config = {
"temperature": float(temp),
"top_p": top_p,
"top_k": int(top_k),
"max_output_tokens": int(token),
     }
# faz a restrição de linguagens ofensivas.
safety_settings = [
     {
"category": "HARM_CATEGORY_HARASSMENT",
"threshold": "BLOCK_MEDIUM_AND_ABOVE"
     },
     {
"category": "HARM_CATEGORY_HATE_SPEECH",
"threshold": "BLOCK_MEDIUM_AND_ABOVE"
     },
     {
"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
"threshold": "BLOCK_MEDIUM_AND_ABOVE"
     },
     {
"category": "HARM_CATEGORY_DANGEROUS_CONTENT",
"threshold": "BLOCK_MEDIUM_AND_ABOVE"
     },
     ]
     # escolhendo o modelo e passando seus parametros
print(f"\nmodelo a ser usado sera {escolha_IA}\n")
model = genai.GenerativeModel(model_name=escolha_IA,
                                   generation_config=generation_config,
                                   safety_settings=safety_settings)

Resposta_Gemini = ""
for i in range(3):
    convo = model.start_chat(history=[
     ])
    msg = input("Voce =>  ")
    mensagem_para_Gemnni = msg
    convo.send_message(mensagem_para_Gemnni)
    Resposta_Gemini = convo.last.text
   # print(convo.last.text)
    print(f"\nGemini => {Resposta_Gemini}\n\nquantidade de chamadas ({i+1}° | 3°)\n")
    
     

    
    