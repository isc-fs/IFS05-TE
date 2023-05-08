#include <SPI.h>
#include "mcp_can.h"

// Define the CAN bus pins
#define CAN_CS_PIN 8
MCP_CAN CAN(CAN_CS_PIN); // Set CS pin for MCP2515 module

// Define the CAN message IDs
#define I_ACUM_ID 0x100
#define DC_BUS_ID 0x101
#define THROTTLE_ID 0x102
#define BRAKE_ID 0x103
#define TIMESTAMP_ID 0x104

// Define the CAN message lengths
#define I_ACUM_LEN 2
#define DC_BUS_LEN 2
#define THROTTLE_LEN 1
#define BRAKE_LEN 1
#define TIMESTAMP_LEN 4

#define CAN_KBPS CAN_250KBPS

// Define the variables to send
int I_Acum = 0;
int DC_bus = 0;
int Throttle = 0;
int Brake = 0;
unsigned long timestamp = 0;

void setup() 
{
  Serial.begin(115200);

  // Inicialización del CAN de Telemetría
  if (CAN.begin(MCP_ANY,CAN_KBPS,MCP_20MHZ) == CAN_OK) {
    Serial.println("CAN: Inicializacion correcta!");
    CAN.setMode(MCP_NORMAL);
  } else {
    Serial.println("CAN: Fallo al incializar, reinicie por favor");
    while(1);
  }

}

void loop() {
  // Update the variables to send
  I_Acum = random(0, 2000); // Generate random value for I_Acum (0-2000 mA)
  DC_bus = random(0, 500); // Generate random value for DC_bus (0-500 V)
  Throttle = random(0, 101); // Generate random value for Throttle (0-100%)
  Brake = random(0, 101); // Generate random value for Brake (0-100%)
  timestamp = millis(); // Get current timestamp in milliseconds

  // Create the CAN messages
  byte I_Acum_data[I_ACUM_LEN] = {highByte(I_Acum), lowByte(I_Acum)};
  byte DC_bus_data[DC_BUS_LEN] = {highByte(DC_bus), lowByte(DC_bus)};
  byte Throttle_data[THROTTLE_LEN] = {Throttle};
  byte Brake_data[BRAKE_LEN] = {Brake};
  byte timestamp_data[TIMESTAMP_LEN] = {byte(timestamp >> 24), byte(timestamp >> 16), byte(timestamp >> 8), byte(timestamp)};

  // Send the CAN messages
  CAN.sendMsgBuf(I_ACUM_ID, 0, I_ACUM_LEN, I_Acum_data);
  CAN.sendMsgBuf(DC_BUS_ID, 0, DC_BUS_LEN, DC_bus_data);
  CAN.sendMsgBuf(THROTTLE_ID, 0, THROTTLE_LEN, Throttle_data);
  CAN.sendMsgBuf(BRAKE_ID, 0, BRAKE_LEN, Brake_data);
  CAN.sendMsgBuf(TIMESTAMP_ID, 0, TIMESTAMP_LEN, timestamp_data);

  // Print the variables for debugging
  Serial.print("I_Acum: ");
  Serial.println(I_Acum);
  Serial.print("DC_bus: ");
  Serial.println(DC_bus);
  Serial.print("Throttle: ");
  Serial.println(Throttle);
  Serial.print("Brake: ");
  Serial.println(Brake);
  Serial.print("Timestamp: ");
  Serial.println(timestamp);

  delay(1000); // Delay
}
