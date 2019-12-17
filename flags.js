const texto = 'Carlos assinou o abaixo assinado'

console.log(texto.match(/C|ab/)) // sem flag global não acha ab
console.log(texto.match(/c|ab/i))
console.log(texto.match(/ab|c/gi))
