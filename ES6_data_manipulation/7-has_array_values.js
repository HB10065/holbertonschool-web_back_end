export default function hasValuesFromArray(set, array) {
    return [...set].every(element => array.includes(element))
}
