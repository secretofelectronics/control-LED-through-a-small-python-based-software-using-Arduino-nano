int ledPin = 13; // Pin connected to the LED
String command = ""; 

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600); // Start serial communication
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read(); 
    if (c == '\n') { // End of command
      if (command == "ON") {
        digitalWrite(ledPin, HIGH); // Turn LED on
      } else if (command == "OFF") {
        digitalWrite(ledPin, LOW); // Turn LED off
      }
      command = ""; // Reset command
    } else {
      command += c; // Build the command
    }
  }
}
