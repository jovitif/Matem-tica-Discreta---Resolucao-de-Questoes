import Complex from 'complex.js';
import { question } from 'readline-sync';

const tmp_a = question("Digite o valor do coeficiente correspondente ao A: ");
const tmp_b = question("Digite o valor do coeficiente correspondente ao B: ");
const tmp_c = question("Digite o valor do coeficiente correspondente ao B: ");

const a = tmp_a / tmp_a;
const b = tmp_b / tmp_a;
const c = tmp_c / tmp_a;

function quadraticRoot(a, b, c) {
  const sqrt = Complex(b * b - 4 * a * c).sqrt()
  const x1 = Complex(-b).add(sqrt).div(2 * a);
  const x2 = Complex(-b).sub(sqrt).div(2 * a);
  return {x1, x2};
}

function solveQuadraticEquation(a, b, c) {
  const delta = Math.pow(b, 2) - 4*a*c;
  const x1 = (((-b) + Math.sqrt(delta, 2)) / 2*a).toFixed(4);
  const x2 = (((-b) - Math.sqrt(delta, 2)) / 2*a).toFixed(4);

  if (delta > 0) {
    return `Solução para Delta > 0: Xn = C1*${x1}^n + C2*${x2}^n`;
  } else if (delta === 0) {
    return `Solução para delta = 0: Xn = C1*${x1}^n + C2*n*${x2}^n`;
  } else {
    const solution = quadraticRoot(a, b, c);
    return `Solução para delta < 0: Xn = C1* ${solution.x1}^n + C2* ${solution.x2}^n`;
  }
}

console.log(solveQuadraticEquation(a, b, c));
