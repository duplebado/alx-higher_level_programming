#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let big1 = Number(process.argv[2]);
  let big2 = Number(process.argv[3]);

  for (let i = 4; i < process.argv.length; i++) {
    let potentialBig = Number(process.argv[i]);
    let temp;

    if (big1 < potentialBig) {
      temp = big1;
      big1 = potentialBig;
      potentialBig = temp;
    }

    if (big2 < potentialBig) {
      temp = big2;
      big2 = potentialBig;
      potentialBig = temp;
    }
  }

  console.log(big1 < big2 ? big1 : big2);
}
