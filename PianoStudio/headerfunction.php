<?php
function doheader($pagename){
	$host  = $_SERVER['HTTP_HOST'];
	$uri   = rtrim(dirname($_SERVER['PHP_SELF']), '/\\');
	$extra = $pagename;
	header("Location: http://$host$uri/$extra");
	exit;
}
?>