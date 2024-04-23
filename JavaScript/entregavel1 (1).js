//numero primo 
function eprimo(n) {
    if (n <= 1) {
      return false;
    }
  
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) {
        return false;
      }
    }
  
    return true;
  }
  
  
  const numberToCheck = 17; 
  if (eprimo(numberToCheck)) {
    console.log(numberToCheck + ' é primo.');
  } else {
    console.log(numberToCheck + ' não é primo.');
  }
