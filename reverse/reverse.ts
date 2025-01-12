// A funtion that reverses an int
//
//
//

function reverse(x: number): number {

    let res: number = 0;
    let flag: boolean = false;

    if (x < 0) {
        x = -x;
        flag = true;
    }

    while (x > 0) {
        res = res * 10 + (x % 10);
        x = Math.floor(x / 10);
    }

    return flag ? -res : res;
};
