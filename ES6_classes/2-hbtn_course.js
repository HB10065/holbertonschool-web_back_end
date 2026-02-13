export default class HolbertonCourse {
    constructor(name, length, students) {
        this._name = name;
        this._lenght = length;
        this._students = students;
    }
    // getters and setters
    get name() {
        return this._name
    }
    set name(value) {
        this._name = value
    }

    get length() {
        return this._lenght
    }
    set length(value) {
        this._lenght = value
    }

    get students() {
        return this._students
    }
    set students(value) {
        this._students = value
    }
}