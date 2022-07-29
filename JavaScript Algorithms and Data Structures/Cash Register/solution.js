const currency = {
    "PENNY": 0.01,
    "NICKEL": 0.05,
    "DIME": 0.1,
    "QUARTER": 0.25,
    "ONE": 1,
    "FIVE": 5,
    "TEN": 10,
    "TWENTY": 20,
    "ONE HUNDRED": 100 
}
  
function checkCashRegister(price, cash, cid) {
    const changeCurr = []
    let result = {status: null, change: []}

    var eleTotal = 0
    let changes = cash - price;
    const newCid = cid.filter(ele => ele[1] !== 0).reverse()

    for (let e of cid){
        eleTotal += e[1]
    }
    eleTotal = eleTotal.toFixed(2)

    if (eleTotal < changes) {
        result.status = "INSUFFICIENT_FUNDS"
        return result
    } else if(eleTotal === changes.toFixed(2)){
        result.status = "CLOSED"
        result.change = cid
        return result
    } else {
        result.status = "OPEN"
        console.log(changes)
        newCid.forEach(ele => {
            let temp = [ele[0], 0]
            while (changes >= currency[ele[0]] && ele[1] > 0){
                temp[1] += currency[ele[0]]
                ele[1] -= currency[ele[0]]
                changes -= currency[ele[0]]
                changes = changes.toFixed(2)
        }
        if (temp[1] > 0){
            changeCurr.push(temp)
        }
      })
    }
    
    if (changes > 0){
        result.status = "INSUFFICIENT_FUNDS"
        result.change = []
        return result
    }
    result.change = changeCurr
    console.log(result)
    return result;
  }
  
  checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], 
                                ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], 
                                ["TWENTY", 60], ["ONE HUNDRED", 100]]);
  
  checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], 
                               ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], 
                               ["TWENTY", 60], ["ONE HUNDRED", 100]]);