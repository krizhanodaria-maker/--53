const inc = x => ++x;
const twice = x => x * 2;
const cube = x => x ** 3;

function compose(...functions) {
  return (x) => {
    try {
      for (let i = functions.length - 1; i >= 0; i--) {
        const fn = functions[i];
        if (typeof fn !== "function") return undefined;
        x = fn(x);
      }
      return x;
    } catch {
      return undefined;
    }
  };
}

const fn1 = compose(inc, twice, cube);
const fn2 = compose(inc, inc);
const fn3 = compose(inc, 7, cube);

console.log(fn1(5));  // 251
console.log(fn2(7));  // 9
console.log(fn3(10)); // undefined
