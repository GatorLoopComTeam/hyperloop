#include <Arduino.h>

void pwm_out(){
  // digitalWrite(13, HIGH);
  // delayMicroseconds(60);
  // digitalWrite(13, LOW);
  // delayMicroseconds(60);
  analogWrite(13, 255);
  analogWrite(12, 255);
//   int y=1;
//   while(y==1){
//
//
//   for (int x=0; x<255;x++){
//     analogWrite(13, x);
//     delay(100);
//   }
//   for (int x=255; x>0;x--){
//     analogWrite(13, x);
//     delay(100);
//   }
// }
}

void setup(){
  pinMode(13, OUTPUT); // BLDC PWM Right
  pinMode(12, OUTPUT); // BLDC PWM Left
  pinMode(42, OUTPUT); // BLDC Right Enable
  pinMode(43, OUTPUT); // BLDC Left Enable
  pinMode(40, OUTPUT); // Direction Right
  pinMode(41, OUTPUT); // Direction Left
  pinMode(38, OUTPUT); // Brake Right
  pinMode(39, OUTPUT); // Brake Left

  // int myEraser = 7;
  // TCCR0B &= ~myEraser;
  // int myPrescaler = 2;
  // TCCR0B |= myPrescaler;
}

void loop(){
  digitalWrite(42, HIGH);
  digitalWrite(43, HIGH);
  digitalWrite(40, HIGH);
  digitalWrite(41, HIGH);
  digitalWrite(38, HIGH);
  digitalWrite(39, HIGH);
  delay(1000);
  pwm_out();

}
