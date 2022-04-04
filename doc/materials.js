const MATERIALS = {
	"dummy": {
		strength: 0,
	},
	"metal": {
		strength: 10,
	},
	"iron": {
		type: 'metal',
		strength: 10,
		color: 0xFF,
		vulnerable: ['water'], // deal normal damage?
		resistant: ['fire'], // deal half damage?
		// immune to everything else?
	},
};

class Material {
	constructor(name, volume) {
		this.name = name;
		this.volume = volume;
	}
	
	getName() { return this.name; }
	getStrength() { return MATERIALS[this.name]?.strength ?? MATERIALS[this.getType()]?.strength; ?? MATERIALS['dummy'].strength; }
}
