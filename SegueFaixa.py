from machine import Pin, PWM, ADC
import time

# === SENSORES ===
sensor_esq = ADC(Pin(26))
sensor_dir = ADC(Pin(34))

sensor_esq.atten(ADC.ATTN_11DB)
sensor_dir.atten(ADC.ATTN_11DB)

sensor_esq.width(ADC.WIDTH_12BIT)
sensor_dir.width(ADC.WIDTH_12BIT)

# === MOTORES ===
in1 = Pin(33, Pin.OUT)  # Esq frente
in2 = Pin(13, Pin.OUT)  # Esq trás
in3 = Pin(32, Pin.OUT)  # Dir frente
in4 = Pin(14, Pin.OUT)  # Dir trás

# === ENABLERS ===
ena = PWM(Pin(25), freq=1000) # motor esquerdo
enb = PWM(Pin(21), freq=1000) # motor direito

#==============================================================
#=========================== MOVIMENTOS ========================
#==============================================================

def frente(v=600):
    in1.on()
    in2.off()
    in3.on()
    in4.off()
    ena.duty(v)
    enb.duty(v)

def vira_esquerda():
    in1.off()
    in2.on()
    in3.on()
    in4.off()
    ena.duty(400)
    enb.duty(700)

def vira_direita():
    in1.on()
    in2.off()
    in3.off()
    in4.on()
    ena.duty(700)
    enb.duty(400)

def parar():
    in1.off()
    in2.off()
    in3.off()
    in4.off()
    ena.duty(0)
    enb.duty(0)

def direita_90():
    in1.on()
    in2.off()
    in3.off()
    in4.on()
    ena.duty(400)
    enb.duty(0)

#==============================================================
#=================== PROCEDIMENTO DE ESTACIONAR ===============
#==============================================================

def BARRAESCANEADA():
    # 1) Avançar para passar pela barra
    for i in range(34):
        se = sensor_esq.read()
        sd = sensor_dir.read()
        print(se, sd)

        if se <= TH and sd <= TH:
            frente()

        elif se > TH and sd <= TH:
            vira_esquerda()

        elif se <= TH and sd > TH:
            vira_direita()
            
        else:
            parar()
            
        time.sleep(0.05)

    # 2) Girar ~90° para a direita
    parar()
    direita_90()
    time.sleep(0.8)   # Ajuste fino do seu robo

    parar()
    time.sleep(0.2)

    # 3) Avançar até o interior da vaga 2
    frente(400)
    time.sleep(1)   # Ajustar conforme distância até a vaga

    # 4) Finalizar estacionado
    parar()

    # 5) Fim: fica parado para sempre
    while True:
        parar()
        time.sleep(1)

#==============================================================
#============================= LOOP ===========================
#==============================================================

time.sleep(5)
TH = 250
TH2= 1000
# OBS: os valores de TH e TH2 são ajustáveis para o sensor que utilizamos
# atente-se de calibrar esses valores de acordo com o seu sensor!

while True:
    se = sensor_esq.read()
    sd = sensor_dir.read()
    print(se, sd)

    if se <= TH and sd <= TH:
        frente()

    elif se > TH and sd <= TH:
        vira_esquerda()

    elif se <= TH and sd > TH:
        vira_direita()
        
    elif se > TH2 and sd > TH2:
        BARRAESCANEADA()   # Entra na vaga 2
        
    else:
        parar()
        
    time.sleep(0.05)

