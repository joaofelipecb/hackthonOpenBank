if(typeof(command) == "undefined")
	command = {}

command.Maps = {}

command.Maps.drag_start = function(e){
	e.preventDefault();
	var maps = e.toElement.maps;
	maps.isDrag = true;
	maps.dragInit.x = e.clientX - maps.positionX;
	maps.dragInit.y = e.clientY - maps.positionY;
	command.Maps.render(maps);
}

command.Maps.drag_move = function(e){
	e.preventDefault();
	var maps = e.toElement.maps;
	if(maps.isDrag == false)
		return;
	maps.positionX = e.clientX - maps.dragInit.x;
	maps.positionY = e.clientY - maps.dragInit.y;
	command.Maps.render(maps);
}

command.Maps.drag_stop = function(e){
	e.preventDefault();
	var maps = e.toElement.maps;
	maps.isDrag = false;
}

command.Maps.zoom = function(e){
	e.preventDefault();
	var maps = e.toElement.maps;
	var zoomFactor = e.wheelDeltaY*0.0005*maps.scale;
	maps.scale = maps.scale + zoomFactor;
	if(zoomFactor>0){
		maps.positionX = maps.positionX - (maps.width*zoomFactor*(e.screenX/window.innerWidth));
		maps.positionY = maps.positionY - (maps.height*zoomFactor*(e.screenY/window.innerHeight));
	}
	else{
		maps.positionX = maps.positionX - (maps.width*zoomFactor*(e.screenX/window.innerWidth));
		maps.positionY = maps.positionY - (maps.height*zoomFactor*(e.screenY/window.innerHeight));
	}
	command.Maps.render(maps);
	console.log(e);
}

command.Maps.render = function(maps){
	maps.img.style.left = maps.positionX + 'px';
	maps.img.style.top = maps.positionY + 'px';
	maps.img.style.width = (maps.width*maps.scale) + 'px';
	maps.img.style.height = (maps.height*maps.scale) + 'px';
}
