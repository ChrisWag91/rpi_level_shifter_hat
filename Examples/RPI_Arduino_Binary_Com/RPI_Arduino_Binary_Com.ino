//# Demo binary communication between Raspberry Pi and Arduino
//# 4 bit Raspberry --> Arduino
//# 4 bit Arduino --> Raspberry

//# General Cycle
//# 1.    [Raspberry] Enable GPIO 26                              [Arduino] Start test signal
//# 2.    [Raspberry] Read IN bits                                [Arduino] Write OUT bits
//# 3.    [Raspberry] Write OUT bits                              [Arduino] Read IN bits
//# 4.    [Raspberry] Print IN bits                               [Arduino] Serial print IN bits

//# WIRING
//#
//# [RPI Level Shifter Hat]         [Arduino]
//# [GPIO; 5V Side]                 [Pin Nr]
//# 26             -->              4     ENABLE
//# 0              -->              14
//# 1              -->              15
//# 2              -->              32
//# 3              -->              34

//# 4              <--              36
//# 5              <--              12
//# 6              <--              10
//# 7              <--              17

#define BAUD (115200)
#define TESTDELAY 1000

//[RPI GPIO Nr] = [Arduino Pin]
int testPin0 = 14;
int testPin1 = 15;
int testPin2 = 32;
int testPin3 = 34;

int testPin4 = 36;
int testPin5 = 12;
int testPin6 = 10;
int testPin7 = 17;

int enablePin = 4; // Enable pin; start signal

// initial OUT values
bool outPin4 = 1;
bool outPin5 = 0;
bool outPin6 = 1;
bool outPin7 = 0;

int ledPin = 13; // select the pin for the LED

void setup()
{
  Serial.begin(BAUD);

  // Set IO Modes
  pinMode(testPin0, INPUT);
  pinMode(testPin1, INPUT);
  pinMode(testPin2, INPUT);
  pinMode(testPin3, INPUT);

  pinMode(enablePin, INPUT);

  pinMode(testPin4, OUTPUT);
  pinMode(testPin5, OUTPUT);
  pinMode(testPin6, OUTPUT);
  pinMode(testPin7, OUTPUT);

  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);

  Serial.println("");
  Serial.println("Initialized");

  //STEP 1
  //Waiting for start signal
  Serial.println("");
  Serial.println("Waiting for start signal from RPI (GPIO 26 High)");

  while (not digitalRead(enablePin))
  {
    delay(TESTDELAY);
  }
  Serial.println("start communication...");
}

void loop()
{
  while (digitalRead(enablePin))
  {

    //STEP 2
    //Write OUT bits
    //Alternating values for test purposes
    Serial.println("");
    Serial.println("Writing OUT pins");
    Serial.println(outPin4);
    Serial.println(outPin5);
    Serial.println(outPin6);
    Serial.println(outPin7);

    digitalWrite(testPin4, outPin4);
    digitalWrite(testPin5, outPin5);
    digitalWrite(testPin6, outPin6);
    digitalWrite(testPin7, outPin7);

    digitalWrite(ledPin, outPin7); // just for visualisation

    //Invert OUT bits for next cycle
    outPin4 = not outPin4;
    outPin5 = not outPin5;
    outPin6 = not outPin6;
    outPin7 = not outPin7;

    //STEP 3 and 4
    //Read IN bits
    Serial.println("");
    Serial.println("Read IN pins");
    Serial.println(digitalRead(testPin0));
    Serial.println(digitalRead(testPin1));
    Serial.println(digitalRead(testPin2));
    Serial.println(digitalRead(testPin3));
    Serial.println("");
    Serial.println("---- Cycle complete ----");
    Serial.println("");

    delay(TESTDELAY);
  }
}
