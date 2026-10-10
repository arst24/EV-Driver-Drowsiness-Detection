#include <LiquidCrystal.h>

// LCD pins: RS, E, D4, D5, D6, D7
LiquidCrystal lcd(7, 6, 5, 4, 3, 2);

const int PLAY_PIN = 8;
String currentStatus = "";

unsigned long lastWarningTime = 0;
const unsigned long WARNING_INTERVAL = 3000; // Repeat every 3 seconds

void setup() {
  pinMode(PLAY_PIN, OUTPUT);
  digitalWrite(PLAY_PIN, LOW);

  Serial.begin(9600);
  Serial.setTimeout(100);

  lcd.begin(16, 2);
  lcd.print("EV Safety System");
  lcd.setCursor(0, 1);
  lcd.print("System Ready");
}

void loop() {

  // Receive status from Python
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "AWAKE" && currentStatus != "AWAKE") {
      lcd.clear();
      lcd.print("Driver Status:");
      lcd.setCursor(0, 1);
      lcd.print("AWAKE");

      currentStatus = "AWAKE";
      lastWarningTime = 0;
    }

    else if (cmd == "DROWSY" && currentStatus != "DROWSY") {
      lcd.clear();
      lcd.print("WARNING!");
      lcd.setCursor(0, 1);
      lcd.print("DROWSINESS!");

      currentStatus = "DROWSY";
      lastWarningTime = 0; // Trigger warning immediately
    }

    else if (cmd == "NOFACE" && currentStatus != "NOFACE") {
      lcd.clear();
      lcd.print("Face Not Found");

      currentStatus = "NOFACE";
      lastWarningTime = 0;
    }
  }

  // Repeat voice warning every 3 seconds while DROWSY
  if (currentStatus == "DROWSY" &&
      (lastWarningTime == 0 ||
       millis() - lastWarningTime >= WARNING_INTERVAL)) {

    digitalWrite(PLAY_PIN, HIGH);
    delay(300);
    digitalWrite(PLAY_PIN, LOW);

    lastWarningTime = millis();
  }
}