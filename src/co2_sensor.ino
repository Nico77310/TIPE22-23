// Programme Arduino pour lire la concentration de CO2 en ppm à partir du capteur MQ135

// Déclaration des constantes
const int mq135Pin = A0; // Broche analogique utilisée pour le cpateur MQ135

// Déclaration des variables
float ppm = 0.0; // Stocke la concentration de CO2 en ppm

void setup() {
  // Démarre la communication série
  Serial.begin(9600);
}

void loop() {
    // Lit la valeur analogique du capteur MQ135
    int sensorValue = analogRead(mq135Pin);

    // Convertion de la valeur analogique en concentration de CO2 en ppm
    ppm = convertToPpm(sensorValue);

    // Affiche la concentration de CO2 en ppm sur le moniteur série
    Serial.print("Concentration de CO2 (ppm): ");
    Serial.println(ppm);

    delay(1000); // Attente de 1 seconde
}

// Fonction de conversion de la valeur analogique en concentration de CO2 en ppm
float convertToPPM(int sensorValue) {
    // Formule de conversion spécifique au capteur MQ135

    float voltage = sensorValue * (5.0 / 1023.0); // Conversion de la valeur analogique en tension
    float ppm = 500 * (voltage / 5.0); // Calcule la concentraton de CO2 en ppm

    return ppm; // Retourne la concentration de CO2 en ppm
}