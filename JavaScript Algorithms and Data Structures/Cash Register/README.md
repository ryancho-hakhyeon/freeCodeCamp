# Cash Register

<p> Design a cash register drawer function checkCashRegister() that accepts purchase price as the first argument (price), payment as the second argument (cash), and cash-in-drawer (cid) as the third argument. </p>

<p> cid is a 2D array listing available currency. </p>

<p> The checkCashRegister() function should always return an object with a status key and a change key. </p>

<p> Return {status: "INSUFFICIENT_FUNDS", change: []} if cash-in-drawer is less than the change due, or if you cannot return the exact change. </p>

<p> Return {status: "CLOSED", change: [...]} with cash-in-drawer as the value for the key change if it is equal to the change due. </p>

<p> Otherwise, return {status: "OPEN", change: [...]}, with the change due in coins and bills, sorted in highest to lowest order, as the value of the change key. </p>

Currency Unit	        Amount
Penny	                $0.01 (PENNY)
Nickel	                $0.05 (NICKEL)
Dime	                $0.1 (DIME)
Quarter	                $0.25 (QUARTER)
Dollar	                $1 (ONE)
Five Dollars	        $5 (FIVE)
Ten Dollars	            $10 (TEN)
Twenty Dollars	        $20 (TWENTY)
One-hundred Dollars	    $100 (ONE HUNDRED)

<p> See below for an example of a cash-in-drawer array: </p>
[
  ["PENNY", 1.01],
  ["NICKEL", 2.05],
  ["DIME", 3.1],
  ["QUARTER", 4.25],
  ["ONE", 90],
  ["FIVE", 55],
  ["TEN", 20],
  ["TWENTY", 60],
  ["ONE HUNDRED", 100]
]