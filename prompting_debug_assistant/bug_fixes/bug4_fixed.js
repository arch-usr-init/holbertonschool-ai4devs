// Return exactly the final count items from an array.
function takeLast(items, count) {
  const result = [];
  const start = items.length - count;
  for (let index = start; index < items.length; index++) {
    result.push(items[index]);
  }
  return result;
}

const sample = [10, 20, 30, 40, 50];
const count = 3;
const result = takeLast(sample, count);
console.log("Last items:", result);
console.log("Expected:", [30, 40, 50]);
