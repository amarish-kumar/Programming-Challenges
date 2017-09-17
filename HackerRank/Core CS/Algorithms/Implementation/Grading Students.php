<?php
$handle = fopen ("php://stdin", "r");
fscanf ($handle, "%d", $n);

$grades = array();
for($i = 0; $i < $n; $i++){
    fscanf ($handle, "%d", $grade);

    $remainder = $grade % 5;

    if ($remainder == 0 || $grade < 38) {
        $grades[] = $grade;
    } else {
        if ($remainder >= 3) {
            $grades[] = $grade - $remainder + 5;
        } else {
            $grades[] = $grade;
        }
    }
}

echo implode("\n", $grades)."\n";
