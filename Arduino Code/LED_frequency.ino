//#include <TimerOne.h>


int PowerPin = 9;
int DetectPin = 4;
const int OnDur = 20;
const int OffDur = 30;
unsigned long currentMillis = 0;
unsigned long previousMillis = 0;

void setup() {
  pinMode(PowerPin, OUTPUT);
  pinMode(DetectPin, INPUT);
  // put your setup code here, to run once:

}

void loop() {
  if (digitalRead(DetectPin) == HIGH) {
    digitalWrite(PowerPin, HIGH);
    delay(OnDur);
    digitalWrite(PowerPin,LOW);
    delay(OffDur); 
  }
  if (digitalRead(DetectPin) == HIGH) {
    digitalWrite(PowerPin, LOW);
  }
  
  
  }

  
