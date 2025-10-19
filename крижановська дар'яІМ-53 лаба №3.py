# ...existing code...
#**
# * 1. random(min, max)
 #* - if called with one argument random(max) => min = 0
 #* - returns integer in [min, max]
 #*
function random(min, max) {
  if (max === undefined) {
    max = min;
    min = 0;
  }
  min = Math.floor(min);
  max = Math.floor(max);
  if (max < min) [min, max] = [max, min];
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

#**
 #* 2. generateKey(length, characters)
 #* - returns string of given length built from characters
 #*
function generateKey(length, characters) {
  if (!characters || characters.length === 0) return '';
  let result = '';
  for (let i = 0; i < length; i++) {
    const idx = random(0, characters.length - 1);
    result += characters[idx];
  }
  return result;
}

#**
 #* 3. ipToNumber(ip = '127.0.0.1')
 #* - converts IPv4 like 'a.b.c.d' to 32-bit number using shifts
 #* - uses reduce and bitwise shifts; result is a signed 32-bit integer (matches examples)
 #*
function ipToNumber(ip = '127.0.0.1') {
  const parts = String(ip).split('.').map(s => Number(s) || 0).slice(0, 4);
  while (parts.length < 4) parts.push(0);
  # accumulate: ((p0 << 8 | p1) << 8 | p2) << 8 | p3
  return parts.reduce((acc, p) => (acc << 8) | (p & 0xff), 0);
}

#**
 #* 4. introspect iface
 #* - returns array of [key, argCount] for function-valued keys
 #*
function introspect(iface) {
  const res = [];
  for (const key of Object.keys(iface)) {
    const val = iface[key];
    if (typeof val === 'function') {
      res.push([key, val.length]);
    }
  }
  return res;
}

# ----------------------
# Examples / quick checks

# random
console.log('random 0..5:', random(5));       # 0..5
console.log('random 10..15:', random(10,15)); # 10..15

# generateKey
const chars = 'abcdefghijklmnopqrstuvwxyz0123456789';
console.log('key:', generateKey(16, chars));

# ipToNumber examples
console.log('127.0.0.1 ->', ipToNumber('127.0.0.1'));       # 2130706433
console.log('10.0.0.1  ->', ipToNumber('10.0.0.1'));        # 167772161
console.log('192.168.1.10 ->', ipToNumber('192.168.1.10')); # may be negative (signed 32-bit)

# introspect example
const iface = {
  m1: x => [x],
  m2: function (x, y) { return [x, y]; },
  m3(x, y, z) { return [x, y, z]; },
  notFn: 42
};
console.log('introspect:', introspect(iface));
# expected: [ ['m1',1], ['m2',2], ['m3',3] ]
# ...existing code...