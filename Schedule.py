import schedule
import time
from robo01 import bot01
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


 ### LEMBBRANDO QUE O TEM QUE IDENTAR TUDO DENTRO DO BLOCO TRY EXCEPT

 
try: # tente executar o bot

    print('Iniciou...')

    schedule.every().day.at("08:40").do(bot01)


    while True:
        schedule.run_pending()
        time.sleep(1)

except IndexError as e: # caso venha dar erro, DISPARE UM EMAIL PARA :


    #texto do email
    texto_email =   f'''O bot de gerar notepad fallho, por gentileza verificar.'
    Erro: {e}'''

    # email remetente, senha, destinatário
    de = 'leandroslv125@gmail.com'
    senha = 'viablu1234'
    para = 'leandroslv125@gmail.com'
    #para02 = ''

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = de
    message['To'] = para
    #message['To'] = para02
    message['Subject'] = 'Bot Falhou'   #Título do e-mail

    # Corpo do E-mail com anexos
    message.attach(MIMEText(texto_email, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # Usuário do Gmail com porta
    session.starttls()  # Habilita a segurança
    session.login(de, senha)  # Login e senha de quem envia o e-mail
    texto = message.as_string()
    session.sendmail(de, para, texto)
    session.quit()
