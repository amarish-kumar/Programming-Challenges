<?php
$f = fopen ("php://stdin", "r");

$mealCost = fgets ($f);
$tipPercent = fgets ($f);
$taxPercent = fgets ($f);

$tip = $mealCost * ($tipPercent / 100);
$tax = $mealCost * ($taxPercent / 100);
$totalCost = $mealCost + $tip + $tax;
$totalCost = round ($totalCost);

printf ("The total meal cost is %d dollars.", $totalCost);
?>