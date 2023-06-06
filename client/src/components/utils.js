function salt(length = 6) {
    return Array.from(Array(length), () =>
        Math.floor(Math.random() * 16).toString(16)
    ).join('');
}
export default { salt };
