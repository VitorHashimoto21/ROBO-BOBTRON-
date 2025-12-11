# ROBO-BOBTRON-
Este projeto apresenta o desenvolvimento de um robô móvel autônomo utilizando uma ESP32 de 38 pinos, programada inteiramente em MicroPython. O robô foi projetado para realizar navegação básica através de leitura de sensores e controle independente dos motores.

## Hardware Utilizado

- ESP32 (38 pinos)
- Shield para ESP32 para facilitar conexões e alimentação;
- Ponte H L298N para controle dos dois motores DC;
- 2 Sensores infravermelhos analógicos para detecção de obstáculos / seguidor de linha;
- 2 baterias de 9V: Uma dedicada à ESP32 Outra dedicada à ponte H L298N e aos motores
Chassi com motores DC e rodas.

## Software
- Código escrito totalmente em MicroPython
- Controle de motores via PWM
- Leitura analógica dos sensores IR
- Lógica de decisão para movimento autônomo

## Objetivo do Projeto

Demonstrar o uso prático da ESP32 com MicroPython em robótica, explorando controle de motores, leitura de sensores e integração de eletrônica básica em um sistema embarcado funcional.
