function words(str) {
  
    var result = {};
    // split on whitespace, including newline
    str.split(/[\s]+/).forEach(function(word) {
    result[word] = (+result[word] || 0) + 1;

    });
    return result;
  
}
console.log(words("twinkle twinkle little star"));
