//Encontrar el número mayor de una lista de números en un array

let numeros = [5, 10, 15, 60, 8]
let numero_maximo = 0
let tamaño = numeros.length

for(let i = 0; i < tamaño; i++){
    if(numero_maximo < numeros[i]){
        numero_maximo = numeros[i]
    }
}

console.log(numero_maximo)

let maximo = Math.max(5, 10, 15, 60, 8)
console.log(maximo)