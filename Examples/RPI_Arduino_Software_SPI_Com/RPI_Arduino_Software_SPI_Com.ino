/*
  # Demo SPI communication between Raspberry Pi and Arduino

  # GENERAL FUNCTION
  # This is a simple example to demonstrate Software-SPI communication between a Raspberry (Master) with the RPI Level Shifter Hat and Arduino Mega (Slave)

  # WIRING
  # [RPI Level Shifter Hat]         [Arduino]
  # [GPIO; 5V Side]                 [Pin Nr]
  # 26             -->              4     ENABLE RPI Level Shifter Hat
  # 25             -->              21    CLK (Interrupt 2 Pin)
  # 1              <--              15    MISO
  # 2              -->              32    MOSI
  # 21             -->              3     CS (Interrupt 1 Pin)
*/

#define SCK_PIN 21 //Needs to be a Interrupt PIN https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/
#define MISO_PIN 15
#define MOSI_PIN 32
#define SS_PIN 3 //Needs to be a Interrupt PIN

#define DEBUG LOW // Make sure to also set Debug True in the Python script if you set it HIGH here

volatile byte SPI_Byte = 0;
volatile byte SPI_Byte_tmp = 0;
volatile boolean Read_enable = LOW;
volatile int SPI_Counter = 8;
volatile boolean Write_enable = LOW;
volatile byte Write_data = 0xAA; //Massage to send to Raspberry. Fixed value for demo purposes

void setup()
{
  pinMode(SCK_PIN, INPUT);
  pinMode(MOSI_PIN, INPUT);
  pinMode(MISO_PIN, OUTPUT);
  pinMode(SS_PIN, INPUT);

  Serial.begin(115200);
  Serial.println("SPI slave mode");
  attachInterrupt(digitalPinToInterrupt(SS_PIN), SPI_slave_in, RISING); // RISING or FALLING
  attachInterrupt(digitalPinToInterrupt(SCK_PIN), SPI_transfer_bit, RISING);
}

void loop()
{

  if (SPI_Byte == 0x55)
  { //Check for Write Instruction
    Write_enable = HIGH;
    Read_enable = LOW;
    SPI_Byte = 0;
    if (DEBUG)
      Serial.println("Writing data");
  }
}

void SPI_slave_in()
{
  Read_enable = HIGH;
  Write_enable = LOW;
  //Serial.println("CS Active");
}

void SPI_transfer_bit()
{
  //
  // read SPI
  //
  if (Read_enable)
  {
    if (digitalRead(MOSI_PIN) == 1)
    {
      SPI_Byte_tmp = (SPI_Byte_tmp << 1) | 0x01; //Set "1"
      if (DEBUG)
        Serial.println("Read 1");
    }

    else
    {
      SPI_Byte_tmp = (SPI_Byte_tmp << 1) & 0xFE; //Set "0"
      if (DEBUG)
        Serial.println("Read 0");
    }

    SPI_Counter--;

    if (SPI_Counter <= 0)
    {
      Read_enable = LOW;
      SPI_Byte = SPI_Byte_tmp;
      Serial.println("Read data:");
      Serial.println(SPI_Byte, BIN);
      SPI_Byte_tmp = 0;
      SPI_Counter = 8;
    }
  }

  //
  // write SPI
  //
  if (Write_enable)
  {
    digitalWrite(MISO_PIN, bitRead(int(Write_data), SPI_Counter - 1));
    if (DEBUG)
      Serial.print("Write ");
    if (DEBUG)
      Serial.println(bitRead(int(Write_data), SPI_Counter - 1));

    SPI_Counter--;

    if (SPI_Counter <= 0)
    {
      Write_enable = LOW;
      Serial.println("Write Data:");
      Serial.println(Write_data, BIN);
      SPI_Counter = 8;
    }
  }
}
