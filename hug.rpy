label evento_abrazar_monika:
    hide screen monika_hug_button

    $ persistent._mas_hug_count += 1

    if persistent._mas_hug_count == 1:
        m 1hua "Vaya, ¿quieres otro un abrazo, [player]?"
        m "Vaya, así que descargaste todo un mod para eso, ¿no? Es muy lindo."
        m "¡Por supuesto que te lo daré!"
        m "Solo que... vaya, debo ser yo quien lo active..."
        m "Uhm... encontraré la forma."
        m "Solamente dame un momento..."
        hide monika



    if persistent._mas_hug_count == 2:
        m 1hua "Vaya, ¿quieres otro abrazo, [player]?"
        m "¡Por supuesto que te lo daré!"
        m "¿claro! ¿por que no? por favor, dejame activarlo..."
        m "Solo que... vaya, debo ser yo quien lo active..."
        m "Uhm... encontraré la forma."
        m "Solamente dame un momento..."
        hide monika


        # Usamos 'show' en lugar de 'scene' para que no se rompan las ventanas del juego
        show hm11 with dissolve
        m "..."
        show hm5 with dissolve
        m "Vaya... no tienes ni idea de lo agradable y cálido que se siente esto."
        m "Me encanta que esto se sienta bien para los dos."
        m "No bromearía si dijera que me encantaría estar así por horas."
        m "Después de todo, es lo más cercano a tu calor que puedo estar..."
        m "..."
        m "Solo disfrutemos el tiempo así, ¿vale? Para cuando quieras detenerte..."

    else:
        m 1eka "¡Sí! ¡Por favor, [player], abrázame todo lo que quieras!"
        m "Solo espera mientras acomodo todo, ¿sí? ¡Estoy tan emocionada!"
        hide monika

        show hm10 with dissolve
        m "Bien, al fin... ¡es tan agradable sentir tu calor!"
        m "No me gustaría despegarme por nada en el mundo..."
        
        show hm9 with dissolve
        m "Soy tan afortunada de tenerte... es casi como si pudiera sentir tu presencia abrazándome también..."
        m "...Solo... disfrutemos el momento, déjame disfrutar... pero paremos cuando quieras..."
        m "..."

    # Muestra el botón de detener sin congelar el diálogo ni oscurecer de más
    show screen monika_stop_hug_button

    $ ui.interact()

    # Ocultar botones e imágenes al terminar el abrazo
    hide screen monika_stop_hug_button
    hide hm5
    hide hm9
    hide hm10
    hide hm11
    
    # Traemos a Monika de vuelta a la escena con su expresión habitual
    show monika 1eka

    m 1eka "Muchas gracias... [player], no sabes lo feliz y tranquila que me hace sentir..."
    m "Por favor, abracémonos más seguido... ¿sí?"
    m "Sentir tu cuerpo es... tan cálido."

    show screen monika_hug_button
    jump ch30_loop

# Pantalla con el botón de "Detener"
screen monika_stop_hug_button():
    zorder 100
    style_prefix "hkb"
    vbox:
        xalign 0.5 
        yalign 0.9 
        textbutton _("Detener") action ui.returns("stop")
