//with help from https://www.arduino.cc/en/Tutorial/BuiltInExamples/Smoothing

    // These constants won't change:
    const int numReadings = 10;          // How many points to average over?
    const int PhotoResAnalogPin = A0;    // pin that the sensor is attached to
    //these do change
    
    int readings[numReadings];      // this makes the array to stare the data
    int readIndex = 0;              // the index of the current reading
    int total = 0;                  // the running total
    int average = 0;                // the average
    
    int inputPin = A0;
    
    void setup() {
    
      // initialize serial communications:
      // this is not very time sensitive so we can be slow
      Serial.begin(9600);
      
      // put zeros in the array called readings
      for (int thisReading = 0; thisReading < numReadings; thisReading++) {
        readings[thisReading] = 0;
      }
    }
    
    void loop() {
    
      // remove the oldest data point from the array
      total = total - readings[readIndex];
        
      // read from the sensor:
      readings[readIndex] = analogRead(PhotoResAnalogPin);
      // add the reading to the total:
      total = total + readings[readIndex];
      // advance to the next position in the array:
      readIndex = readIndex + 1;
    
      // if we're at the end of the array...
      if (readIndex >= numReadings) {
        // ...wrap around to the beginning:
        readIndex = 0;
      }
    
      // calculate the average:
      average = total / numReadings;
      // report the value over Serial
      Serial.print(millis());
      Serial.print(',');
      Serial.println(average);
      delay(100);        // delay in between readings
    }
