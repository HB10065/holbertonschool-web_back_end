import Building from "./5-building";

export default class SkyHighBuilding extends Building {
    constructor(sqft, floors) {
        super(sqft);
        this._floors = floors;
    }

    // getters and setters
    get floors() {
        return this._floors
    }
    set floors(value) {
        this._floors = value
    }

    // methods
    evacuationWarningMessage() {
        return `Evacuate slowly the ${this.floors} floors`
    }
}
