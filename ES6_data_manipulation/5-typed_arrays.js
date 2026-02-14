export default function createInt8TypedArray(length, position, value) {
    if (length <= position || position < 0) {
        throw new Error('Position outside range')
    }

    const buffer = new ArrayBuffer(length)
    const viewer = new DataView(buffer)
    viewer.setInt8(position, value)

    return viewer
}
