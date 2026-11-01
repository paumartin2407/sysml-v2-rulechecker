package EnsayoDron {
    import ModeloDron::*;
    satisfy autonomia by dron;
    verification pruebaAutonomia { objective { verify autonomia; } }
}
