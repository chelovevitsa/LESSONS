CREATE DATABASE baza;
USE baza;

CREATE TABLE lokale (
    id INTEGER USIGNED AUTO_INCREMENT PRIMARY KEY,
    nazwa TEXT NOT NULL,
    miaso TEXT NOT NULL,
    ulica TEXT NOT NULL,
    numer INTEGER NOT NULL
);
CREATE TABLE dania (
    id INTEGER USIGNED AUTO_INCREMENT PRIMARY KEY,
    typ INTEGER NOT NULL,
    nazwa TEXT NOT NULL,
    cena INTEGER NOT NULL
);
CREATE TABLE rezerwacje (
    id INTEGER PRIMARY KEY,
    nr_stolika INTEGER,
    data_rez DATE NOT NULL,
    liczba_osob INTEGER NOT NULL,
    telefon TEXT NOT NULL
);
CREATE TABLE pracownicy (
    id INTEGER PRIMARY KEY,
    imie TEXT NOT NULL,
    nazwisko TEXT NOT NULL,
    stanowisko INTEGER NOT NULL
);