unsigned long currentTime = 0;
unsigned long lastTime = 0;
const unsigned long intervalBetweenData = 1000;
    
void setup() {
    // make the serial talk faster
    // be sure to also change this in the serial monitor window settings
    pinMode(5, OUTPUT);
    Serial.begin(500000);
    tone(5, 100); //should be digital pin 5, 100 hz; the doc said no pin 3 and 11.
}
        
        
void loop() {
  // get the current time in microseconds
  currentTime =  micros();
  
  if (currentTime - lastTime >= intervalBetweenData ) {
   int sensorValue = analogRead(A0);
   lastTime+=intervalBetweenData;
   
   Serial.print(currentTime/1000);
   Serial.print(',');
   Serial.println(sensorValue);
            
  }
          
         
}
