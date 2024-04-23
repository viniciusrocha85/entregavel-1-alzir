function contarValoresInteiros(primeiroDado, N) {
    let contador = 0;
  
    for (let i = primeiroDado; i <= N; i++) {
      contador++;
    }
  
    return contador;
  }
  
  const primeiroDado = 5; 
  const N = 15; 
  
  const quantidadeDeValores = contarValoresInteiros(primeiroDado, N);
  
  console.log(`Existem ${quantidadeDeValores} valores inteiros entre ${primeiroDado} e ${N}.`);