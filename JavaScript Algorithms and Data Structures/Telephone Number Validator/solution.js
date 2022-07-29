function telephoneCheck(str) {
    // 1. If there is country number, checked country number with the space 
    // 2. Checked the first three numbers, only allowed numbers with or without brackets'()'
    // 3. If there is dash '-' or spcase, checked validation. If there is nothing, allowed.
    // 4. Checked the second three numbers.
    // 5. If there is dash '-' or spcase, checked validation. If there is nothing, allowed.
    // 6. Checked the last four numbers.
    // 7. Specified the pattern with start 1 and followed the above condition till the end.
    const reg = /^(1\s?)?(\d{3}|\(\d{3}\))[\-\s]?\d{3}[\-\s]?\d{4}$/

    return reg.test(str);
  }
  
  telephoneCheck("555-555-5555");