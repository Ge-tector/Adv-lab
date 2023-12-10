int analogIn = 0;
int hallSensor = 0;
unsigned long currentTime = 0;
unsigned long lastTime = 0;
const unsigned long intervalBetweenData = 1000;

void setup() {
  // 500k baud
  Serial.begin(500000);
}

void loop() {
  // lab 4 coding adapted into this project
  currentTime =  micros();
          
  if (currentTime - lastTime >= intervalBetweenData) {
    lastTime+=intervalBetweenData;
    analogIn = analogRead(A0);
    hallSensor = analogRead(A1);
    
    Serial.print(currentTime/1000);
    Serial.print(',');
    Serial.print(hallSensor);
    Serial.print(',');
    Serial.println(analogIn);
  }
}
