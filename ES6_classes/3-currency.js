export default class Currency {
    constructor(code, name) {
        this._code = code;
        this._name = name;
    }

    // getters and setters
    get code() {
        return this._code
    }
    set code(value) {
        if (typeof value === 'string') {
            this._code = value
        }
    }

    get name() {
        return this._name
    }
    set name(value) {
        if (typeof value === 'string') {
            this._name = value
        }
    }

    // methods
    displayFullCurrency() {
        return `${this.name} (${this.code})`
    }
}
