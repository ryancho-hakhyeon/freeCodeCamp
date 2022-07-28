function convertToRoman(num) {
    const roman = {'I': 1, 'IV': 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, 
                   'XC': 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
    
    const numValues = Object.values(roman).reverse()
  
    const romanized = []
    while (num !== 0){
      for (let i in numValues){
        if (num >= numValues[i]){
          // console.log(numValues[i])
          const temp = Object.keys(roman).find(key => roman[key] === numValues[i])
          romanized.push(temp)
          num -= numValues[i]
          break
        }
      }
    }
    
    return romanized.join("");
  }
  
  convertToRoman(36);   // Ouput: XXXVI
  convertToRoman(649)   // Ouput: DCXLIX
  convertToRoman(97)    // Ouput: XCVII
  convertToRoman(891)   // Ouput: DCCCXCI
  convertToRoman(1023)  // Ouput: MXXIII
  convertToRoman(3999)  // Ouput: MMMCMXCIX
  convertToRoman(2014)  // Ouput: MMXIV