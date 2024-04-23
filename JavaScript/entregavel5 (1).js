function quicksort(array) {
    if (array.length <= 1) {
      return array;
    }
  
    const pivot = array[0];
    const left = [];
    const right = [];
  
    for (let i = 1; i < array.length; i++) {
      if (array[i] < pivot) {
        left.push(array[i]);
      } else {
        right.push(array[i]);
      }
    }
  
    return [...quicksort(left), pivot, ...quicksort(right)];
  }
  
  const arrayParaOrdenar = [7, 2, 1, 6, 8, 5, 3, 4]; 
  const arrayOrdenado = quicksort(arrayParaOrdenar);
  
  console.log('Array ordenado:', arrayOrdenado);