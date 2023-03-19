#recomendo transformar o .py em .bat, não se preocupe! o app continua funcionando sem defeitos.
#trabalhos escolares
while (True):
    from playsound import playsound
    import webbrowser


    #assunto inicial
    print('O que deseja saber sobre Nova Zelândia?')

    #variável juntamente ao input para a escolha do insteresse da professora
    escolha = input('1 PIB - 2 História Da Nova Zelândia - 3 Dados Gerais Da Nova Zelândia - 4 Imagens De Nova Zelândia - 5 Fechar Programa ')

    if (escolha == '1'):
        # toque o aúdio desejado
        playsound('audio1.mp3')

    elif (escolha == '2'):
        # toque o aúdio desejado
        playsound('audio2.mp3')

    elif (escolha == '3'):
        # toque o aúdio desejado
        playsound('audio3.mp3')

    elif (escolha == '4'):
        #link da web que deseja abrir
        webbrowser.open_new("https://www.google.com/search?q=nova+zel%C3%A2ndia+imagens&hl=pt-BR&sxsrf=AJOqlzWfjhysA2eVMfTsAJsLCxfTT-bdgw:1678815888406&source=lnms&tbm=isch&sa=X&ved=2ahUKEwivwa_F_Nv9AhVsALkGHbxbAW0Q_AUoAXoECAEQAw&biw=1360&bih=625&dpr=1")

    elif(escolha == '5'):
        break
