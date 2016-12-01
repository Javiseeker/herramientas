int dato=0;
void setup() {
Serial.begin(9600);
pinMode(13,OUTPUT);

}

void loop() {
dato=Serial.read();
Serial.write(dato);
if(dato=='a'){
  digitalWrite(13,HIGH);
}
else if(dato=='<'){
  digitalWrite(13,LOW);
}
}
}
