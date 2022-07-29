function rot13(str) {
    const minRange = 'A'.charCodeAt()
    const maxRange = 'Z'.charCodeAt()
  
    const strArr = str.split("")
    const decrypted = []
  
    for (let c of strArr) {
      const temp = c.charCodeAt()
      if (temp >= minRange && temp <= maxRange){
        const decryptedLetter = temp + 13
        if (decryptedLetter > maxRange){
          const tempStr = (decryptedLetter - maxRange - 1) + minRange
          decrypted.push(String.fromCharCode(tempStr))
        } else {
          decrypted.push(String.fromCharCode(decryptedLetter))
        }
      } else {
        decrypted.push(c)
      }
    }
  
    return decrypted.join("");
  }
  
  rot13("SERR PBQR PNZC");

//                   1                   2
// 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
// a b c d e f g h i j k l m n o p q r s t u v w x y z
// n o p q r s t u v w x y z a b c d e f g h i j x l m