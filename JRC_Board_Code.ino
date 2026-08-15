#include <SoftwareSerial.h>

SoftwareSerial mySerial(13, 05);
char t;
int enA = 0;
int in1 = 2;
int in2 = 4;

int enB = 15;
int in3 = 17;
int in4 = 16;


void setup() {
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  mySerial.begin(9600);
  Serial.begin(9600);
  
}

void loop() {

    if (mySerial.available()) {
    t = mySerial.read();
    Serial.println(t);
  }



  if (t== 'F'){
  analogWrite(enA, 255);
  analogWrite(enB, 255);

  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);

  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  delay(1000);
}

  if (t== 'R'){
  analogWrite(enA, 255);
  analogWrite(enB, 255);

  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);

  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  delay(1000);
}

  if (t== 'L'){
  analogWrite(enA, 255);
  analogWrite(enB, 255);

  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);

  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  delay(1000);
}

  if(t== 'B'){
  analogWrite(enA, 255);
  analogWrite(enB, 255);

  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);

  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  delay(1000);
}

  if(t== 'S'){
  analogWrite(enA, 255);
  analogWrite(enB, 255);

  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);

  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  delay(1000);
}

 if (t== 'P'){
  
}
}
