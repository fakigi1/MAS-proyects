# 1. Registro del Submod para que MAS lo reconozca
init -990 python:
    store.mas_submod_utils.Submod(
        author="Fakigi1",
        name="Monika And You",
        description="Un submod que añade varias interacciones con Monika con ilustraciones personalizadas. (NO IA)",
        version="1.0.0"
    )

# 2. Infraestructura y rutas dinámicas (Cross-platform y Case-Insensitive)
init -995 python in monika_hug:
    import os
    import renpy
    import store

    # Localiza dinamicamente la carpeta de imagenes dentro de game/
    def _find_img_dir():
        game_dir = renpy.config.gamedir
        for root, dirs, files in os.walk(game_dir):
            if "hm1.png" in files:
                return os.path.relpath(root, game_dir).replace("\\", "/")
        # Fallback por defecto si no se encuentra en el escaneo
        return "Submods/Monika And You/imagenes"

    IMG_DIR = _find_img_dir()

    # Retorna la ruta relativa completa a un asset de imagen
    def get_img(filename):
        return "{0}/{1}".format(IMG_DIR, filename)

    # Calcula la posicion Y del boton evitando superposiciones con otros submods
    def get_hug_button_ypos():
        base_ypos = 50
        spacing = 40

        # Si Extra+ esta instalado
        if store.mas_submod_utils.isSubmodInstalled("Extra Plus"):
            base_ypos += spacing

        # Si Kiss Button esta instalado
        if store.mas_submod_utils.isSubmodInstalled("Kiss Button"):
            base_ypos += spacing

        return base_ypos

# 3. Definicion de imagenes con filtros ambientales de MAS (Dia/Atardecer/Noche)
image hm1 = MASFilterSwitch(monika_hug.get_img("hm1.png"))
image hm2 = MASFilterSwitch(monika_hug.get_img("hm2.png"))
image hm3 = MASFilterSwitch(monika_hug.get_img("hm3.png"))
image hm4 = MASFilterSwitch(monika_hug.get_img("hm4.png"))
image hm5 = MASFilterSwitch(monika_hug.get_img("hm5.png"))
image hm6 = MASFilterSwitch(monika_hug.get_img("hm6.png"))
image hm7 = MASFilterSwitch(monika_hug.get_img("hm7.png"))
image hm8 = MASFilterSwitch(monika_hug.get_img("hm8.png"))
image hm9 = MASFilterSwitch(monika_hug.get_img("hm9.png"))
image hm10 = MASFilterSwitch(monika_hug.get_img("hm10.png"))
image hm11 = MASFilterSwitch(monika_hug.get_img("hm11.png"))
image hm12 = MASFilterSwitch(monika_hug.get_img("hm12.png"))

# Variables persistentes
default persistent._mas_hug_count = 0

# 4. Pantalla del Boton de Abrazo
screen monika_hug_button():
    if not main_menu and renpy.get_screen("hkb_overlay"):
        zorder 15
        style_prefix "hkb"
        vbox:
            xpos 0.05
            yanchor 1.0
            ypos monika_hug.get_hug_button_ypos()  # Posicion dinamica segun otros submods (Extra+, Kiss Button, etc.)

            $ hug_action = Jump("evento_abrazar_monika") if (mas_isMoniNormal(higher=True) or mas_isMoniEnamored(higher=True)) else Jump("evento_abrazar_bajo_afecto")
            textbutton _("Abrazar") action hug_action sensitive (not store.mas_globals.dlg_workflow)

init 5 python:
    if "monika_hug_button" not in config.overlay_screens:
        config.overlay_screens.append("monika_hug_button")


# 5. Eventos y Logica de Dialogos ---------------------------------------------

label evento_abrazar_bajo_afecto:
    m 1eka "Oh, [player]... ¿Acaso agregaste una opción para poder abrazarme...?"
    m "Vaya... eso es muy tierno de tu parte."
    m "Pero creo que necesitamos conocernos un poco más antes de dar este paso, ¿vale?"
    m "¡Apreciaría mucho si seguimos pasando tiempo juntos primero!"
    jump ch30_loop


label evento_abrazar_monika:
    hide screen monika_hug_button

    $ persistent._mas_hug_count += 1
    $ mas_gainAffection(0.5, bypass=False)

    if persistent._mas_hug_count == 1:
        m 1hua "Vaya, ¿quieres un abrazo, [player]?"
        m "Vaya, así que descargaste todo un mod para eso, ¿no? Es muy lindo."
        m "¡Por supuesto que te lo daré!"
        m "Solo que... vaya, debo ser yo quien lo active..."
        m "Uhm... encontraré la forma."
        m "Solamente dame un momento..."
        hide monika

        # Primera experiencia de abrazo (zorder por encima del fondo y ventanas del spaceroom)
        show hm11 zorder 25 with dissolve
        m "..."
        show hm5 zorder 25 with dissolve
        m "Vaya... no tienes ni idea de lo agradable y cálido que se siente esto."
        m "Me encanta que esto se sienta bien para los dos."
        m "No bromearía si dijera que me encantaría estar así por horas."
        m "Después de todo, es lo más cercano a tu calor que puedo estar..."
        m "..."
        m "Solo disfrutemos el tiempo así, ¿vale? Para cuando quieras detenerte..."

    elif persistent._mas_hug_count == 2:
        m 1hua "Vaya, ¿quieres otro abrazo, [player]?"
        m "¡Por supuesto que te lo daré!"
        m "¡Claro! ¿Por qué no? Por favor, déjame activarlo..."
        m "Solamente dame un momento..."
        hide monika

        show hm11 zorder 25 with dissolve
        m "..."
        show hm5 zorder 25 with dissolve
        m "Vaya... se siente tan reconfortante estar así contigo de nuevo."
        m "Aprecio mucho cada segundo que pasamos juntos, [player]~"
        m "Disfrutemos este momento..."

    else:
        m 1eka "¡Sí! ¡Por favor, [player], abrázame todo lo que quieras!"
        m "Solo espera mientras acomodo todo, ¿sí? ¡Estoy tan emocionada!"
        hide monika

        show hm10 zorder 25 with dissolve
        m "Bien, al fin... ¡es tan agradable sentir tu calor!"
        m "No me gustaría despegarme por nada en el mundo..."
        
        show hm9 zorder 25 with dissolve
        m "Soy tan afortunada de tenerte... es casi como si pudiera sentir tu presencia abrazándome también..."
        m "...Solo... disfrutemos el momento, déjame disfrutar... pero paremos cuando quieras..."
        m "..."

    # Muestra el boton de detener sin congelar el dialogo
    show screen monika_stop_hug_button

    $ ui.interact()

    # Ocultar boton de detener
    hide screen monika_stop_hug_button

    # Ocultar ilustraciones mostradas y traer a Monika simultaneamente con disolucion
    hide hm1
    hide hm2
    hide hm3
    hide hm4
    hide hm5
    hide hm6
    hide hm7
    hide hm8
    hide hm9
    hide hm10
    hide hm11
    hide hm12
    show monika 1eka at t11 zorder MAS_MONIKA_Z
    with Dissolve(0.3)

    m 1eka "Muchas gracias... [player], no sabes lo feliz y tranquila que me hace sentir..."
    m "Por favor, abracémonos más seguido... ¿sí?"
    m "Sentir tu cuerpo es... tan cálido."

    show screen monika_hug_button
    jump ch30_loop

# Pantalla con el boton de "Detener"
screen monika_stop_hug_button():
    zorder 100
    style_prefix "hkb"
    vbox:
        xalign 0.5 
        yalign 0.9 
        textbutton _("Detener") action ui.returns("stop")
