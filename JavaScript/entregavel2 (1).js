function somatorio(numbers) {
    let sum = 0;
    for (let i = 0; i < numbers.length; i++) {
      sum += numbers[i];
    }
    return sum;
  }
  
  const numeros = [1, 2, 3, 4, 5];
  const resultado = somatorio(numeros);
  console.log('O somatório é:', resultado);
  