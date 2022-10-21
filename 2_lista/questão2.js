import Complex from 'complex.js';
import { question } from 'readline-sync';

const A = question("Digite o valor de r : ");
const B = question("Digite o valor de pr : ");
const C = question("Digite o valor de q : ");

const r = A / A;
const pr = B / A;
const q = C / A;



function main(a, b, c) {
  
    const delta = Math.pow(b, 2) - 4*a*c;
    


    if (delta > 0) {
        const x1 = (((-b) + Math.sqrt(delta, 2)) / 2*a).toFixed(4);
        const x2 = (((-b) - Math.sqrt(delta, 2)) / 2*a).toFixed(4);
        return `Resultado : Xn = C1*${x1}^n + C2*${x2}^n`;
    } 
    else if (delta === 0) 
    {
        const x1 = (((-b) + Math.sqrt(delta, 2)) / 2*a).toFixed(4);
        return `Resultado : Xn = C1*${x1}^n + C2*n*${x2}^n`;
    } 
    else 
    {
        const sqrt = Complex(b * b - 4 * a * c).sqrt()
        const x1 = Complex(-b).add(sqrt).div(2 * a);
        const x2 = Complex(-b).sub(sqrt).div(2 * a);
        return `Resultado: Xn = C1*(${x1})^n + C2*(${x2})^n`;
    }
}

console.log(main(a, b, c));
