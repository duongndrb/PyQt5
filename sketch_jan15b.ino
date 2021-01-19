//khai bao chan led 13
int led = 13;
//bien dung de luu du lieu tu Raspberry Pi
String buff;

void setup() {
  // put your setup code here, to run once:
  // bat cong Serial Baudrate 9600
  Serial.begin(9600);
  // khai bao chan OUTPUT
  pinMode(led,OUTPUT);
}

void loop() {
  //neu co tin hieu tu Pi
  if(Serial.available())
  {
    buff = Serial.readStringUntil('\r');

    // neu du lieu = "Led On"
    if(buff == "Led On")
    {
      // bat HIGH chan led
      digitalWrite(led,HIGH);
      // tra nguoc ve "Turned On"
      Serial.println("Turned On");
    }
    else if(buff == "Led Off")
    {
      // bat LOW chan led
      digitalWrite(led,LOW);
      // tra nguoc ve "Turned Off"
      Serial.println("TUrned Off");
      
    }
    if(buff == "Hello")
    {
      Serial.println("Hi");
    }
    if(buff == "Name")
    {
      Serial.println("Arduino");
    }
    if (buff == "Good Bye")
    {
      Serial.println("Bye Bye");
      //lap vo han de khong nhan lenh
      while (true) {}
    }
  }
}
