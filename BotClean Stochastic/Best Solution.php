<?php
/* Head ends here */
function next_move(&$posx, &$posy, &$board,$first) {
    //your logic here

    
    for($i=0;$i<5;$i++){
        for($j=0;$j<5;$j++){
            if($board[$i][$j]=='d'){
                $board[$i][$j]='-';
                $currentmove=abs($i-$posx)+abs($j-$posy)+next_move($i, $j, $board,false);
                $board[$i][$j]='d';
                if(!isset($minmove)||$currentmove<$minmove){
                    $minmove=$currentmove;
                    $x=$i;
                    $y=$j;
                }
            }
        }
    }
    if($first){

        switch(true){
            case $x>$posx:
                echo "DOWN";
            break;
            case $x<$posx:
                echo "UP";
            break;
            case $y<$posy:
                echo "LEFT";
            break;
            case $y>$posy:
                echo "RIGHT";
            break;
        }
    }
    
    return $minmove;
}

/* Tail starts here */
$fp = fopen("php://stdin", "r");

$temp = fgets($fp);              //moves made by the second player
$position = split(' ',$temp);

$board = array();

for ($i=0;$i<5;$i++) {
    fscanf($fp, "%s", $tmp);
    $board[$i]=str_split($tmp);
}
$position[0]=(int)$position[0];
$position[1]=(int)$position[1];
if($board[$position[0]][$position[1]]=='d'){
echo "CLEAN";
} else {
    next_move($position[0], $position[1], $board,true);
}
?>
