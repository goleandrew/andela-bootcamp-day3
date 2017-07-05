function words(str) {

  var result={};

  str.split(" ").forEach(function(el,i,arr){
    result[el] =  result[el]? ++result[el]: 1;
  });
  return result;
  
}
console.log(words("twinkle twinkle little star"));
