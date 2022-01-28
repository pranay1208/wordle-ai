// Adapted from https://en.wikipedia.org/wiki/Letter_frequency
// Each letter corresponds to its a percentage, thus making this normalized. If a letter appears twice in a word, we will divide its "utility" by 10
const letterWeight = {
  a: 8.2,
  b: 1.5,
  c: 2.8,
  d: 4.3,
  e: 13,
  f: 2.2,
  g: 2,
  h: 6.1,
  i: 7,
  j: 0.15,
  k: 0.77,
  l: 4,
  m: 2.5,
  n: 6.7,
  o: 7.5,
  p: 1.9,
  q: 0.095,
  r: 6,
  s: 6.3,
  t: 9.1,
  u: 2.8,
  v: 0.98,
  w: 2.4,
  x: 0.15,
  y: 2,
  z: 0.074,
};

export default letterWeight;
