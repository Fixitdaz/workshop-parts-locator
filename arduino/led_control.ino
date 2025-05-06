const int ledPins[] = {2, 3, 4, 5};
void setup() {
  Serial.begin(9600);
  for(int i=0;i<4;i++) {
    pinMode(ledPins[i],OUTPUT);
    digitalWrite(ledPins[i],LOW);
  }
}
void loop() {
  if(Serial.available()) {
    int bin = Serial.parseInt();
    if(bin>=0 && bin<4) {
      digitalWrite(ledPins[bin],HIGH);
      delay(3000);
      digitalWrite(ledPins[bin],LOW);
    }
  }
}
