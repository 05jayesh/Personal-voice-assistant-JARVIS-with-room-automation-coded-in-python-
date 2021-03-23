char x;
int incoming[2];
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(10, OUTPUT);
pinMode(11, OUTPUT);
pinMode(12, OUTPUT);
digitalWrite(10,HIGH);
digitalWrite(11,HIGH);
digitalWrite(12,HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
if (Serial.available()>=1)
{
  incoming[0]=Serial.read();
  //Serial.write(x);
  //Serial.println("pin");
  x=incoming[0];
  Serial.println(x);
  switch(x)
  {
      case 'a':
      digitalWrite(10,LOW);
      digitalWrite(11,LOW);
      Serial.println("pin 1");
      break;
      case 'b':
      digitalWrite(10,HIGH);
      digitalWrite(11,HIGH);
      Serial.println("pin 2");
      break;
      case 'c':
      digitalWrite(12,LOW);
      Serial.println("pin 3");
      break;
      case 'd':
      digitalWrite(12,HIGH);
      Serial.println("pin 4");
      break;
  }
  }
}

