export default function cleanSet(set, startString) {
    if (typeof startString !== 'string') {
        return ''
    }
    
    newString = ''
    for (const element of [...set]) {
        if (element.startsWith(startString)) {
            if (newString !== '') {
                newString += '-'
            }
            newString += element.slice(startString.length)
        }
        
    }
    return newString
}
