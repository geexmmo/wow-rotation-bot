#include "Keyboard.h"
char altKey = KEY_LEFT_ALT;
char shiftKey = KEY_LEFT_SHIFT;
char ctrlKey = KEY_LEFT_CTRL;

void setup() {

  // open the serial port:
  Serial.begin(9600);
  Serial.setTimeout(10);

  // initialize control over the keyboard:

  Keyboard.begin();
}

void loop() {

  // check for incoming serial data:
  if (Serial.available() > 0) {
    // read incoming serial data:
    String inString = Serial.readString();
    // inString.toLowerCase();2
    // inString.trim(); // shouldnt be used but mistakes could be made with my bad usb cable
    // delay(3000);
    if (inString.length() > 1) { // if input contains modifier - it is going to be parsed
      String inMod = inString.substring(0, 3); // getting first 3 chars
      char inKey = inString.charAt(inString.length() - 1); // getting last char from input
      if (inMod == "alt") { // KEY_LEFT_ALT
        Keyboard.press(altKey);
      } else if (inMod == "sft") { // KEY_LEFT_SHIFT
        Keyboard.press(shiftKey);
      } else if (inMod == "ctl") { // KEY_LEFT_CTRL
        Keyboard.press(ctrlKey);
      }
      delay(random(20, 30));
      Keyboard.press(inKey);
      delay(random(15, 20));
      Keyboard.release(inKey);
    } else { // if input does not contain modifier - it is going to be send as is
      Keyboard.press(inString[0]);
      delay(random(15, 25));
      Keyboard.release(inString[0]);
    }
    Keyboard.releaseAll();
  }
}
