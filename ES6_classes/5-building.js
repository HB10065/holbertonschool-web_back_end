export default class Building {
    constructor(sqft) {
        this._sqft = sqft;
    }

    // getters and setters
    get sqft() {
        return this._sqft;
    }
    set sqft(value) {
        this._sqft = value
    }

    //methods
    evacuationWarningMessage() {
        throw new Error('Class extending Building must override evacuationWarningMessage')
    }
}
