


def calc(s):

	arr = []
	num = ""
	for i in range(len(s)):
		if s[i].isdigit():
			num += s[i]
		elif s[i]:
			arr.append(num)
			num = ""
			arr.append(s[i])
	arr = [elem for elem in arr if elem.strip()]

	stack = [[]]

	for i in range(len(arr)):
		if arr[i] == '(':
			stack.append([])
		elif arr[i] == ')':
			top = stack.pop()
			stack[-1].append(top)
		else:
			stack[-1].append(arr[i])

	print stack



s = "(+  (* 10 (+ 5 2) 2) 50)"
# 190
print calc(s)





# /*



# "(+ (* 10 (+ 5 2) 2) 50)"


# => 190


# 1) Parse the expression

# ["+", ["*", 10, ["+", 5, 2], 2], 50]

# 2) Evaluate the components

# */


# let test = "( + ( * 10 ( + 5 2 ) 2 ) 50 )"


# function parseExpression(str) {
# //   Split characters
#   let arr = str.split("");
  

  
# //   Concatonate the numbers
#   let newArr = [];
#   let currentNumber = "";
  
#   for(let i = 0; i < arr.length; i++) {
#     if(!isNaN(parseInt(arr[i]))) { //refactor
#       currentNumber += arr[i];
#     } else {
#       newArr.push(currentNumber);
#       currentNumber = "";
#       newArr.push(arr[i]);
#     }
#   }
  
#   let chars = newArr.filter(char => char != "" && char != " ");
  
  
#   let stack =[[]];
  
 
# //   [[] ["+"], ["*", "10", ["+", "5", "2"]]]
  
#   for(let i = 0; i < chars.length ; i++) {
#     if(chars[i] === "(") {
#       stack.push([]);
#     } else if(chars[i] === ")") {
#       let top = stack.pop();
#       stack[stack.length - 1].push(top);
#     } else {
#       stack[stack.length - 1].push(chars[i]);
#     }
#   }
  
#   let expr = stack[0][0]
  
#   console.log(evaluateExpression(expr))

# }

# function evaluateExpression(expr) {
#   let accumulator;
  
#   if(expr[0] === "*") {
#     accumulator = 1;
#     for(let i = 1; i <expr.length; i++) {
#       if(Array.isArray(expr[i])) {
#         accumulator *= evaluateExpression(expr[i]);
#       } else {
#         accumulator *= parseInt(expr[i])
#       }
#     }
#   }
  
#   else if(expr[0] === "+") {
#     accumulator = 0;
#     for(let i = 1; i <expr.length; i++) {
#       if(Array.isArray(expr[i])) {
#         accumulator += evaluateExpression(expr[i]);
#       } else {
#         accumulator += parseInt(expr[i])
#       }
#     }
#   }
#   return accumulator;
# }







# parseExpression(test)


# function parseExpression(str){
#   let res = [];
#   let cNum = '';
#   const isNum = c => '123456789.0'.includes(c);
  
#   for(let i = 0; i < str.length; i++){
#     if(isNum(str[i])){ 
#       cNum += str[i];
#       if(!isNum(str[i+1])){
#         res.push(Number(cNum));
#         cNum = '';
#       }
#     }
#     else if(str[i] !== ' '){ res.push(str[i]); }
#   }
#   return res;
# }


