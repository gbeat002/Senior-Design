//'* Author:  Sunil Alexander THE SON OF A BISCUIT CONQUEROR
//* Lab Section: 021
// * Assignment: Lab Final Project
// * Exercise Description: [optional - include for your own benefit]
// *
// * I acknowledge all content contained herein, excluding template or example
// * code, is my own original work.
// *
// *  Demo Link: https://drive.google.com/file/d/1u_rLmP5nUXY-HwEEr2AvZb6z6dsKXMWZ/view?usp=sharing
//    https://drive.google.com/file/d/1Niaap2sKQjGRSW3e9IFZhQNANrRmxlKP/view?usp=sharing
//
//    Demo#2: https://drive.google.com/file/d/1ZlpfcudxScRiedtSmgaA8Bs-b-qnyizu/view?usp=sharing
//
// *


#include <Servo.h>
int pivot_flag=0;
unsigned long currentMillis = 0;
unsigned long previousMillis = 0;
unsigned long millistimer = 50;//50,500


int pivot_servo_pin = 19;
int left_servo_pin = 18;


Servo pivot_servo;
Servo left_servo;



void setup(){
  Serial.begin(9600);

  pivot_servo.attach(pivot_servo_pin);
  left_servo.attach(left_servo_pin);

  pinMode(pivot_servo_pin,OUTPUT);
  pinMode(left_servo_pin,OUTPUT);

}


int pivot_angle=20;
int left_angle=10;


void loop(){

if(pivot_flag==0){
  pivot_flag=1;
  Pivot_Movement();
}



}

void Pivot_Movement(){
currentMillis = millis();
previousMillis = currentMillis;
while (pivot_angle<60)
{
currentMillis = millis();
if(currentMillis - previousMillis > millistimer) {
  previousMillis = currentMillis;
  pivot_angle=pivot_angle+1;
  pivot_servo.write(pivot_angle);
  left_servo.write(left_angle);
  
}}//end of while

while (left_angle<175){
currentMillis = millis();
if(currentMillis - previousMillis > millistimer) {
  previousMillis = currentMillis;
  left_angle=left_angle+3;
  pivot_servo.write(pivot_angle);
  left_servo.write(left_angle);
  }
}
//end of while


while (pivot_angle>20)
{
currentMillis = millis();
if(currentMillis - previousMillis > millistimer) {
  previousMillis = currentMillis;
  pivot_angle=pivot_angle-1;
  pivot_servo.write(pivot_angle);
  left_servo.write(left_angle);

}
}//end of while


}//end of loop