package Dron {
    part dron;
    requirement autonomia;
    satisfy autonomia by dron;
    verification pruebaAutonomia {
        objective { verify autonomia; }
    }
}
