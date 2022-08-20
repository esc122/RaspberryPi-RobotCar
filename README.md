# RaspberryPi-RobotCar
  
Raspberry Piにて作成したロボットカーにおいて  
作成した部分のソースコードです。  

## 概要（ProtoPediaに記載）
[Raspberry Piロボットカー作成](https://protopedia.net/prototype/3058 "Raspberry Piロボットカー作成")  
  

### ■コントローラで遠隔操作用
**joy_sub_raspi_move.py**  
Raspberry Piのモータをコントローラ（ジョイスティック）から  
遠隔操作するPythonプログラム  
（ROSでは、sudoでPythonを実行できないためRPi.GPIOは使えない。  
このため「pigpio」を使用しGPIOからモーターを動かす）  
「sudo pigpiod」してROSで動かす  

[![](https://img.youtube.com/vi/KuJdXyhc9Lg/0.jpg)](https://www.youtube.com/watch?v=KuJdXyhc9Lg)
<p>
  
### ■Uniry用
**Tf_Move.cs**  
Unityで位置と角度のデータからオブジェクトを動かすスクリプト  

[![](https://img.youtube.com/vi/D4HmZw1sfcI/0.jpg)](https://www.youtube.com/watch?v=D4HmZw1sfcI)
<p>

### ■Navigationで自動走行用
**/launch**  
move_baseを起動するlanchファイル  
**/param**  
パラメータ設定のyamlファイル   
 **navi_raspi_move.py**  
Raspberry Piのモータをトピックcmd_velから  
自動走行するPythonプログラム  
（ROSでは、sudoでPythonを実行できないためRPi.GPIOは使えない。  
このため「pigpio」を使用しGPIOからモーターを動かす）  
「sudo pigpiod」してROSで動かす  
＊後退できないので壁にぶつかると動かなくなります。。  

[![](https://img.youtube.com/vi/EbqeJYNXlME/0.jpg)](https://www.youtube.com/watch?v=EbqeJYNXlME)
<p>

