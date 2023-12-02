-- Datenbank erstellen
CREATE DATABASE IF NOT EXISTS meineDatenbank;

-- Zu der erstellten Datenbank wechseln
USE meineDatenbank;

-- Tabelle erstellen (Beispiel: Benutzer)
CREATE TABLE IF NOT EXISTS Benutzer (
    BenutzerID INT PRIMARY KEY,
    Vorname VARCHAR(50),
    Nachname VARCHAR(50),
    Geburtsdatum DATE
);

-- Beispiel-Datensätze einfügen
INSERT INTO Benutzer (BenutzerID, Vorname, Nachname, Geburtsdatum)
VALUES
    (1, 'Max', 'Mustermann', '1990-01-01'),
    (2, 'Maria', 'Musterfrau', '1985-05-15');
