import Currency from "./3-currency";

export default class Pricing {
    constructor(amount, Currency) {
        this._amount = amount;
        this._currency = Currency;
    }

    // getters and setters
    get amount() {
        return this._amount
    }
    set amount(value) {
        this._amount = value
    }

    get currency() {
        return this._currency
    }
    set currency(object) {
        this._currency = object
    }
    
    // methods
    displayFullPrice() {
        return `${this.amount} ` + this.currency.displayFullCurrency();
    }

    static convertPrice(amount, conversionRate) {
        return amount * conversionRate;
    }
}
