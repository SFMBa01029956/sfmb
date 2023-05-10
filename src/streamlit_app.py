import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import altair as alt
import pandas as pd
import streamlit as st
import time
from flask import Flask

def trayectoryVALUES(vo, phiDeg, soy, t,aoy):
    phi = np.radians(phiDeg)
    vox = vo*np.cos(phi)
    voy = vo*np.sin(phi)
    rx = vox*t
    ry = (-1/2*aoy*(t**2))+(voy*t)+(soy)
    return rx, ry


def trayectoryVALUES_wdg(vo, phiDeg, soy, m, D, dt, aoy):

    phi = np.radians(phiDeg)
    vox = vo*np.cos(phi)
    voy = vo*np.sin(phi)
    v = vo
    vx = vox
    vy = voy
    sx = 0
    sy = soy
    ax = -(D/m)*v*vx
    ay = -aoy-(D/m)*v*vy
    tN = 0
    vList = [v]
    vxList = [vx]
    vyList = [vy]
    sxList = [sx]
    syList = [sy]
    axList = [ax]
    ayList = [ay]
    tList = [tN]
    for i in range(1000):
        vxN = vx + ax*dt
        vyN = vy + ay*dt
        vN = np.sqrt(vxN**2 + vyN**2)
        sxN = (sx) + (vxN*dt) + 0.5*ax*(dt**2)
        syN = (sy) + (vyN*dt) + 0.5*ay*(dt**2)
        axN = -(D/m)*v*vxN
        ayN = -aoy-(D/m)*v*vyN
        tN += dt
        vList.append(vN)
        vxList.append(vxN)
        vyList.append(vyN)
        sxList.append(sxN)
        syList.append(syN)
        axList.append(axN)
        ayList.append(ayN)
        tList.append(tN)
        vx = vxN
        vy = vyN
        v = vN
        sx = sxN
        sy = syN
        ax = axN
        ay = ayN
    trayectoryMATRIX = [sxList,syList,vList,vxList,vyList,axList,ayList,tList]
    return trayectoryMATRIX


def graph_wdg(matrix_): #SOLO CON RESISTENCIA
    lastsy = min(matrix_[1])
    lastsyINDEX = matrix_[1].index(lastsy)
    st.text(lastsyINDEX)
    lastsx = float(matrix_[0][lastsyINDEX])
    st.text(lastsx)
    maxsy = max(matrix_[1])
    maxsyINDEX = matrix_[1].index(maxsy)
    maxsx = matrix_[0][maxsyINDEX]
    landx = round(lastsx,2)
    maxx = round(maxsx,2)
    maxy = round(maxsy,2)

    limitx = round(lastsx, -2)
    if limitx < 1000:
        limitx += 50
        if limitx -50 > lastsx:
            limitx -= 50
        if limitx -20 > lastsx:
            limitx -= 20
        if limitx -10 > lastsx:
            limitx -= 10
        if limitx -6 > lastsx:
            limitx -= 6
        if limitx -5 > lastsx:
            limitx -= 5
        if limitx -3 > lastsx:
            limitx -= 3
        if limitx -2 > lastsx:
            limitx -= 2
        if limitx -1 > lastsx:
            limitx -= 1       
    limity = round(maxsy, -3)
    if limity -1000 > maxsy:
        limity -= 1000
    elif limity < maxsy:
        limity += 1000

    #GRAFICA CON MATPLOT
    fig, ax = plt.subplots()
    x = matrix_[0]
    ax.plot(x, matrix_[1])
    plt.grid()
    plt.axis('scaled')
    st.title("Trayectoria del proyectil con resistencia del aire")
    plt.xlim([0,round(limitx,-3)+1000])
    plt.ylim([0,limity])
    _ = plt.xticks(np.arange(0,limitx,1000))
    _ = plt.yticks(np.arange(0,limity,1000))
    st.pyplot(fig)
    #GRÁFICA CON ALTAIR
    #path = pd.DataFrame({'x': matrix_[0],'y':matrix_[1]})
    #st.altair_chart(alt.Chart(path).mark_line(clip=True).encode(alt.X('x',scale=alt.Scale(domain=[0,limitx])),alt.Y('y',scale=alt.Scale(domain=[0,limity]))))
    return landx,maxx,maxy


def graph(list_): #SOLO SIN RESISTENCIA
    lastsy = min(abs(list_[1]))
    lastsyINDEX = np.where(abs(list_[1])==lastsy)
    lastsx = float(list_[0][lastsyINDEX])
    st.text(lastsx)
    maxsy = max(list_[1])
    maxsyINDEX = np.where(list_[1]==maxsy)
    maxsx = float(list_[0][maxsyINDEX])
    landx = round(lastsx,2)
    maxx = round(maxsx,2)
    maxy = round(maxsy,2)

    fig,ax = plt.subplots()
    ax.plot(list_[0],list_[1])
    plt.grid()
    plt.axis('scaled')
    st.title("Trayectoria del proyectil sin resistencia del aire")
    plt.xlim([0,110])
    plt.ylim([0,40])
    _ = plt.xticks(np.arange(0,6001,1000))
    _ = plt.yticks(np.arange(0,6001,1000))
    st.pyplot(fig)

    return landx,maxx,maxy


def graphboth(matrix_,list_): #AMBAS
    lastsy = min(abs(list_[1]))
    lastsyINDEX = np.where(abs(list_[1])==lastsy)
    lastsx = float(list_[0][lastsyINDEX])
    st.header(":volcano:")
    maxsy = max(list_[1])
    maxsyINDEX = np.where(list_[1]==maxsy)
    maxsx = float(list_[0][maxsyINDEX])
    landx = round(lastsx,2)
    maxx = round(maxsx,2)
    maxy = round(maxsy,2)

    limitx = round(lastsx, -2)
    if limitx < 1000:
        limitx += 50
        if limitx -50 > lastsx:
            limitx -= 50
        if limitx -20 > lastsx:
            limitx -= 20
        if limitx -10 > lastsx:
            limitx -= 10
        if limitx -6 > lastsx:
            limitx -= 6
        if limitx -5 > lastsx:
            limitx -= 5
        if limitx -3 > lastsx:
            limitx -= 3
        if limitx -2 > lastsx:
            limitx -= 2
        if limitx -1 > lastsx:
            limitx -= 1       
    limity = round(maxsy, -3)
    if limity -1000 > maxsy:
        limity -= 1000
    elif limity < maxsy:
        limity += 1000

    fig, ax = plt.subplots()
    ax.plot(list_[0], list_[1], label = "Sin Resistencia del aire")
    ax.plot(matrix_[0], matrix_[1], label = "Con Resistencia del aire")
    plt.grid()
    plt.axis('scaled')
    st.title("Trayectoria del proyectil con resistencia del aire")
    plt.xlim([0,round(limitx,-3)+1000])
    plt.ylim([0,limity])
    _ = plt.xticks(np.arange(0,limitx,1000))
    _ = plt.yticks(np.arange(0,limity,1000))
    _ = plt.legend()
    st.pyplot(fig)

    lastsx = matrix_[0][-1]
    lastsy = matrix_[1][-1]
    maxsy = max(matrix_[1])
    maxsyINDEX = matrix_[1].index(maxsy)
    maxsx = matrix_[0][maxsyINDEX]
    landx = round(lastsx,2)
    maxx = round(maxsx,2)
    maxy = round(maxsy,2)

    return landx,maxx,maxy

 
def graph2EXAMEN_ARG(matrix_,matrix2_): #DOS TRAYECTORIAS EXAMEN ARG
    lastsy = min(matrix_[1])
    lastsyINDEX = matrix_[1].index(lastsy)
    st.text(lastsyINDEX)
    lastsx = float(matrix_[0][lastsyINDEX])
    st.text(lastsx)
    maxsy = max(matrix_[1])
    maxsyINDEX = matrix_[1].index(maxsy)
    maxsx = matrix_[0][maxsyINDEX]
    landx = round(lastsx,2)
    maxx = round(maxsx,2)
    maxy = round(maxsy,2)

    limitx = round(lastsx, -2)
    if limitx < 1000:
        limitx += 50
        if limitx -50 > lastsx:
            limitx -= 50
        if limitx -20 > lastsx:
            limitx -= 20
        if limitx -10 > lastsx:
            limitx -= 10
        if limitx -6 > lastsx:
            limitx -= 6
        if limitx -5 > lastsx:
            limitx -= 5
        if limitx -3 > lastsx:
            limitx -= 3
        if limitx -2 > lastsx:
            limitx -= 2
        if limitx -1 > lastsx:
            limitx -= 1       
    limity = round(maxsy, -3)
    if limity -1000 > maxsy:
        limity -= 1000
    elif limity < maxsy:
        limity += 1000

    fig, ax = plt.subplots()
    x = matrix_[0]
    ax.plot(x, matrix_[1])
    y = matrix2_[0]
    ax.plot(y, matrix2_[1])
    plt.grid()
    plt.axis('scaled')
    st.title("Trayectoria del proyectil con resistencia del aire")
    plt.xlim([0,round(limitx,-3)+1000])
    plt.ylim([0,limity])
    _ = plt.xticks(np.arange(0,limitx,1000))
    _ = plt.yticks(np.arange(0,limity,1000))
    st.pyplot(fig)

    lastsx = matrix_[0][-1]
    lastsy = matrix_[1][-1]
    maxsy = max(matrix_[1])
    maxsyINDEX = matrix_[1].index(maxsy)
    maxsx = matrix_[0][maxsyINDEX]
    landx = round(lastsx,2)
    maxx = round(maxsx,2)
    maxy = round(maxsy,2)

    return landx,maxx,maxy


def graphSPECIAL(matrix_,list_,t): #TIEMPO, VELOCIDAD Y ACELERACIÓN
    st.title("Gráficas de tiempo, velocidad y aceleración")
    
    fig, ax = plt.subplots()
    ax.plot(t,list_[1],label="Vacio")
    ax.plot(matrix_[7],matrix_[1],label="Con Resistencia de Aire")
    plt.title("Altura contra tiempo")
    plt.legend()
    plt.xlim([0,50])
    _ = plt.ylim([0,6000])
    plt.tight_layout()
    st.pyplot(fig)
    
    fig, ax = plt.subplots()
    ax.plot(matrix_[7],matrix_[3],label="vx")
    ax.plot(matrix_[7],matrix_[4],label="vy")
    ax.plot(matrix_[7],matrix_[2],label="v")
    plt.title("Velocidad contra tiempo")
    plt.grid()
    plt.legend()
    plt.xlim([0,160])
    plt.tight_layout()
    st.pyplot(fig)
  
    fig, ax = plt.subplots()
    ax.plot(matrix_[7],matrix_[5],label="ax")
    ax.plot(matrix_[7],matrix_[6],label="ay")
    plt.title("Aceleracion contra tiempo")
    plt.legend()
    plt.xlim([0,150])
    plt.tight_layout()
    st.pyplot(fig)


def initial_parameters():
    st.sidebar.title(':gear: Configuración')
    st.text("")
    st.header("Establece los parámetros iniciales:")
    vo = st.slider("Velocidad inicial (metros sobre segundo): ",0,200,160)
    phiDeg = st.slider("Ángulo de disparo (grados): ",0,90,40)
    t = np.linspace(0,1000,900)
    if st.sidebar.checkbox("Modificar proyectil"):
        m = st.sidebar.slider("Masa del proyectil",1.00,2000.00,700.00)
        dm = st.sidebar.slider("Diámetro del proyectil",0.01,2.00,0.46)
        st.text(f"Masa del proyectil: {m} kg") 
        st.text(f"Diámetro del proyectil: {dm} m")
        st.sidebar.text("________________________________________")
    else:
        m = 700.00
        dm = 0.46
    if st.sidebar.checkbox("Configuración avanzada"):
        volcano = st.sidebar.radio("Volcán",("Popocatépetl","Kilimanjaro","Vesubio","Krakatoa","Personalizado"))
        if volcano == "Popocatépetl":
            soy = 5426
        elif volcano == "Kilimanjaro":
            soy = 4906
        elif volcano == "Vesubio":
            soy = 1281
        elif volcano == "Krakatoa":
            soy = 813
        elif volcano == "Personalizado":
            volcano = "Indefinido"
            volcano = st.sidebar.text_input("Establece un nombre para el volcán: ")
            soy = "Indefinida"
            soy = st.sidebar.number_input("Altura en metros:")
        st.text(f"Volcán: {volcano}, Altura: {soy} m")
        if st.sidebar.checkbox("Modificar constantes [Experimental]"):
            aoy = st.sidebar.slider("Valor de la gravedad:",-10.00,10.00,9.81)
            C = st.sidebar.slider("Coeficiente de arrastre",0.01,1.00,0.47)
            st.text(f"Valor de la gravedad: {aoy} m/s^2")
            st.text(f"Coeficiente de arrastre: {C}")
        else:
            aoy = 9.81 #GRAVEDAD#
            C = 0.47
        st.sidebar.text("________________________________________")
    else:
        soy = 5426
        aoy = 9.81 #GRAVEDAD#
        C = 0.47
    landin = False
    maxin = False
    if st.sidebar.checkbox("Mostrar punto de aterrizaje"):
        landin = True
    if st.sidebar.checkbox("Mostrar punto máximo"):
        maxin = True
    if st.sidebar.checkbox("Considerar resistencia del aire",True): #EMPLEA RESISTENCIA DEL AIRE   
        rho = st.slider("Densidad del aire",0.0001,2.0000,1.2754)
        r = dm/2
        A = np.pi*r**2
        st.text(f"Área del proyectil: {A} m3")
        dt = 1
        D = (rho*C*A)/2
        if st.sidebar.checkbox("Mostrar tambien trayectoria sin resistencia",True): #MOSTRAR AMBAS TRAYECTORIAS
            if st.sidebar.checkbox("Mostrar gráficas de tiempo, velocidad y aceleración",True):
                if st.button('LANZAR!'):
                    st.write('Lanzando proyectil')
                    time.sleep(1)
                    databox = graphboth(trayectoryVALUES_wdg(vo, phiDeg, soy, m, D, dt,aoy),trayectoryVALUES(vo, phiDeg, soy, t,aoy))
                    if landin:
                        st.subheader("Aterrizaje en:")
                        st.text(f"({databox[0]}, 0.00)")
                    if maxin:
                        st.subheader("Máximo en: ")
                        st.text(f"({databox[1]}, {databox[2]})")
                    graphSPECIAL(trayectoryVALUES_wdg(vo, phiDeg, soy, m, D, dt,aoy),trayectoryVALUES(vo, phiDeg, soy, t,aoy),t)
            elif st.button('LANZAR!'):
                st.write('Lanzando proyectil')
                time.sleep(1)
                databox = graphboth(trayectoryVALUES_wdg(vo, phiDeg, soy, m, D, dt,aoy),trayectoryVALUES(vo, phiDeg, soy, t,aoy))
                #databox = graph2EXAMEN_ARG(trayectoryVALUES_wdg(121, 52, soy, 108.87, 0.012, dt,aoy),trayectoryVALUES_wdg(134, 64, soy,352.36, 0.004, dt,aoy))
                if landin:
                    st.subheader("Aterrizaje en:")
                    st.text(f"({databox[0]}, 0.00)")
                if maxin:
                    st.subheader("Máximo en: ")
                    st.text(f"({databox[1]}, {databox[2]})")
        else: #MOSTRAR SÓLO TRAYECTORIA CON RESISTENCIA
            if st.sidebar.checkbox("Mostrar gráficas de tiempo, velocidad y aceleración",True):
                if st.button('LANZAR!'):
                    st.write('Lanzando proyectil')
                    time.sleep(1)
                    databox = graph_wdg(trayectoryVALUES_wdg(vo, phiDeg, soy, m, D, dt,aoy))
                    if landin:
                        st.subheader("Aterrizaje en:")
                        st.text(f"({databox[0]}, 0.00)")
                    if maxin:
                        st.subheader("Máximo en: ")
                        st.text(f"({databox[1]}, {databox[2]})")
                    graphSPECIAL(trayectoryVALUES_wdg(vo, phiDeg, soy, m, D, dt,aoy),trayectoryVALUES(vo, phiDeg, soy, t,aoy),t)
            elif st.button('LANZAR!'):
                st.write('Lanzando proyectil')
                time.sleep(1)
                databox = graph_wdg(trayectoryVALUES_wdg(vo, phiDeg, soy, m, D, dt,aoy))
                if landin:
                    st.subheader("Aterrizaje en:")
                    st.text(f"({databox[0]}, 0.00)")
                if maxin:
                    st.subheader("Máximo en: ")
                    st.text(f"({databox[1]}, {databox[2]})")
        st.sidebar.text("________________________________________")
    

def startup():
    st.title(f"Ygneus :comet: ")
    st.subheader('*"El juego serio para la trayectoria de un volcán"*')
    
def make():
  startup()
  initial_parameters()
  st.subheader(" © Salvador Milanés Braniff, 2020 ITESM  [Ver 3.0.0]")

@app.route('/streamlit_app', methods=['POST'])
def run_script():
  result = make()