$(document).ready(function(){
	var position = 0;
	var videos=[
	"http://www.youtube.com/embed/et9Uyv_aXcg",
	"http://www.youtube.com/embed/l9wyJuyWdNg",
	"http://www.youtube.com/embed/0P-JfB6W35I",
	"http://www.youtube.com/embed/aQ5u7DD8nbU"
	];

	$("iframe").attr("src", videos[position]);

	$("#gallery-right").click(function(){
		if (position == videos.length - 1) {
			position = 0;
		}
		else {
			position++;
		}
		$("iframe").attr("src", videos[position]);
	});
	$("#gallery-left").click(function(){
		if (position == 0) {
			position = videos.length - 1;
		}
		else {
			position--;
		}
		$("iframe").attr("src", videos[position]);
	});
});