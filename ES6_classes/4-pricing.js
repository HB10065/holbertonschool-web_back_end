import Currency from "./3-currency";

export default class Pricing {
    constructor(amount, Currency) {
        this._amount = amount;
        this._Currency = Currency;
    }

    // getters and setters
    get amount() {
        return this._amount
    }
    set amount(value) {
        this._amount = value
    }

    get Currency() {
        return this._Currency
    }
    set Currency(object) {
        this._Currency = object
    }
    
    // methods
    displayFullPrice() {
        return `${this.amount} ${this.Currency.displayFullCurrency()}`
    }

    static convertPrice(amount, conversionRate) {
        return amount * conversionRate
    }
}
