
function palindrome(str) {
    const alphAndnum = str.toLowerCase()
                          .match(/[a-z0-9]/g)

    return alphAndnum.join('') === alphAndnum.reverse().join('')
}

palindrome("eye");