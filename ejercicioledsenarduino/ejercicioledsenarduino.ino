void setup() {
Serial.begin(9600);
pinMode(4,OUTPUT);
pinMode(5,OUTPUT);
pinMode(6,OUTPUT);
pinMode(7,OUTPUT);
pinMode(8,OUTPUT);
}

void loop() {
int val=analogRead(analog_pin);
digitalWrite(4,LOW);
digitalWrite(5,LOW);
digitalWrite(6,LOW);
digitalWrite(7,LOW);
digitalWrite(8,LOW);
unsigned char c= (unsigned char)(((float)analogRead(0)/850.0)*255.0);
Serial.println((unsigned int)c);
if(c>50{
  digitalWrite(4,HIGH);
  if(c>100){
  digitalWrite(5,HIGH);
  if(c>150){
    digitalWrite(6,HIGH);
    if(c>200){
      digitalWrite(7,HIGH);
      if(c>250){
        digitalWrite(8,HIGH);
      }
    }
  }
  }
}
delay(250);
}
      }
    }
  }
}
}
