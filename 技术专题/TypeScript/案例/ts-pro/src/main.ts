interface LengthObj {
  length: number
}
function logLen<T extends LengthObj>(obj: T) {
  console.log(obj.length);
  
}


logLen({length: 10})