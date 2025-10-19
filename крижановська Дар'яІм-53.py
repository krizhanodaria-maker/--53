#
# ...existing code...
type Num = { n: number };

# 1) Скалярна версія — повертає нове значення
function inc(n: number): number {
    return n + 1;
}

# 2) Версія для об'єкта — змінює поле в переданому об'єкті
function incObj(num: Num): void {
    num.n += 1;
}

# Приклади використання
const a = 5;
const b = inc(a);
console.dir({ a, b }); // a:5, b:6

const obj: Num = { n: 5 };
incObj(obj);
console.dir(obj); // { n: 6 }

# ------------------------
# Підрахунок типів у масиві
const items = [
    true, 'hello', 5, 12, -200, false, false, 'word',
    null, undefined, { x: 1 }, [1, 2], Symbol('s'), 3n
];

const counts: Record<string, number> = {}; # початково пустий — ключі додаються динамічно

for (const item of items) {
    const t = typeof item;           # 'number', 'string', 'boolean', 'object', 'symbol', 'bigint', 'undefined'
    counts[t] = (counts[t] ?? 0) + 1;
}

console.log(counts);
# Приклад результату: { boolean: 3, string: 2, number: 4, object: 3, undefined: 1, symbol: 1, bigint: 1 }
