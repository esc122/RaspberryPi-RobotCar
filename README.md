# RaspberryPi-RobotCar
  
Raspberry Piにて作成したロボットカーにおいて  
作成した部分のソースコードです。  

[![](https://img.youtube.com/vi/9P2Gq69iAng/0.jpg)](https://www.youtube.com/watch?v=9P2Gq69iAng)
<p>

---------------------------------------
**概要（ProtoPediaに記載）**  
[Raspberry Piロボットカー作成](https://protopedia.net/prototype/3058 "Raspberry Piロボットカー作成")  
  
**joy_sub_raspi_move.py**  
Raspberry Piのモーター操作用  
（ROSでは、sudoでPythonを実行できないためRPi.GPIOは使えない。  
このため「pigpio」を使用しGPIOからモーターを動かす）  
「sudo pigpiod」してROSで動かす  
  
**Tf_Move.cs**  
Unityで位置と角度のデータからオブジェクトを動かすスクリプト  
