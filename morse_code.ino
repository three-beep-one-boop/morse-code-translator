const int sound_sensor = A2; 
const int activation_led_pin = 9;
const int msg_led_pin = 6;
const int threshold_volume = 100;
const int button_pin = 8; 

int t = 0;
bool first_run = true;
bool listening_mode = false;

bool hear_sound = false;

bool playing_beep = false;
bool playing_space = false;

bool listen_for_sound() {
  int sound_value = 0;
    
  for (int i = 0; i < 32; i++) { 
    sound_value += analogRead(sound_sensor);  
  
  }
 
  sound_value >>= 5; //bitshift operation 
 
  if (sound_value > threshold_volume) { 
//    Serial.println("Loud sound");
    digitalWrite(msg_led_pin, HIGH);
    return true;
    }
  else {
    return false;
  }
//  Serial.print("Sound value: ");
//  Serial.println(sound_value);
}

void listening_mode_control() {
    if (digitalRead(button_pin) == HIGH) {
    Serial.println("Button pressed.");

    // Turn on listening-mode
    if (listening_mode == false) {
      listening_mode = true;
      delay(1000);
      digitalWrite(activation_led_pin, HIGH);
      Serial.println("Listening Mode ON");
    }
    
    // Turn off listening-mode
    else {
      listening_mode = false;
      Serial.println("Listening mode OFF");
      digitalWrite(activation_led_pin, LOW);
      delay(1000);
      
    }
//    Serial.println(listening_mode);
  }
}

 
void setup() {
  Serial.begin(9600); //begin Serial Communication
  Serial.setTimeout(1); 

  pinMode(msg_led_pin, OUTPUT);
  pinMode(activation_led_pin, OUTPUT);
  pinMode(button_pin, INPUT);

  // Set initial state to LOW
  digitalWrite(msg_led_pin, LOW); 
  digitalWrite(activation_led_pin, LOW); 
  
}

// REMEMBER TO RESET ARRAY SIZE
void loop() {
  digitalWrite(msg_led_pin, LOW);

  // Mimics a switch
  listening_mode_control();

  t = 0;  
  first_run = true;
  
  playing_beep = false;
  playing_space = false;

  while (listening_mode == true) {
    digitalWrite(msg_led_pin, LOW);
    listening_mode_control();
    hear_sound = listen_for_sound();

    // Playing beep for the first time. Initiating the timer.
    if (hear_sound == true && first_run == true && playing_beep == false && playing_space == false) {
      first_run = false;
      playing_beep = true;
      t = 0;
    }

    // We are tracking the length of the space but it stops
    else if (hear_sound == true && first_run == false && playing_space == true) {
      playing_space = false;
      first_run = true;
      Serial.print("Length of space: ");
      Serial.println(t);
      t = 0;
    }
    
    // Playing space for the first time. Initiating the timer.
    else if (hear_sound == false && first_run == true && playing_beep == false && playing_space == false) {
      first_run = false;
      playing_space = true;
      t = 0;
    }

    // We are tracking the length of the beep but it stops
    else if (hear_sound == false && first_run == false && playing_beep == true) {
      playing_beep = false;
      first_run = true;
      Serial.print("Length of beep: ");
      Serial.println(t);
      t = 0;
    }
    // increment time
    t++; 
    delay(25); /

  }
    Serial.print("Idle...\n");
  delay(200); 
  
}


  
