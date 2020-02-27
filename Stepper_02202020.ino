
const int switch1 = 6; //clockwise
const int switch2 = 11; // counter-clockwise
const int direct = 10;
const int stepPin = 3;
int switchState1 = 0;
int switchState2 = 0;


void setup() {
Serial.begin(9600);
pinMode(switch1, INPUT);
pinMode(switch2, INPUT);
pinMode(direct, OUTPUT);
pinMode(stepPin, OUTPUT);

}

void loop() {

  switchState1 = digitalRead(switch1);
  switchState2 = digitalRead(switch2);
  analogWrite(stepPin,100 );
  analogWrite(direct, 100);
  //delay(20);

  
  
/*if (switchState1 == HIGH) {
  //for (int n = 0; n < steps; n++) 
  digitalWrite(stepPin, HIGH);
  digitalWrite(direct, HIGH);
  Serial.println("IM THE FIRST SWITCH");
  delay(20);

  }
if (switchState2 == HIGH) {
  digitalWrite(stepPin, HIGH);
  digitalWrite(direct, LOW);
  Serial.println("I AM THE SECOND SWITCH");
  delay(20);
}
else
{*/
  Serial.println("Turn me back on!");
  delay(20);

//}
}
