if(typeof(struct) == "undefined")
	struct = {}

class structMaps{
	constructor(img, width, height){
		img.maps = this;
		this.img = img;
		this.img.style.position = 'absolute';
		this.img.onmousedown = command.Maps.drag_start;
		this.img.onmousemove = command.Maps.drag_move;
		this.img.onmouseup = command.Maps.drag_stop;
		this.img.onwheel = command.Maps.zoom;
		this.width = width;
		this.height = height;
		this.scale = 1;
		this.positionX = 0;
		this.positionY = 0;
		this.isDrag = false;
		this.dragInit = {};
		this.dragInit.x = 0;
		this.dragInit.y = 0;
		command.Maps.render(this);
	}
}

console.log(structMaps)
