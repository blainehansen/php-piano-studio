<?php
function body($filename){
	$stuff = file_get_contents("../resources/content/$filename.txt");
	$array = explode("\t", $stuff);

	if (count($array) == 1){
		echo $array[0];
	}
	else {
		$firstline = $array[0];
		echo "<div id='content' class='area'><p class='firstline'>$firstline</p>";

		for ($i = 1; $i < count($array); $i = $i + 1){
			$string = $array[$i];
			if ($string[0] == '#') {
				$string = substr($string, 1, strlen($string) - 1);
				echo "<div class='block'><img src='../resources/pictures/$string.jpg'/></div>";
			} /*
			else if (strpos($string,'#') {
				$split_string = preg_split('/#/', $string, NULL, PREG_SPLIT_NO_EMPTY);
				echo "<div class='block'>$split_string[0]<img src='../resources/pictures/$split_string[1].jpg'/>$split_string[2]</div>";
			}
			*/
			else if ($string[0] == '@')  {
				echo substr($string, 1, strlen($string) - 1);
			}
			else if ($string[0] == '/') {
				continue;
			}
			else {
				echo "<div class='block'><p>$string</p></div>";
			}
		}

		echo "</div>";
	}
}
?>