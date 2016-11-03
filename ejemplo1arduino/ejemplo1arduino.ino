int incomingByte = 0;   // for incoming serial data

void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
        pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {

        // send data only when you receive data:
        if (Serial.available() > 0) {
                // read the incoming byte:
                incomingByte = Serial.read();
                Serial.println(incomingByte);
                if (incomingByte=='a'){
                  digitalWrite(LED_BUILTIN, HIGH);  
                  }
                  if(incomingByte=='z'){
                    digitalWrite(LED_BUILTIN, LOW);
                    }
                  
                }
}
