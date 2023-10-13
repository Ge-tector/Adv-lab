/* LED BRIGHTNESS CONTROL */

// our potentiometer will go to Analog Input 1
const int PotInputPin = A1;

// our digital PWN output is set to Digital Out 9
const int outPin = 9;

// we start with an output of 0 and declare this variable as an integer
int outputLevel=0;
    
void setup() {
    //define the pin mode for the digital output
    pinMode(outPin, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    int sensorValue = analogRead(A0);
    int potValue = analogRead(A1);

    // use the map() function to scale the potentiometer input from 0-1023 to 0-255
    outputLevel = map(potValue,0,1023,0,255);

    // write the outputLevel variable to our digital output pin
    analogWrite(outPin, outputLevel);

    Serial.print(millis());
    Serial.print(',');
    Serial.print(sensorValue);
    Serial.print(',');
    Serial.println(potValue);
    delay(200);
}
