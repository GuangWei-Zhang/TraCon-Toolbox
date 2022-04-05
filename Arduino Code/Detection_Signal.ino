//#include <TimerOne.h>

char serialData;
int DetectPin = 9;
unsigned long currentMillis = 0;
unsigned long previousMillis = 0;

void setup() {
  pinMode(DetectPin, OUTPUT);
  
  Serial.begin(9600);
  // put your setup code here, to run once:

}

void loop() {
  serialData = Serial.read();
  if (serialData == '1') {
    digitalWrite(DetectPin, HIGH);  
  }
  if (serialData == '0') {
    digitalWrite(DetectPin, LOW);
  }
  }

  
