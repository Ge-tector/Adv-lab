/**** Simple Photo-Gate

  Use analogRead to measure light on a photoresistor

  revision history:
  09/22/2015 Mark D. Shattuck <mds> VMon.ino
             Lab 2 part II for P371
             000 mds Starting point for assignment 2-II
  12/22/2020 000 mds convert to SimpleGate

  Therory of opperation:

  Use an LED and a photoresitor as a light gate.  When an object is between
  the gate the light is lowered and can be measured with the photo resistor.
  Circut:

  P9--R1--LED--GND

       [object in light gate]

  5V------Rp-+-R2--GND
           |
           A0

  R1=0.1K
  R2=1K

**************/

int pinIn = A0;  // input pin
int pinOut = 9;  // output pin
int del = 1000;  // Delay between measurements
int output = 0;  // variable to store the value coming from pinIn

char outstr[100]; // store output string

void setup() {
  Serial.begin(115200);           // Set up Serial library at 115200 bps
  pinMode(pinOut, OUTPUT);        // Initialize pin pinOut as an output.
  digitalWrite(pinOut, HIGH);     // Turn on pinOut
}

void loop() {
  output = analogRead(pinIn);                 // read voltage 10-bit 0 - 2^10-1=1023
  float V1 = (5.0 * (float)output) / 1024;    // convert to Volts
  sprintf(outstr, "Counts =%4d => ", output); // Arduino sprintf cant use floats
  Serial.write(outstr);                       // Print to serial monitor 
  Serial.print(V1, 3);
  Serial.println("V");
  delay(del);                                 // wait
}
