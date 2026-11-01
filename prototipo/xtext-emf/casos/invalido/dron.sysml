package Dron {
    part dron;
    requirement autonomia;
    satisfy autonomia by dronInexistente;
    verification pruebaAutonomia { objective { verify autonomia; } }
}
