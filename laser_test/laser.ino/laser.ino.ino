#define L1 8
#define L2 9

void setup() {
  pinMode(L1, OUTPUT);
  pinMode(L2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(L1, HIGH);
  delay(500);
  digitalWrite(L1, LOW);
  delay(500);
}
