if(typeof(command) == "undefined")
	command = {}

command.Maps = {}

command.Maps.drag_start = function(e){
	e.preventDefault();
	var maps = e.toElement.maps;
	maps.isDrag = true;
	maps.dragInit.x = e.clientX - maps.positionX;
	maps.dragInit.y = e.clientY - maps.positionY;
}

command.Maps.drag_move = function(e){
	e.preventDefault();
	var maps = e.toElement.maps;
	if(maps.isDrag == false)
		return;
	maps.positionX = e.clientX - maps.dragInit.x;
	maps.positionY = e.clientY - maps.dragInit.y;
	maps.img.style.left = maps.positionX + 'px';
	maps.img.style.top = maps.positionY + 'px';
}

command.Maps.drag_stop = function(e){
	e.preventDefault();
	var maps = e.toElement.maps;
	maps.isDrag = false;
}
