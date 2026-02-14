export default class Airport {
    constructor(name, code) {
        this._name = name;
        this._code = code;
    }

    // methods
    toString() {
        return `[Airport ${this._code}]`
    }
}
