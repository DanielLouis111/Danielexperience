#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
Servo feederServo;

const int xPin = A0;       // Joystick X-axis
const int buttonPin = A2;  // Joystick Button
const int servoPin = D9;   // Servo Signal

unsigned long lastFeedTime = 0;
int feedInterval = 10; // in seconds
const int minInterval = 5;
const int maxInterval = 60;
bool buttonPressed = false;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT_PULLUP);

  lcd.init();
  lcd.backlight();

  feederServo.attach(servoPin);
  feederServo.write(90); // Start at 90
  delay(500);

  lcd.setCursor(0, 0);
  lcd.print("Feeder Ready!");
  delay(1500);
  lcd.clear();
}

void loop() {
  int xVal = analogRead(xPin);
  int btnVal = digitalRead(buttonPin);

  Serial.print("Joystick X: ");
  Serial.print(xVal);
  Serial.print(" | Interval: ");
  Serial.print(feedInterval);
  Serial.print(" | Button: ");
  Serial.println(btnVal);

  // --- Joystick: adjust interval ---
  if (xVal < 1500) {
    feedInterval = constrain(feedInterval - 1, minInterval, maxInterval);
    Serial.println("Decreased interval");
    delay(300); // debounce
  } else if (xVal > 2500) {
    feedInterval = constrain(feedInterval + 1, minInterval, maxInterval);
    Serial.println("Increased interval");
    delay(300); // debounce
  }

  // --- Manual Feed ---
  if (btnVal == LOW && !buttonPressed) {
    buttonPressed = true;
    Serial.println("Manual Feed Triggered");
    dispenseFood();
    lastFeedTime = millis(); // reset timer
  }
  if (btnVal == HIGH) {
    buttonPressed = false;
  }

  // --- Auto Feed ---
  if (millis() - lastFeedTime >= feedInterval * 1000UL) {
    Serial.println("Auto Feed Triggered");
    dispenseFood();
    lastFeedTime = millis();
  }

  // --- LCD Display ---
  lcd.setCursor(0, 0);
  lcd.print("Interval: ");
  lcd.print(feedInterval);
  lcd.print("s    ");

  lcd.setCursor(0, 1);
  int remaining = (feedInterval * 1000 - (millis() - lastFeedTime)) / 1000;
  lcd.print("Next in: ");
  lcd.print(remaining > 0 ? remaining : 0);
  lcd.print("s   ");
}

void dispenseFood() {
  lcd.setCursor(0, 1);
  lcd.print("Dispensing...     ");

  feederServo.write(90);  // Start at 90
  delay(300);
  feederServo.write(0);   // Drop to 0
  delay(2000);
  feederServo.write(90);  // Return to 90
  delay(300);

  lcd.setCursor(0, 1);
  lcd.print("Done.             ");
}
