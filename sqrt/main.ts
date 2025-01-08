function mySqrt(x: number) : number {

    if (x === 0 || x === 1) {
        return x;
    }

    let low : number = 0;
    let high: number = x - 1;
    let result : number = -1;

    while (low <= high) {
        const mid : number = Math.floor(low + (high - low) / 2);
        const sq : number = mid * mid;

        if (sq === x) {
            return mid;
        }

        if (sq > x) {
            high = mid - 1;
        } else {
            result = mid;
            low = mid + 1;
        }
    }
    return result;
}

