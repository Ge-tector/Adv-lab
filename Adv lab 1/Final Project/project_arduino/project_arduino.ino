int analogIn = 0;
int hallSensor = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  analogIn = analogRead(A0);
  hallSensor = analogRead(A1);
  Serial.print(millis());
  Serial.print(',');
  Serial.print(hallSensor);
  Serial.print(',');
  Serial.println(analogIn);
}
